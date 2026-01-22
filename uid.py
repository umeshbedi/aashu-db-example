import secrets
import string

# Define the characters allowed (alphanumeric + hyphen + underscore)
alphabet = string.ascii_letters + string.digits + '-_'
# Generate an 11-character string
uid = ''.join(secrets.choice(alphabet) for _ in range(11))
print(uid)
