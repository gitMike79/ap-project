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

    def try_again(self):
        self.find_file()

    def red_create(self):
        print("\n")
        self.newUser = CreateAccount()
        self.newUser.fillInfo()
        self.newUser.signUp()

    def authenticate_password(self):
        self.passInput = input("Password: ")
        tries = 0
        while tries < 5:
            if self.passInput == self.passStr:
                print("Success!")
                break
            else:
                print("The password you entered does not match with your account.\n"
                      "Please try again.")
                self.passInput = input("Password: ")
            tries += 1

        if self.passInput != self.passStr:
            print("You have exceeded the maximum number of trials.\nTry again later.")


if __name__ == "__main__":
    test = logIn("test")
    if test.find_file() == True:
        test.authenticate_password()
    else:
        test.try_again()
        test.red_create()                         
