from passlib.context import CryptContext

# Create a CryptContext instance with the chosen hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash a password using the chosen hashing algorithm (bcrypt).

    Args:
        password (str): The plaintext password.

    Returns:
        str: The hashed and salted password.
    """
    return pwd_context.hash(password)
