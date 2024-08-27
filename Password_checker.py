import random
import string

# Define the allowed characters
ALLOWED_CHARACTERS = string.ascii_letters + string.digits + "!$%^&*()-_=+"

# Function to check the strength of the password
def check_password_strength(password):
    if len(password) < 8 or len(password) > 24:
        return "Error: Password length must be between 8 and 24 characters."

    for char in password:
        if char not in ALLOWED_CHARACTERS:
            return "Error: Password contains invalid characters."

    score = len(password)
    unique_char_types = 0

    if any(char.islower() for char in password):
        unique_char_types += 1
    if any(char.isupper() for char in password):
        unique_char_types += 1
    if any(char.isdigit() for char in password):
        unique_char_types += 1
    if any(char in "!$%^&*()-_=+" for char in password):
        unique_char_types += 1

    score += unique_char_types * 2  # Award 2 points for each unique character type

    if score > 20:
        strength = "strong"
    elif score <= 10:
        strength = "weak"
    else:
        strength = "medium"

    return f"Password strength: {strength}, Score: {score}"

# Function to generate a strong password
def generate_strong_password ():
    password_range = random.randint (11,12)
    generate_random_password = ''.join (random.choice(ALLOWED_CHARACTERS)for _ in range(password_range))
    
    score = len(generate_random_password)
    unique_char_types = 0
    
    if any(char.islower() for char in generate_random_password):
        unique_char_types += 1
    if any(char.isupper() for char in generate_random_password):
        unique_char_types += 1
    if any(char.isdigit() for char in generate_random_password):
        unique_char_types += 1
    if any(char in "!$%^&*()-_=+" for char in generate_random_password):
        unique_char_types += 1

    score += unique_char_types * 2  # Award 2 points for each unique character type

    if score >= 20:
        strength = "strong"
    elif score <= 10:
        strength = "weak"
    else:
        strength = "medium"
    
    return(f"Generated password: {generate_random_password}, Score: {score},strengh: {strength}")

# Main program loop
def main():
    while True:
        print("\nMenu:")
        print("1. Check Password")
        print("2. Generate Password")
        print("3. Quit")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            password = input("Enter a password: ")
            result = check_password_strength(password)
            print(result)
        elif choice == '2':
            generate_random_password ,score = generate_strong_password()
            print(f"Generated password: {generate_random_password}, Score: {score}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

    #hello just seening if this works ok 