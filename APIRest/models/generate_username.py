# username_generator.py

from models import Waiter  # Import the Waiter class from the models module

def generate_username(waiter: Waiter):
    # Access the first name, first surname, and second surname from the Waiter object
    first_name = waiter.firstname.strip() if waiter.firstname else ""
    first_surname = waiter.lastname1.strip() if waiter.lastname1 else ""
    second_surname = waiter.lastname2.strip() if waiter.lastname2 else ""

    # Extract the first two letters from each part of the name
    first_letter_first_name = first_name[:2].lower() if first_name else ""
    first_two_letters_first_surname = first_surname[:2].lower() if first_surname else ""
    first_two_letters_second_surname = second_surname[:2].lower() if second_surname else ""

    # Combine to generate the username
    username = first_letter_first_name + first_two_letters_first_surname + first_two_letters_second_surname

    return username
