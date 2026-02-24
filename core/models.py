from datetime import datetime
import uuid

class User:
    def __init__(self, username, role):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.role = role  # admin / user / attacker
        self.failed_attempts = 0
        self.created_at = datetime.utcnow()
        self.nonce = None
        self.key_id = None
        self.hash = None


class Object:
    def __init__(self, filename, owner_id, sensitivity_level):
        self.object_id = str(uuid.uuid4())
        self.filename = filename
        self.owner_id = owner_id
        self.sensitivity_level = sensitivity_level  # low/medium/high
        self.encryption_at_rest = False  # metadata only
        self.created_at = datetime.utcnow()