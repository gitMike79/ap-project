from CreateAccount import *

class logIn:

    def __init__(self, CreateAccount):
        pass

    def find_file(self):
        self.userName = input("Username: ")
        try:
            openF = open("%sPASS.txt" % self.userName, 'r')
            self.passStr = openF.readline()
            openF.close()
            return True

        except:
            print("The username you entered does not exsits\nClick \'here\' to create an account instead"
                  " or click \'here\' to try again.")
            return False

    def try_again(self):                      #Michael this is front end stuff. If the user click on the
        self.find_file()                      #'here' button to try again this method should execute

    def go_to_create(self):
        print("\n")                           #Same thing here bro. If the user clicks on the second 'here'
        self.newUser = CreateAccount()        #button that I want you to create, this method should run
        self.newUser.fillInfo()
        self.newUser.signUp()

    def authenticate_password(self):
        self.passInput = input("Password: ")
        while self.passInput != self.passStr:
            if self.passInput == self.passStr:
                break
            else:
                print("The password you entered does not match with your account.\n"
                      "Please try again.")
                self.passInput = input("Password: ")
        print("Success!")




test = logIn("test")

if test.find_file() == True:
    test.authenticate_password()
else:
    test.try_again()                          #elif-else here for userclick depending if he clicks
    test.go_to_create()                       #on try again or clicks on create an account