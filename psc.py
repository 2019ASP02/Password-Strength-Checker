# Import string library
import string

# Input from user
pwd = input('Enter the password: ')

# Password strength check function
def password_strength_check(pw):
    # Compute password length
    length = len(pw)

    # Check if password contains different character types
    has_upper = any(c.isupper() for c in pw)  # Uppercase letters
    has_lower = any(c.islower() for c in pw)  # Lowercase letters
    has_punctuation = any(char in string.punctuation for char in pw)  # Special characters
    has_numbers = any(char.isdigit() for char in pw)  # Digits

    # Initialize strength variable
    strength = 0

    # Check password length greater than 8 characters
    if length > 8:
        strength += 1
    if has_lower:
        strength += 1
    if has_upper:
        strength += 1
    if has_punctuation:
        strength += 1
    if has_numbers:
        strength += 1

    # Return password strength based on conditions
    return (
        "Very Strong" if strength == 5 else
        "Strong" if strength == 4 else
        "Average" if strength == 3 else
        "Weak" if strength == 2 else
        "Very Weak"
    )

# Display the password strength
print('Password Strength:', password_strength_check(pwd))
