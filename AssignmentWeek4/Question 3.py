class User:
    active_users = 0

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        User.active_users+=1

    def __str__(self):
        return f"{self.user_id} - {self.name} - {self.email}"
    
    def __repr__(self):
        return f"User(user_id={self.user_id}, name={self.name}, email={self.email})"
    
    def __len__(self):
        return len(self.name)
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id
    
    def __lt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id < other.user_id
    
    def __call__(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email
        }
    
user_1 = User(1, 'Nakil', "Nakil@gmail.com")
user_2 = User(1, "Nakil 1", 'Nakil2@email.com')
user_3 = User(2, 'Nakil 2', 'Nakil2@email.com')
    
print(user_1)
print(repr(user_2))
print(len(user_1))

print(f'user_1 is equals to user_2: {user_1==user_2}')
print(f'user_1 is less than user_3: {user_1<user_3}')

print(user_1())