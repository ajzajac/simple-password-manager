import json
from cryptography.fernet import Fernet

def generate_key():
    #Generates an encryption key
    return Fernet.generate_key()

def encrypt_password(password, key):
    # Encrypts a password using given key
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password, key):
    # Decrypts an encrypted password using the given key
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()

def load_data(filename="passwords.json"):
    # Loads the password data from the json file
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data, filename="passwords.json"):
    # Saves the password data to the json file
    with open(filename, "w") as f:
        json.dump(data, f)

def main():
    # Main function for the password manager

    key = generate_key()
    data = load_data()

    while True:
        choice = input("What do you want to do? (add, get, list, quit): ")

        if choice == "add":
            website = input("Enter the website name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            data[website] = {
                "username": username,
                "password": encrypt_password(password, key)
            }

        elif choice == "get":
            website = input("Enter the website name: ")
            if website in data:
                print("Username:", data[website]["username"])
                print("Password:", decrypt_password(data[website]["password"], key))
            else:
                print("Website not found.")
        elif choice == "list":
            for website in data:
                print(website)
        elif choice == "quit":
            save_data(data)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()