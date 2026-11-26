# ============================================================
# LAGOS TECH WEEK — EVENT REGISTRATION SYSTEM
# File name: event_registration.py
#
# Manages attendee registration and session sign-ups for a
# 3-day conference at Landmark Centre, Victoria Island.
#
# NO OOP: the brief's two "classes" (Attendee and Session) are
# built from DICTIONARIES plus ordinary FUNCTIONS instead:
#   - each attendee is a dict:  {"name", "email", "phone", "ticket_type"}
#   - each session is a dict:   {"title", "speaker", "capacity", "attendees"}
#   - each "method" is a function that takes the dict as its first input
# Tools used: Topics 1–13 only (variables, loops, conditionals,
# strings, lists, dicts, functions, try/except, modules, CSV files).
# ============================================================

import csv
import datetime

VALID_TICKET_TYPES = ["Regular", "VIP"]

# Stands in for the class attribute Attendee.total_registered.
# A dictionary is used so functions can update it without `global`
# (changing an item INSIDE a dict doesn't need the global keyword).
REGISTRATION_STATS = {"total_registered": 0}


# ============================================================
# PHASE 1 — "ATTENDEE" AND "SESSION" (dicts + functions, no classes)
# ============================================================

# ---------- Attendee ----------

def create_attendee(name, email, phone, ticket_type):
    """Build and return an attendee dictionary; count it as registered."""
    attendee = {
        "name": name,
        "email": email,
        "phone": phone,
        "ticket_type": ticket_type,
    }
    # Same job as the class attribute: +1 every time an attendee is created
    REGISTRATION_STATS["total_registered"] += 1
    return attendee


def attendee_to_string(attendee):
    """Return text like 'Amara Okafor (amara@email.com) — VIP' (the __str__ job)."""
    return f"{attendee['name']} ({attendee['email']}) — {attendee['ticket_type']}"


def attendee_to_dict(attendee):
    """Return all attendee details as a NEW dictionary (the to_dict job).

    A copy is returned so that changing the result can't change the
    original record by accident (two names, one dict — Chapter 8 trap).
    """
    return {
        "name": attendee["name"],
        "email": attendee["email"],
        "phone": attendee["phone"],
        "ticket_type": attendee["ticket_type"],
    }


# ---------- Session ----------

def create_session(title, speaker, capacity):
    """Build and return a session dictionary with an empty attendee list."""
    if capacity <= 0:
        raise ValueError("Session capacity must be greater than 0.")
    return {
        "title": title,
        "speaker": speaker,
        "capacity": capacity,
        "attendees": [],          # a list of attendee EMAILS
    }


def session_to_string(session):
    """Return text like 'Intro to AI by Dr. Bello — 12/30 seats taken'."""
    taken = len(session["attendees"])
    return (f"{session['title']} by {session['speaker']} — "
            f"{taken}/{session['capacity']} seats taken")


def is_full(session):
    """Return True if the session has no seats left."""
    return len(session["attendees"]) >= session["capacity"]


def available_seats(session):
    """Return how many seats are still free."""
    return session["capacity"] - len(session["attendees"])


def add_attendee(session, attendee):
    """Sign an attendee up. Return True on success, or False with a printed reason."""
    email = attendee["email"]
    # Check duplicates first: someone already in should hear "already
    # signed up", not "session full", even when the session is full
    if email in session["attendees"]:
        print(f"  ✘ {attendee['name']} is already signed up for '{session['title']}'.")
        return False
    if is_full(session):
        print(f"  ✘ '{session['title']}' is full ({session['capacity']} seats). No seats left.")
        return False
    session["attendees"].append(email)
    return True


def remove_attendee(session, email):
    """Remove an email from a session. Return True if removed, False if not found."""
    email = email.strip().lower()
    if email in session["attendees"]:
        session["attendees"].remove(email)
        return True
    return False


# ============================================================
# INPUT HELPERS (validation loops with try/except — Topics 6 & 11)
# ============================================================

def ask_text(prompt):
    """Ask until the user types something that isn't blank."""
    while True:
        answer = input(prompt).strip()
        if answer:                       # empty text is falsy
            return answer
        print("  This field cannot be empty. Please try again.")


def is_valid_email(email):
    """Return True if the email has text before '@' and a '.' after it."""
    if email.count("@") != 1:
        return False
    username, domain = email.split("@")
    return username != "" and "." in domain and not domain.startswith(".") \
        and not domain.endswith(".")


