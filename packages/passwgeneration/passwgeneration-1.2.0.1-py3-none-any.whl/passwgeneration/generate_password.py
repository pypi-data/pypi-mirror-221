import random
import string
import os

# Get the current working directory
current_working_dir = os.getcwd()

# File names
PLACES_FILE = 'places.csv'
BIRD_FILE = 'bird.csv'

# File paths
places_file_path = os.path.join(current_working_dir, PLACES_FILE)
bird_file_path = os.path.join(current_working_dir, BIRD_FILE)

#places_file_path = os.path.join(current_working_dir, "passwgeneration", PLACES_FILE)
#bird_file_path = os.path.join(current_working_dir, "passwgeneration", BIRD_FILE)


# Read names from the files
with open(places_file_path, 'r', encoding='utf-8') as file1, open(bird_file_path, 'r', encoding='utf-8') as file2:
    names1 = set(name.strip().lower() for name in file1)
    names2 = set(name.strip().lower() for name in file2)
    names = names1.union(names2)

# Define function to generate random password
def generate_password():
    """
    Generate a random password that meets the specified requirement.

    Returns:
        str: A randomly generated password.
    """
    while True:
        # Generate random password with length between 6 and 12 characters
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 12)))

        # Check if password meets requirements and is not in the names set
        if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and password.lower() not in names:
            return password

# Call function to generate password and then print
RANDOM_PASSWORD = generate_password()

# Print the generated password
print(RANDOM_PASSWORD)

