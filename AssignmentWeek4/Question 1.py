class User:
    active_users = 0

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.is_active = 1

        User.active_users+=1

    def get_role(self):
        return "Base User"
    
    def deactivate(self):
        if self.is_active:
            self.is_active = 0
            User.active_users-=1
            if(isinstance(self, Admin)):
                Admin.active_admins-=1
            elif(isinstance(self, Customer)):
                Customer.active_customers-=1

class Admin(User):
    active_admins = 0

    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        Admin.active_admins+=1
    
    def get_role(self):
        return 'Admin User'
    
    def delete_user(self, user):
        user.deactivate()

class Customer(User):
    active_customers = 0

    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        Customer.active_customers+=1

    def get_role(self):
        return 'Customer User'

    def place_order(self):
        return "Order Placed"

admin = Admin(1, "Nakil", "Nakil@gmail.com")
customer = Customer(2, "Test", "Test@gchj.com")

print(admin.get_role())
print(customer.get_role())

print(f'Number of Users: {User.active_users}')
print(f'Number of Admins: {Admin.active_admins}')
print(f'Number of Customers: {Customer.active_customers}')

print(customer.place_order())
admin.delete_user(customer)

print(f'Number of Users: {User.active_users}')
print(f'Number of Admins: {Admin.active_admins}')
print(f'Number of Customers: {Customer.active_customers}')