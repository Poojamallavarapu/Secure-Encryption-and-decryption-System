from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key_from_password(password: str) -> bytes:
    """Generate a Fernet key from the given password."""
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_message(message: str, password: str) -> str:
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()

def decrypt_message(token: str, password: str) -> str:
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    return fernet.decrypt(token.encode()).decode()

def encrypt_file(file_data: bytes, password: str) -> bytes:
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    return fernet.encrypt(file_data)

def decrypt_file(encrypted_data: bytes, password: str) -> bytes:
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)
