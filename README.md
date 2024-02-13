# Random Email Generator

This Python script generates random email addresses. It follows these steps:

**Character Set:** The script defines a character set containing lowercase letters, underscores, and periods
              
    ('abcdefghijklmnopqrstuvwxyz_.')
    
<br>
**Random Lengths:** It randomly selects lengths for the email username, domain name, and top-level domain (TLD). The username length is between 5 and 12 characters, the domain name length is between 4 and 7 characters, and the TLD length is between 2 and 3 characters.

<br>
**Username Generation:** `The generate_string()` function creates a random string of characters based on the specified length.

<br>
**Validating Usernames:** `The is_valid_username()` function checks if the generated username contains at most one period (to ensure it’s a valid format).

<br>
**Email Composition:** The main function, `generate_email()`, repeatedly generates usernames until a valid one is found. It then generates a random domain and combines them to form an email address.

<br>
**Output:** The script prints the generated email address.
