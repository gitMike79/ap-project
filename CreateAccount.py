import random
import string

class CreateAccount:

    def __init__(self):
        self.ID = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])
        print("\nThank you for selecting North Bergen Banking services! \n")
        self.userName = input("Create a username: ")
        self.userPassword = input("Create a Password: ")        #todo make basic password validation
        userPasswordConf = input("Re-enter you Password: ")

        while userPasswordConf != self.userPassword:
            print("\nYou have made a mistake.\nThe passwords you entered do not match. Please enter again.\n")
            self.userPassword = input("Create a Password: ")
            userPasswordConf = input("Re-enter you Password: ")

        print("\nCongratualtions! You have successfully initialized your account.\nPlease fill in your information"
                "so we can keep it in our records for the next time.\n")

    def fillInfo(self):
        self.firstName = input("What is your first name? ")
        self.lastName = input("What is your last name? ")
        self.MoB = int(input("\nPlease enter your date of birth.\nMonth (MM): "))
        self.DoB = int(input("Day (DD): "))
        self.YoB = int(input("Year (YYYY): "))                  #todo make DOB validation
        self.DOB = (self.MoB, self.DoB, self.YoB)
        self.userBalance = float(input("\nEnter your current balance: $"))

    def signUp(self):
        openF = open('%sPASS.txt'%self.userName, 'w')
        openF.write("%s"%self.userPassword)
        openF.close()
        print("\nWe have stored your information in our records." \
                "\nPlease use your ID number '", self.userName, "' to log into your account.")

if __name__ == "__main__":
    newAcc = CreateAccount()
    newAcc.fillInfo()
    newAcc.signUp()