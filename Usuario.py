class Usuario:
    def __init__(self, username, password, age, avatar):
        self.username = username
        self.__password = password
        self.age = age
        self.avatar = avatar
        

    def show_attributes(self):
        print(f'Username: {self.username} Age: {self.age} Avatar: {self.avatar}')

    def get_password(self):
        return self.__password