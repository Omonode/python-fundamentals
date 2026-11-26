import datetime
import validator

# Record when the session starts, so we can show the time and duration later
session_start = datetime.datetime.now()

print("=== MY UTILITY TOOLKIT ===")
print(f"Today is {session_start.strftime('%d/%m/%Y')} ({session_start.strftime('%A')})")

user_name = input("What is your name? ").strip()
if not user_name:                     # an empty name is falsy
    user_name = "Friend"

actions_done = []                     # every successful action is added here

while True:
    print("\n--- MENU ---")
    print("1. Celsius to Fahrenheit")
    print("2. BMI calculator")
    print("3. Password generator")
    print("4. Email checker")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()

    # ---------- 1. Temperature ----------
    if choice == "1":
        celsius_value = input("Enter the temperature in Celsius: ")
        try:
            c = float(celsius_value)
            fahrenheit = validator.celsius_to_fahrenheit(c)
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print(f"{c}°C equals {fahrenheit:.1f}°F")
            actions_done.append("temperature")

    # ---------- 2. BMI ----------
    elif choice == "2":
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in metres (e.g. 1.75): "))
            bmi, category = validator.calculate_bmi(weight, height)   # unpack the tuple
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print(f"Your BMI is {bmi:.1f}, which is {category}.")
            actions_done.append("bmi")

    # ---------- 3. Passwords ----------
    elif choice == "3":
        passwords = validator.generate_passwords()   # it handles its own questions
        for number, password in enumerate(passwords, start=1):
            print(f"  {number}. {password}")
        actions_done.append("password")

    # ---------- 4. Email ----------
    elif choice == "4":
        email = input("Enter an email address: ").strip()
        if validator.is_valid_email(email):
            print(f"'{email}' looks valid.")
        else:
            print(f"'{email}' is not a valid email (it needs '@' and '.').")
        actions_done.append("email")

    # ---------- 5. Exit ----------
    elif choice == "5":
        break

    else:
        print(f"'{choice}' is not an option. Please type a number from 1 to 5.")

# ---------- Session summary ----------
session_end = datetime.datetime.now()
seconds_used = int((session_end - session_start).total_seconds())

print("\n=== SESSION SUMMARY ===")
print(f"Temperatures converted : {actions_done.count('temperature')}")
print(f"BMI calculations       : {actions_done.count('bmi')}")
print(f"Password batches       : {actions_done.count('password')}")
print(f"Emails checked         : {actions_done.count('email')}")
print(f"Time spent             : {seconds_used // 60} min {seconds_used % 60} sec")
print(f"Goodbye, {user_name}!")
