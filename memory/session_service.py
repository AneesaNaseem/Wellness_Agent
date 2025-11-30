# ------------------ Session ------------------ #
class SessionService:
    def __init__(self):
        self.sessions = {}

    def start_session(self, user):
        if user not in self.sessions:
            self.sessions[user] = []

    def store_message(self, user, role, message):
        if user not in self.sessions:
            self.sessions[user] = []
        self.sessions[user].append({"role": role, "message": message})

    def get_session(self, user):
        if user not in self.sessions:
            self.sessions[user] = []
        return self.sessions[user]

