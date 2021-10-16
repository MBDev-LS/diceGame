from argon2 import PasswordHasher
ph = PasswordHasher()
import secrets

hash = ph.hash("Lewisham")
print(hash)

print(ph.verify(hash, "Lewisham"))

print(ph.check_needs_rehash(hash))

def hashpassword(password: str):
    return(ph.hash(password + ''.join([secrets.choice('QWERTYUIOPASDFGHJKLZXCVBNM')])))

phash = hashpassword(input())

ph.verify(phash['p'], input())
