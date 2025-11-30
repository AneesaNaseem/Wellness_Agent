# ------------------ Memory  ------------------ #
class MemoryBank:
    def __init__(self):
        self.store_data = {}

    def store(self, user, query, response):
        # Save chat logs per user
        if user not in self.store_data:
            self.store_data[user] = []

        self.store_data[user].append({
            "query": query,
            "response": response
        })
