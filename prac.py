class chatbook:
    def __init__(self):
        self.username = ' '
        self.password = ' '
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input(""""welcome to chatbook || How would you like to proceed?
                           1. press 1 to signup
                           2. press2 to signin
                           3. press 3 to wrote a post
                           4. press 4 to message friend
                           5. press any  other key to exist""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    def signup(self):
        email = input("enter your email :")
        pwd = input("setup your password:")
        self.username = email
        self.password = pwd 
        print("you have signed up successfully!!")
        print("\n")
        self.menu()

obj = chatbook()