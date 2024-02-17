# Welcome to Secure Code Game Season-1/Level-5!

# This is the last level of our first season, good luck!
import os
import secrets
import bcrypt
from argon2 import PasswordHasher

class Random_generator:

    # generates a random token using the secrets library for true randomness
    def generate_token(self, length=8, alphabet=(
    '0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(secrets.choice(alphabet) for i in range(length))

    # generates salt using the bcrypt library which is a safe implementation
    def generate_salt(self, rounds=12):
        return bcrypt.gensalt(rounds)

class Hasher:

    # produces the password hash by combining password + salt because hashing
    def password_hash(self, password, salt):
        ph = PasswordHasher()
        return ph.hash(password, salt=salt)

    # verifies that the hashed password reverses to the plain text version on verification
    def password_verification(self, password, password_hash):
        ph = PasswordHasher()
        return ph.verify(password_hash, password)

# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
PASSWORD_HASHER = 'Hasher'


# Contribute new levels to the game in 3 simple steps!
# Read our Contribution Guideline at github.com/skills/secure-code-game/blob/main/CONTRIBUTING.md