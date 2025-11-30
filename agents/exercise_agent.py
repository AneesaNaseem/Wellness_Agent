class ExerciseAgent:
    def handle(self, query):
        q = query.lower()

        if "walk" in q:
            return {
                "agent": "exercise",
                "intent": "walk",
                "message": "A 30-minute walk is great for cardiovascular health."
            }

        if "run" in q:
            return {
                "agent": "exercise",
                "intent": "run",
                "message": "Running 20–30 minutes daily boosts stamina and mood."
            }

        if "stretch" in q:
            return {
                "agent": "exercise",
                "intent": "stretch",
                "message": "A 10-minute stretching session improves flexibility."
            }

        return {
            "agent": "exercise",
            "intent": "general",
            "message": "A mix of cardio, strength, and stretching each week keeps you balanced."
        }

