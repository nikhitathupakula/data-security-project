import hashlib
import time


# In-memory integrity metadata store (simulation)
integrity_store = {}


def generate_hash(data: bytes):
    """
    Generates SHA-256 hash of data.
    Returns hex digest.
    """
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()


def store_hash(object_id: str, data: bytes):
    """
    Stores hash and timestamp for an object.
    """
    hash_value = generate_hash(data)

    integrity_store[object_id] = {
        "hash": hash_value,
        "last_checked": time.time()
    }

    return hash_value


def verify_hash(object_id: str, data: bytes):
    """
    Verifies stored hash against current data.
    Returns True if valid, False if tampered.
    """

    if object_id not in integrity_store:
        raise Exception("Integrity record not found")

    stored_hash = integrity_store[object_id]["hash"]
    current_hash = generate_hash(data)

    integrity_store[object_id]["last_checked"] = time.time()

    if stored_hash == current_hash:
        return True
    else:
        return False


def get_integrity_metadata(object_id: str):
    """
    Returns integrity metadata.
    """

    if object_id not in integrity_store:
        raise Exception("Integrity record not found")

    return integrity_store[object_id]