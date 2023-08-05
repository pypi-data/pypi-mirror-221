class BigGoError(Exception):
    def __init__(self, message: str, cause: Exception = None):
        super().__init__(message)
        self.__cause__ = cause

class BigGoAuthError(Exception):
    def __init__(self, message: str, cause: Exception = None):
        message = message.replace('( app_id )', '( clientID )')
        message = message.replace('( app_key )', '( clientSecret )')
        super().__init__(message)
        self.__cause__ = cause