def ask_email(prompt):
    """Ask until a valid-looking email is typed; return it in lowercase."""
    while True:
        email = ask_text(prompt).lower()
        if is_valid_email(email):
            return email
        print("  That doesn't look like a valid email (e.g. amara@email.com).")


def ask_phone(prompt):
    """Ask until a phone number of 10–14 digits is typed (spaces, + and - allowed)."""
    while True:
        phone = ask_text(prompt)
        digits = phone.replace(" ", "").replace("-", "").replace("+", "")
        if digits.isdigit() and 10 <= len(digits) <= 14:
            return phone
        print("  Enter a valid phone number, e.g. 08031234567 or +234 803 123 4567.")


def ask_ticket_type(prompt):
    """Ask until the user chooses Regular or VIP (any capitals)."""
    while True:
        answer = ask_text(prompt).strip()
        for ticket in VALID_TICKET_TYPES:
            if answer.lower() == ticket.lower():
                return ticket            # stored in its proper spelling
        print("  Ticket type must be Regular or VIP.")


def find_session_by_title(sessions, typed_title):
    """Return the session whose title matches (ignoring capitals), or None."""
    for title, session in sessions.items():
        if title.lower() == typed_title.strip().lower():
            return session
    return None


# ============================================================
# PHASE 2 — REGISTRATION FUNCTIONS
# ============================================================

def register_attendee(attendees):
    """Collect details with input(), create an attendee and add it. Rejects duplicate emails."""
    print("\n--- REGISTER ATTENDEE ---")
    name = ask_text("Full name: ").title()
    email = ask_email("Email: ")
    if email in attendees:
        print(f"  ✘ {email} is already registered to "
              f"{attendees[email]['name']}. Registration cancelled.")
        return False
    phone = ask_phone("Phone: ")
    ticket_type = ask_ticket_type("Ticket type (Regular / VIP): ")

    attendees[email] = create_attendee(name, email, phone, ticket_type)
    print(f"  ✔ Registered: {attendee_to_string(attendees[email])}")
    return True


def sign_up_for_session(attendees, sessions):
    """Ask for an email and a session title, then sign the attendee up with add_attendee()."""
    print("\n--- SIGN UP FOR SESSION ---")
    if not attendees:
        print("  No attendees registered yet. Register first (option 1).")
        return False

    email = ask_email("Attendee email: ")
    if email not in attendees:
        print(f"  ✘ No attendee registered with {email}.")
        return False

    print("  Sessions:")
    for number, session in enumerate(sessions.values(), start=1):
        seats = available_seats(session)
        status = "FULL" if is_full(session) else f"{seats} seat{'' if seats == 1 else 's'} left"
        print(f"   {number}. {session['title']} ({status})")

    choice = ask_text("Session title or number: ")
    session = None
    # Accept either the list number or the title
    if choice.isdigit():
        position = int(choice)
        titles = list(sessions.keys())
        if 1 <= position <= len(titles):
            session = sessions[titles[position - 1]]
    else:
        session = find_session_by_title(sessions, choice)

    if session is None:
        print(f"  ✘ No session called '{choice}'.")
        return False

    if add_attendee(session, attendees[email]):
        seats = available_seats(session)
        print(f"  ✔ {attendees[email]['name']} signed up for '{session['title']}'. "
              f"{seats} seat{'' if seats == 1 else 's'} left.")
        return True
    return False


def search_attendee(attendees, query):
    """Return a list of attendees whose name or email contains the query (case-insensitive)."""
    query = query.strip().lower()
    matches = []
    for attendee in attendees.values():
        if query in attendee["name"].lower() or query in attendee["email"].lower():
            matches.append(attendee)
    return matches


def find_attendee_sessions(sessions, email):
    """Return a list of the session titles this email is signed up for."""
    email = email.strip().lower()
    titles = []
    for title, session in sessions.items():
        if email in session["attendees"]:
            titles.append(title)
    return titles


# ============================================================
# PHASE 3 — PERSISTENCE, REPORT & MENU
# ============================================================

FIELDNAMES = ["name", "email", "phone", "ticket_type"]


