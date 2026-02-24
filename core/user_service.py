from models import User

users = {}

def create_user(username, role):
    user = User(username, role)
    users[user.user_id] = user
    return user

def get_user(user_id):
    return users.get(user_id)