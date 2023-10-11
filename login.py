class Login:
    def __init__(self,username,email,password) -> None:
        self.username = username
        self.email = email
        self.password = password

    def info(self):
        return f"Hallo selamat pagi/siang/sore Mas {self.username}"

    def show(self):
        return f"Username : {self.username}\nEmail : {self.email}\nPassword : {self.password}"
    


username = input("Input your username : ")
email = input("Input your email : ")
password = input("Input your password : ")
user = Login(username,email,password)
print(user.info())
print(user.show())