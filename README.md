# Wellness_Agent

--------> Problem Statement
People often struggle to maintain consistent healthy habits. They often wonder what to eat, how much to walk, the intake of water, or how to build simple routines without needing medical advice. While information exists online it can be overwhelming sometimes and not personalized to a daily context. A lightweight conversational assistant that can provide quick guidance can make these everyday wellness tasks much more approachable.
The problem lies in accessibility and simplicity people want reliable, fast, everyday wellness suggestions without navigating complex apps, large platforms, or heavy interfaces. A small, local, conversational tool reduces friction and improves consistency in following healthier routines.

--------> Why Agents?
Agents work well here because they can respond in a flexible, natural way. Instead of behaving like a fixed webpage or a basic rule bot, an agent can think a little, keep context, and adjust how it replies. It can mix rule-based answers with LLM reasoning, remember the recent conversation, and handle unexpected questions smoothly.
For a wellness tool where questions change every day this mix of structure and flexibility fits perfectly.

--------> What I Created
I’ve built a wellness assistant that runs locally. It has three components:
1.	Rule-Based Routers
These handle simple questions about hydration, food, or exercise. If a question matches a known pattern, the agent answers instantly using clear rules.
2.	LLM Fallback System
If the question doesn’t fit a rule, the agent uses a Gemini model. If that model isn’t available, it automatically switches to another model. If all models fail, it replies with a safe fallback message so the user always gets something.
3.	Session Memory Layer
The agent stores recent messages so the LLM can answer in a way that fits the ongoing conversation.
With this architecture, even if external AI calls fail, the agent still works without crashing.

--------> Demo
The project runs in a simple terminal window.
Start it:
python3 app.py
Example Interaction
🌿 Wellness Agent Online 🌿
Hello, how may I assist you today?

Here’s something for your day:
“Your body is your lifelong home, care for it gently.”

Here's what you can ask me:
• How many liters of water should I drink today?
• Suggest a healthy breakfast.
• How much should I walk today?
• Give me a low-calorie dinner idea.

You: hello
Agent: Hello! I'm here to support your wellness. Ask me anything 🌿
You: How much should I walk today?
Agent: A 30-minute walk is great for cardiovascular health.
The demo showcases rule execution, fallback behavior, and error-resilient LLM integration.
 
--------> The Build
The tool is built using:
•	Python 3
•	google-generativeai
•	A simple SessionService to store message history
•	A rule router for quick answers
•	A model manager that picks the best available Gemini model
•	A basic console loop for interaction
Some design choices were intentional:
Keep dependencies small, make sure the agent doesn’t break when the LLM is down, keep rule logic separate from memory and model-handling, and keep the interface extremely simple.
This makes the agent easy to test and use on any system without needing a server or cloud setup.
 
--------> If I Had More Time
With more time, I would add:
•	A small web interface
•	Long-term memory to track habits
•	A knowledge module based on nutrition tables and activity guidelines
•	Voice input and output
•	User profiles for more personalized suggestions
•	Reminders or habit tracking
•	More wellness areas like sleep, stress, and daily routines
The current version is a solid foundation, and these upgrades would turn it into a more complete personal wellness helper.

