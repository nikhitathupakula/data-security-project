from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
from key_manager import get_key, increment_key_usage


def encrypt_data(plaintext: bytes, key_id: str):
    """
    Encrypts data using key_id.
    Returns nonce and ciphertext.
    """

    key = get_key(key_id)

    nonce = os.urandom(12)
    aesgcm = AESGCM(key)

    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    # Track usage
    increment_key_usage(key_id)

    return nonce, ciphertext


def decrypt_data(nonce: bytes, ciphertext: bytes, key_id: str):
    """
    Decrypts data using key_id.
    """

    key = get_key(key_id)

    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    # Track usage
    increment_key_usage(key_id)

    return plaintext