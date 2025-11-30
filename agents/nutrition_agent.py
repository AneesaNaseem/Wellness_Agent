class NutritionAgent:
    def handle(self, query):
        q = query.lower()

        if "calorie" in q:
            return {
                "agent": "nutrition",
                "intent": "calories",
                "message": "Typical daily intake ranges from 1600–2400 calories depending on age, sex, and activity level."
            }

        if "protein" in q:
            return {
                "agent": "nutrition",
                "intent": "protein",
                "message": "A simple guideline: 0.8g of protein per kilogram of body weight each day."
            }

        if "fruit" in q:
            return {
                "agent": "nutrition",
                "intent": "fruit",
                "message": "Two cups of fruit a day brings vitamins, fiber, and antioxidants without overloading sugar."
            }

        if "vegetable" in q or "veggies" in q:
            return {
                "agent": "nutrition",
                "intent": "vegetables",
                "message": "Aim for 3 cups of varied vegetables daily — leafy greens, colorful veggies, and legumes."
            }

        if "eat" in q or "diet" in q or "food" in q:
            return {
                "agent": "nutrition",
                "intent": "general",
                "message": "Balanced plates usually include lean proteins, whole grains, veggies, and healthy fats."
            }

        return {
            "agent": "nutrition",
            "intent": "fallback",
            "message": "Listening to your body and choosing whole foods most of the time keeps nutrition simple."
        }
