#Una interfaz es una clase abstracta en el que todos los métodos son abstractos. Existe en otros lenguajes.
class User(Saveable):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        return 'Logged in!'
    
    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }