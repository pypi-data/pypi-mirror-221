from HealthCheck_Pinger.core import PingHC
from functools import wraps

def pingDecor(uuid, server=None):
    """Custom decorator that pings HealthCheck Server"""
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if server:
                ping =PingHC(uuid, server)
            else:
                ping = PingHC(uuid)
            try:
                result =function(*args, **kwargs)
            except:
                ping.failure
                return False
            ping.success
            return result
        return wrapper
    return inner_function
