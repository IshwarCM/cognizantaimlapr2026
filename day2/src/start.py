""" 
    Application entry point for the day2 project.
"""

import random

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

if __name__ == "__main__":
    generated_otp = generate_otp()
    print(f"Generated OTP: {generated_otp}")