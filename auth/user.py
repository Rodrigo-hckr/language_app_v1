class User:
    def __init__(self, username, plan):
        self.username = username
        self.plan = plan
        self.favorites = []
        
    def add_favorite(self, phrase):
        self.favorites.append(phrase)