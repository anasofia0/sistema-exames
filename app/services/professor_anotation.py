from functools import wraps
from flask import abort
from flask_login import current_user

def professor_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.professor:  # Replace with your condition to check if the user is a professor
            abort(403)  # HTTP status code for "Forbidden"
        return f(*args, **kwargs)
    return decorated_function