import re 

def check_password_strength(password):

    suggestions = [] 
    
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    
    # Check for lower, upper, digits, and special characters
    
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # If characters are not found, suggests to include them 
    if not has_upper:
        suggestions.append("Include at least one uppercase letter.")
    if not has_lower:
        suggestions.append("Include at least one lowercase letter.")
    if not has_digit:
        suggestions.append("Include at least one number.")
    if not has_special:
        suggestions.append("Include at least one special character.")
    
    # Estimates password strength based on characteristics 
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif len(password) >= 6 and ((has_upper and has_lower) or (has_digit and has_special)):
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions