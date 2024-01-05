import random
import string

def generate_password(length):
    # Ensure a mix of numbers, letters, and symbols
    num_digits = random.randint(1, length // 3)
    num_letters = random.randint(1, (length - num_digits) // 2)
    num_symbols = length - num_digits - num_letters

    digits = ''.join(random.choice(string.digits) for _ in range(num_digits))
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(num_letters))
    symbols = ''.join(random.choice(string.punctuation) for _ in range(num_symbols))

    # Combine digits, letters, and symbols
    all_characters = digits + letters + symbols
    password = ''.join(random.sample(all_characters, length))

    return password

def main():
    print("Password Generator")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("Enter the desired length of the password: ")

        # Check for Quit option
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            length = int(user_input)
            if length > 0:
                # Generate and display the password
                password = generate_password(length)
                print(f"Generated Password: {password}")
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
