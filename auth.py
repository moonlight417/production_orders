def check_password(password, role):
    passwords = {
        "инженер": "engineer",
        "менеджер": "manager",
        "производство": "prod",
    }
    return passwords.get(role) == password