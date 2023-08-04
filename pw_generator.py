import random
import string

def generate_password(length=12, num_passwords=1):
    # Mögliche Zeichen für das Kennwort
    characters = string.ascii_letters + string.digits + string.punctuation

    passwords = []
    for _ in range(num_passwords):
        # Zufällige Zeichen auswählen
        password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)

    return passwords

if __name__ == "__main__":
    password_length = int(input("Geben Sie die Länge des Kennworts ein (Standardmäßig 12): "))
    password_num = int(input("Wieviele Kennwörter benötigen Sie:"))
    password = generate_password(password_length, password_num)

print("Generiertes Kennwort:", password)
