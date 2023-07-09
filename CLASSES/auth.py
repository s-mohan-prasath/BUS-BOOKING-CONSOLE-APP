from DB.connect import create_table, insert_auth_data
from functions import loading
from CLASSES.app import App

class Auth:
    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor
        self.username = None
        self.password = None
        self.open_app()

    def check_user_already_exists(self, username):
        self.cursor.execute(f"SELECT username FROM Users WHERE username='{username}'")
        for x in self.cursor:
            return True
        return False

    def create_acc(self):
        self.username = input("Enter the username: ")
        self.password = input("Enter the password: ")
        if not self.check_user_already_exists(self.username):
            query = "INSERT INTO Users (username, password) VALUES (%s, %s)"
            values = (self.username, self.password)
            self.cursor.execute(query, values)
            self.db.commit()
            loading()
            print("User created successfully")
            app = App()
        else:
            print("User already exists, try a different account or login...")
            self.create_acc()

    def login_acc(self):
        pass

    def open_app(self):
        inp = None
        while inp != "1" and inp != "2":
            print("""
            1. Create a new account
            2. Login to an existing account
            """)
            inp = input("Choose the Option -> ")
            if inp == "1":
                self.create_acc()
            elif inp == "2":
                print("Login Successful! 💖")
