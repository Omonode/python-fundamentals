import random
import string


def is_valid_email(email):
    """Return True if the email contains both '@' and '.'."""
    return "@" in email and "." in email


def is_positive(number):
    """Return True if the number is greater than 0."""
    return number > 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit. Raise ValueError for impossible values."""
    if not isinstance(c, (int, float)):
        raise ValueError("Temperature must be a number.")      # ← raise, NOT try
    if c < -273.15:
        raise ValueError(f"{c}°C is below absolute zero (-273.15°C).")
    return (c * 9 / 5) + 32


def calculate_bmi(weight_kg, height_m):
    """Return (bmi, category) for a weight in kg and a height in metres."""
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must both be greater than 0.")
    if height_m > 3:
        raise ValueError("Height looks too large. Enter it in metres, e.g. 1.75.")

    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


def generate_passwords():
    """Ask the user what they want, then return a list of mixed passwords."""
    # Each group is a tuple: (the name shown to the user, the characters to pick from)
    character_groups = [
        ("CAPITAL letters", string.ascii_uppercase),
        ("small letters", string.ascii_lowercase),
        ("numbers", string.digits),
        ("symbols", string.punctuation),
    ]

    # --- Part 1: ask how many of each group (keep asking until valid) ---
    while True:
        counts = []
        for group_name, group_characters in character_groups:
            while True:
                answer = input(f"How many {group_name} (0-20)? ").strip()
                try:
                    count = int(answer)
                except ValueError:
                    print(f"  '{answer}' is not a whole number. Please type a number like 3.")
                    continue
                if count < 0 or count > 20:
                    print("  Please choose a number from 0 to 20.")
                    continue
                counts.append(count)
                break                       # this group is done, go to the next one

        if sum(counts) > 0:
            break                           # at least 1 character, so stop asking
        print("  Your password would be empty. Please choose at least 1 character.\n")

    # --- Part 2: ask how many passwords ---
    while True:
        answer = input("How many passwords do you want (1-10)? ").strip()
        try:
            how_many = int(answer)
        except ValueError:
            print(f"  '{answer}' is not a whole number.")
            continue
        if how_many < 1 or how_many > 10:
            print("  Please choose a number from 1 to 10.")
            continue
        break

    # --- Part 3: build the passwords ---
    passwords = []
    for password_number in range(how_many):
        characters = []
        # enumerate gives the position, so counts[position] matches each group
        for position, (group_name, group_characters) in enumerate(character_groups):
            for i in range(counts[position]):
                characters.append(random.choice(group_characters))
        random.shuffle(characters)              # mix the list in place
        passwords.append("".join(characters))   # list → text, then store it

    return passwords


MAX_SCORE = 100


if __name__ == "__main__":
    # Quick tests: only run when validator.py itself is run
    print("Testing validator...")
    print(is_valid_email("a@b.com"))        # True
    print(is_positive(-5))                  # False
    print(celsius_to_fahrenheit(37))        # 98.6
    print(calculate_bmi(70, 1.75))          # (22.857142857142858, 'Normal')
    print(generate_passwords())             # asks questions, then shows the list
