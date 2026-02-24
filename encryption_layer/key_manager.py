import time
import uuid
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# In-memory key storage (simulation purpose)
key_store = {}

# Configuration
MAX_KEY_AGE_SECONDS = 60 * 60 * 24 * 30   # 30 days
MAX_KEY_USAGE = 1000                      # Usage threshold


def generate_key():
    """
    Generates a new AES-256 key and stores metadata.
    Returns key_id.
    """

    key_id = str(uuid.uuid4())
    key = AESGCM.generate_key(bit_length=256)

    key_store[key_id] = {
        "key": key,
        "created_at": time.time(),
        "last_rotated": time.time(),
        "usage_count": 0,
        "active": True
    }

    return key_id


def get_key(key_id):
    """
    Returns the raw key bytes for encryption/decryption.
    """

    if key_id not in key_store:
        raise Exception("Key not found")

    return key_store[key_id]["key"]


def increment_key_usage(key_id):
    """
    Increases usage counter for a key.
    """

    if key_id in key_store:
        key_store[key_id]["usage_count"] += 1
    else:
        raise Exception("Key not found")


def is_key_expired(key_id):
    """
    Checks whether key exceeded age or usage threshold.
    Returns True or False.
    """

    if key_id not in key_store:
        raise Exception("Key not found")

    key_data = key_store[key_id]

    age = time.time() - key_data["created_at"]
    usage = key_data["usage_count"]

    if age > MAX_KEY_AGE_SECONDS:
        return True

    if usage > MAX_KEY_USAGE:
        return True

    return False


def rotate_key(old_key_id):
    """
    Rotates a key:
    - Marks old key inactive
    - Generates new key
    - Returns new key_id
    """

    if old_key_id not in key_store:
        raise Exception("Old key not found")

    # Deactivate old key
    key_store[old_key_id]["active"] = False

    # Generate new key
    new_key_id = generate_key()

    return new_key_id


def get_active_keys():
    """
    Returns list of active key IDs.
    """

    return [
        key_id
        for key_id, data in key_store.items()
        if data["active"]
    ]


def get_key_metadata(key_id):
    """
    Returns metadata (without exposing raw key).
    """

    if key_id not in key_store:
        raise Exception("Key not found")

    data = key_store[key_id]

    return {
        "created_at": data["created_at"],
        "last_rotated": data["last_rotated"],
        "usage_count": data["usage_count"],
        "active": data["active"]
    }