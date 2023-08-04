import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Geben Sie die Länge des Kennworts ein (Standardmäßig 12): "))
    password_num = int(input("Wieviele Kennwörter benötigen Sie:"))
    password = generate_password(password_length, password_num)
    print("Generiertes Kennwort:", password)
