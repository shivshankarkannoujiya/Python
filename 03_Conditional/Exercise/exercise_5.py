"""
Age Verification System
You’re building a system to verify user age for access.

Tasks:

    - Define a function verify_age that accepts a string input named age_str.
    - Convert age_str to an integer using int().
    - Use a ternary operator to return:
"Access Granted" if age is 18 or older
"Access Denied" otherwise
"""


def verify_age(age_str: str):
    age = int(age_str)
    return "Access Granted" if age >= 18 else "Access Denied"
