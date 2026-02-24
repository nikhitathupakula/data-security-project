import os
from key_manager import is_key_expired, rotate_key
from integrity import generate_hash


def perform_re_encryption(obj):
    """
    Simulates re-encryption of an object.
    Updates metadata only (no actual data yet).
    """

    if not obj.key_id:
        raise Exception("Object is not encrypted yet.")

    # Check if key expired
    if is_key_expired(obj.key_id):

        print(f"[+] Key expired for object {obj.object_id}. Rotating...")

        # Rotate key
        new_key_id = rotate_key(obj.key_id)

        # Update object metadata
        obj.key_id = new_key_id
        obj.nonce = os.urandom(12)

        # Simulate new hash (since data would be re-encrypted)
        obj.hash = generate_hash(obj.object_id.encode())

        print(f"[+] Re-encryption complete for object {obj.object_id}")

        return True

    else:
        print(f"[+] Key still valid for object {obj.object_id}")
        return False