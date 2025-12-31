class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @staticmethod
    def validate_inputs(name, email):
        if((email is None) or not ('@' in email and '.' in email)):
            print('Invalid Email Data')
            return False
        if name is None:
            print('Invalid Name')
            return False
        return True
    
    @classmethod
    def from_serialized_str(cls, data_str):
        name, email = data_str.split(':')

        if not cls.validate_inputs(name, email):
            raise ValueError('Invalid Data')
        
        return cls(name, email)
    
user = User.from_serialized_str("Nakil:Nakil@gmail.com")
print(user.name)
print(user.email)
