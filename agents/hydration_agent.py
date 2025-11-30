class HydrationAgent:
    def handle(self, query):
        q = query.lower()

        if "how much" in q or "daily intake" in q:
            return {
                "agent": "hydration",
                "intent": "intake",
                "message": "Most adults need around 2–3 liters of water per day, depending on activity and climate."
            }

        if "dehydrated" in q or "thirsty" in q:
            return {
                "agent": "hydration",
                "intent": "symptoms",
                "message": "If you're feeling dehydrated, sip water slowly and avoid heavy caffeine for a while."
            }

        if "drink water" in q or "reminder" in q:
            return {
                "agent": "hydration",
                "intent": "reminder",
                "message": "Take a moment to sip a glass of water. Small, frequent hydration works best."
            }

        return {
            "agent": "hydration",
            "intent": "general",
            "message": "Staying hydrated keeps your energy steady and helps your body regulate temperature."
        }
