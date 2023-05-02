import re 
class BasePasswordManager:
    def __init__(self):
        self.old_password = []
    def get_password(self):
        return self.old_password[-1]
    def is_correct(self, str_chk):
        return str_chk == self.old_password[-1]
    
class PasswordManager(BasePasswordManager):
    def __init__(self):
        super().__init__()
        self.regex = re.compile('[a-zA-Z0-9@_!#$%^8* ()<>?/\}{~:]*$')
    def check_level(self,password) :
        level = -1
        if password.isalpha() or password.isdigit(): level = 0
        elif password.isalnum(): level = 1
        elif self.regex.search(password) != None: level = 2
        return level
    def set_password(self, new_password):
        if len(self.old_password):
            last_password_level = self.check_level(self.old_password[-1])
            new_password_level = self.check_level(new_password)
            if last_password_level < new_password_level:
                self.old_password.append(new_password)
            elif last_password_level == 2 and new_password_level == 2:
                self.old_password.append(new_password)
        else:
            self.old_password.append(new_password)
    def get_level(self):
        return self.check_level(self.old_password[-1])
    

user1 = PasswordManager()
user1.set_password("12345")
print(user1.get_password())
user1.set_password("124sa")
print(user1.get_password())
user1.set_password("124sa$")
print(user1.get_password())
user1.set_password("Aman@1235")
print(user1.get_password())
user1.set_password('123455')
print(user1.get_password())