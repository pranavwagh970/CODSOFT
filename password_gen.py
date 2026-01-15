import random
import string

def generate_password():
    print("--- Password Generator ---")
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("Password length should be at least 4 for better security.")
            return

        # Define character sets
        chars = string.ascii_letters + string.digits + string.punctuation
        
        # Generate password
        password = "".join(random.choice(chars) for _ in range(length))
        
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    generate_password()
