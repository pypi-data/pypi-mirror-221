from termcolor import colored

class ApiError(Exception):
    """ 
    Generic error class, catch-all for most Tumblpy issues.
    from Tumblpy import FlickrAPIError, FlickrAuthError
    """
    def __init__(self, msg, error_code=None):
        self.msg = msg
        self.code = error_code

    def __str__(self):
        return colored(repr(self.msg), 'red')