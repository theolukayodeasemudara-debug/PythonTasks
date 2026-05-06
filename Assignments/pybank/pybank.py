def validate_email(email):
    if "@" not in email:
        raise ValueError("Invalid Email!")
    if email[0] == "@":
        return "Invalid email"
    if email[-1] == "0":
        return "Invalid email"
    if len(email) >= 8:
        return True
    return False

def calculate_balance(transactions):
    total = 0
    for amount in transactions:
        total += amount
    return total
