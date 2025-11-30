import time
import sys
import google.generativeai as genai

# local modules (keep your folder structure: memory/, agents/)
from agents.hydration_agent import HydrationAgent
from agents.nutrition_agent import NutritionAgent
from agents.exercise_agent import ExerciseAgent

from memory.memory_bank import MemoryBank
from memory.session_service import SessionService

# ---------------------------
# Gemini Setup (safe)
# ---------------------------
# replace with your key 
GENIE_API_KEY = ""  
try:
    genai.configure(api_key=GENIE_API_KEY)
except Exception:
    pass


def gemini_reply(prompt: str):
    """
    Safe wrapper for Gemini. If call fails, return a helpful fallback message.
    """
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
     
        if hasattr(response, "text"):
            return response.text.strip()
        if hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content[0].text.strip()
        return str(response)
    except Exception as e:
        # fallback
        print(f"[LLM ERROR] Gemini call failed: {e}")
        return "Sorry — I'm having trouble reaching the LLM right now. I can still answer simple hydration, nutrition, and exercise questions."

# ---------------------------
# WellnessAgent (Coordinator)
# ---------------------------
class WellnessAgent:
    def __init__(self, memory: MemoryBank, session_service: SessionService):
        self.memory = memory
        self.sessions = session_service

        self.hydration = HydrationAgent()
        self.nutrition = NutritionAgent()
        self.exercise = ExerciseAgent()

    def llm_fallback(self, user: str, query: str):
        """
        Build a context-aware prompt from recent session and call Gemini.
        Returns a dict consistent with other agents.
        """
        history = self.sessions.get_session(user)
        context = ""
        for msg in history[-10:]:
            role = "USER" if msg["role"] == "user" else "AGENT"
            text = msg["message"]  # use 'message' instead of 'text'
            context += f"{role}: {text}\n"

        prompt = (
            "You are a friendly, helpful wellness guide. Keep answers concise and focused on hydration, "
            "nutrition, exercise, sleep, and healthy routines.\n\n"
            f"{context}"
            f"USER: {query}\n"
            "ASSISTANT:"
        )

        reply = gemini_reply(prompt)
        return {"agent": "llm_fallback", "intent": "general", "message": reply}

    def route_to_agent(self, query: str):
        """
        Lightweight rule-based routing. Returns a response dict or None.
        """
        q = query.lower().strip()

        # greetings
        if any(k == q or k in q for k in ["hello", "hi", "hey"]):
            return {"agent": "greeting", "intent": "greet",
                    "message": "Hello! I'm here to support your wellness. Ask me anything 🌿"}

        # capabilities
        if "what can you do" in q or "features" in q or "abilities" in q or "what are your features" in q:
            return {
                "agent": "meta",
                "intent": "explain",
                "message": "I can help with hydration guidance, nutrition tips, exercise suggestions, and general wellness questions."
            }

        # hydration triggers
        words = set(q.split())
        if words & {"water", "drink", "hydration", "thirst"}:
            return self.hydration.handle(query)

        # nutrition triggers
        if words & {"eat", "food", "diet", "calorie", "protein", "fruit", "vegetable",
                    "breakfast", "dinner", "lunch", "apple"}:
            return self.nutrition.handle(query)

        # exercise triggers
        if words & {"exercise", "workout", "walk", "run", "stretch", "gym"}:
            return self.exercise.handle(query)

        # fallback to LLM 
        return None

    def handle_request(self, user: str, query: str):
        """
        Store incoming message, route to rule agents, fallback to LLM if needed,
        store agent reply in session and long-term memory, and return the response dict.
        """
        # ensure session exists
        self.sessions.start_session(user)
        # store user message with role
        self.sessions.store_message(user, "user", query)

        # try rule-based routing
        response = self.route_to_agent(query)

        # fallback to LLM
        if response is None:
            response = self.llm_fallback(user, query)

        # store agent reply in session and memory
        self.sessions.store_message(user, "agent", response["message"])
        try:
            self.memory.store(user, query, response)
        except Exception:
            print("[MEMORY WARNING] Could not write to long-term memory.")

        return response


# ---------------------------
# Startup Banner and runner
# ---------------------------
def welcome_animation():
    lines = [
        "",
        "🌿 Wellness Agent Online 🌿",
        "Hello, how may I assist you today?",
        "",
        "Here’s something for your day:",
        "“Your body is your lifelong home, care for it gently.”",
        "",
        "Here's what you can ask me:",
        "• How many liters of water should I drink today?",
        "• Suggest a healthy breakfast.",
        "• How much should I walk today?",
        "• Give me a low-calorie dinner idea.",
        ""
    ]

    for line in lines:
        print(line)
        time.sleep(0.06)

def main_loop():
    memory = MemoryBank()
    sessions = SessionService()

    user = "demo_user"
    sessions.start_session(user)

    agent = WellnessAgent(memory, sessions)

    welcome_animation()

    while True:
        try:
            query = input("You: ").strip()
        except EOFError:
            print("\n[INPUT] No stdin available — exiting interactive loop.")
            break

        if not query:
            continue

        if query.lower() in ["exit", "quit", "bye"]:
            print("Agent: Take care! 🌿 Goodbye.")
            break

        response = agent.handle_request(user, query)
        # print the agent message only (clean output)
        print("Agent:", response["message"])

if __name__ == "__main__":
    main_loop()
