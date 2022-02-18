

class AuthenticationErrors:
    def __init__(self):
        self.errors = {
            'AU_01': ['Username does not exists', 'username']
        }

    def get_error(self, error_code):
        error = self.errors.get(error_code)
        err = {error[1]: [error[0]]}
        return err

    def raise_username_does_not_exist(self):
        return self.get_error('AU_01')
