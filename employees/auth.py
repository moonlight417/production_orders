from django.contrib.auth.hashers import check_password
from employees.models import Role

def authenticate(role_name, entered_password):
    try:
        role = Role.objects.get(name=role_name)
    except Role.DoesNotExist:
        return False
    return check_password(entered_password, role.password)