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
                           5. press any  other key to exist ->
                           """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
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
    
    def signin(self):
        if self.username=='' and self.password=='':
            print("signup first by pressing 1 in menu")
        else:
            uname = input("enter your username here: ")
            pwd = input("enter your password here: ")
            if self.username==uname and self.password==pwd:
                print("you have signed in successfully!!")
                self.loggedin = True
            else:
                print("input correct credentials..")
        print("\n")
        self.menu()
    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here:")
            print(f"Following content has been posted: {txt}")
        else:
            print("you need to sign in to post something..")
        print("\n")
        self.menu()
    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Eter your message here: ")
            frnd=input("whom to send message: ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("you need to sign in to post something..")
        print("\n")
        self.menu()

# obj = chatbook()