def save_attendees(attendees, filename="attendees.csv"):
    """Save every attendee to a CSV file with csv.DictWriter."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for attendee in attendees.values():
                writer.writerow(attendee_to_dict(attendee))
    except OSError as e:
        print(f"  ✘ Could not save to {filename}: {e}")
        return False
    print(f"  ✔ Saved {len(attendees)} attendee(s) to {filename}.")
    return True


def load_attendees(filename="attendees.csv"):
    """Read the CSV and return an email → attendee dict. Missing file gives an empty dict."""
    attendees = {}
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                email = row.get("email", "").strip().lower()
                if not email or email in attendees:
                    continue                 # skip blank or repeated rows
                ticket = row.get("ticket_type", "Regular")
                if ticket not in VALID_TICKET_TYPES:
                    ticket = "Regular"
                attendees[email] = create_attendee(
                    row.get("name", "").strip(), email,
                    row.get("phone", "").strip(), ticket)
    except FileNotFoundError:
        return {}                            # first run: no file yet
    return attendees


def event_summary(sessions, attendees):
    """Print each session's enrolment, then the overall totals."""
    width = 64
    print("\n" + "=" * width)
    print(f"{'LAGOS TECH WEEK — EVENT SUMMARY':^{width}}")
    print(f"{'Landmark Centre, Victoria Island':^{width}}")
    print("=" * width)
    print(f"{'Session':<30}{'Speaker':<18}{'Enrolment':>12}")
    print("-" * width)

    total_signups = 0
    for session in sessions.values():
        taken = len(session["attendees"])
        total_signups += taken
        enrolment = f"{taken}/{session['capacity']} seats"
        full_tag = " [FULL]" if is_full(session) else ""
        print(f"{session['title']:<30}{session['speaker']:<18}{enrolment:>12}{full_tag}")

    vip_count = 0
    for attendee in attendees.values():
        if attendee["ticket_type"] == "VIP":
            vip_count += 1

    print("-" * width)
    print(f"Total registered attendees : {len(attendees)}")
    print(f"Total session sign-ups     : {total_signups}")
    print(f"VIP attendees              : {vip_count}")
    print(f"Regular attendees          : {len(attendees) - vip_count}")
    print("=" * width)


def create_default_sessions():
    """Return the conference's starting sessions (title → session dict)."""
    sessions = {}
    for title, speaker, capacity in [
        ("Intro to AI", "Dr. Bello", 30),
        ("Fintech in Africa", "Mrs. Adeyemi", 50),
        ("Cloud Security", "Engr. Okoro", 20),
        ("Startup Funding", "Mr. Danjuma", 3),     # small, so [FULL] is easy to test
    ]:
        sessions[title] = create_session(title, speaker, capacity)
    return sessions


def show_search(attendees, sessions):
    """Menu option 3: search, then show each match and the sessions they joined."""
    print("\n--- SEARCH ATTENDEE ---")
    query = ask_text("Name or email (part is fine): ")
    matches = search_attendee(attendees, query)
    if not matches:
        print(f"  No attendee matches '{query}'.")
        return
    print(f"  {len(matches)} match(es):")
    for number, attendee in enumerate(matches, start=1):
        joined = find_attendee_sessions(sessions, attendee["email"])
        joined_text = ", ".join(joined) if joined else "no sessions yet"
        print(f"   {number}. {attendee_to_string(attendee)} | {attendee['phone']}")
        print(f"      Sessions: {joined_text}")


def show_menu():
    """Print the main menu."""
    print("\n========== LAGOS TECH WEEK ==========")
    print("1) Register Attendee")
    print("2) Sign Up for Session")
    print("3) Search Attendee")
    print("4) Event Summary")
    print("5) Save & Exit")


def main():
    """Load data, run the menu loop, and save on exit."""
    attendees = load_attendees()
    sessions = create_default_sessions()

    print("Welcome to the Lagos Tech Week Registration System")
    print(f"Today: {datetime.date.today().strftime('%A %d %B %Y')}")
    print(f"Loaded {len(attendees)} attendee(s) from attendees.csv.")

    while True:
        show_menu()
        try:
            choice = int(input("Choose an option (1-5): ").strip())
        except ValueError:
            print("  Please type a number from 1 to 5.")
            continue
        except (EOFError, KeyboardInterrupt):
            # Input stream closed or Ctrl+C: still save before leaving
            print("\n  Input interrupted — saving and exiting.")
            save_attendees(attendees)
            break

        try:
            if choice == 1:
                register_attendee(attendees)
            elif choice == 2:
                sign_up_for_session(attendees, sessions)
            elif choice == 3:
                show_search(attendees, sessions)
            elif choice == 4:
                event_summary(sessions, attendees)
            elif choice == 5:
                save_attendees(attendees)
                print("Goodbye! See you at Lagos Tech Week.")
                break
            else:
                print("  That option doesn't exist. Choose 1 to 5.")
        except (EOFError, KeyboardInterrupt):
            print("\n  Input interrupted — saving and exiting.")
            save_attendees(attendees)
            break


# Run the menu only when this file is run directly, not when imported
if __name__ == "__main__":
    main()