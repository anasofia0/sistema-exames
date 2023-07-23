from flask import abort
from datetime import datetime, timedelta
from ..models import TempoExameAluno

def time_limit_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the time from your model
        # For the sake of this example, let's assume it's stored in a variable called `model_time`
        model_time = ... # Fetch this from your model
        
        # Check if the current time minus the model_time is more than 2 hours
        if datetime.now() - model_time > timedelta(hours=2):
            abort(403)  # HTTP status code for Forbidden
        return f(*args, **kwargs)
    return decorated_function
