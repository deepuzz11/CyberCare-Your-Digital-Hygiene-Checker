import re
import string
import secrets
import hashlib
from utils.logger import log

def calculate_entropy(password):
    """Estimate password entropy in bits."""
    length = len(password)
    unique_chars = len(set(password))
    entropy = length * (unique_chars ** 0.5)
    return entropy

def password_strength(password):
    # Check entropy
    entropy = calculate_entropy(password)
    if entropy < 40:
        return "Weak", entropy
    if entropy < 60:
        return "Moderate", entropy
    return "Strong", entropy

def is_blacklisted(password):
    # A mock-up check for common passwords (a real-world check would integrate a larger list or API)
    blacklist = ["123456", "password", "qwerty", "admin", "letmein"]
    return password.lower() in blacklist

def run_check():
    log("Running advanced password strength check...")
    print("Enter a password to test:")
    password = input("Password: ")
    
    if is_blacklisted(password):
        print("Warning: This password is common and easily guessed. Choose a stronger one.")
        log(f"Password {password} is in blacklist.", "warning")
        return

    strength, entropy = password_strength(password)
    print(f"Password strength: {strength} (Entropy: {entropy} bits)")
    if strength == "Weak":
        print("Recommendation: Use at least 12 characters with a mix of upper, lower, numbers, and special characters.")
    log(f"Password strength evaluated as {strength} with entropy: {entropy} bits.")
