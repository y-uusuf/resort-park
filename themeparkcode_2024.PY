import string, os, time
from datetime import datetime

firstTimeLoggedOn = True

isLockedOut = False
payInCash = False

amountOfPeopleCurrentlyInThemePark = 0
currentTotal = 0

themepark = {
    'capacity': 500,
    'adult': 20,
    'child': 12,
    'senior': 11,
    'wristband': 20
}

adminLogin = {
   'user': 'root',
   'pass': 'adminpassword12345',
   '2fa': '2701'
}

cardDetails = {}

bookingInfo = {}



os.system("title Yusuf's Theme Park")

def main():

    def calculateTotalPrice(numberOfAdults, numberOfChildren, numberOfSeniors, numberOfWristbands):
        global prices, currentTotal
        
        priceOfAdults = numberOfAdults * themepark['adult']
        priceOfChildren = numberOfChildren * themepark['child']
        priceOfSeniors = numberOfSeniors * themepark['senior']
        priceOfWristbands = numberOfWristbands * themepark['wristband']

        currentTotal = priceOfAdults + priceOfChildren + priceOfSeniors + priceOfWristbands
        return currentTotal

    def Payment():
        
        global cardDetails, payInCash, currentTotal

        os.system("cls")

        print("===== PAYMENT INFORMATION =====")

        payInCash = input("Would you like to pay in cash? (Y/N or 'Yes'/'No')\n[Please note we only accept £10 & £20 notes.]\n> ").lower()
        
        while payInCash not in ['y', 'n', 'yes', 'no']:
            print("Sorry, that's an invalid response.")
            payInCash = input("Would you like to pay in cash? (Y/N or 'Yes'/'No')\n[Please note we only accept £10 & £20 notes.]\n> ").lower()

        if payInCash in ['y', 'yes']:
            payInCash = True
            totalDeposited = 0
            amountOwed = currentTotal

            while totalDeposited < currentTotal:
                print('===== PAYMENT IN CASH =====')
                notes_10 = int(input(f"How many £10 notes would you like to deposit? (You owe £{amountOwed}.) "))
                totalDeposited += notes_10 * 10
                amountOwed = currentTotal - totalDeposited

                if totalDeposited >= currentTotal:
                    break

                notes_20 = int(input(f"How many £20 notes would you like to deposit? (You owe £{amountOwed}.) "))
                totalDeposited += notes_20 * 20
                amountOwed = currentTotal - totalDeposited
                input("\nPress {ENTER} to continue.")
                os.system('cls')

            if amountOwed < 0:
                change = -amountOwed
                print(f"We owe you £{change}.")
                return

        elif payInCash in ['n', 'no']:
            while True:
                try:
                 cardNumber = int(input("\n\nPlease enter your card number: "))#
                 break
                except ValueError:
                    print("Invalid card number.")

            while True:
                try:
                 cvv = int(input("What is your CVV? (3 digit security code.): "))
                 break
                except:
                  print("Sorry, that's an invalid cvv.")
            

            expiryDay = int(input("Expiration day? "))
            while expiryDay > 31 or expiryDay < 1:
                expiryDay = int(input("Invalid expiration day. Expiration day? "))

            expiryMonth = int(input("Expiration month? "))
            while expiryMonth > 12 or expiryMonth < 1:
                expiryMonth = int(input("Invalid expiration month. Expiration month? "))

            cardDetails['cardNumber'] = cardNumber
            cardDetails['cvv'] = cvv
            cardDetails['expiry_day'] = expiryDay
            cardDetails['expiry_month'] = expiryMonth

    def saveBookingInformation():
        global bookingInfo
        os.system("cls")
        print('===== BOOKING INFORMATION =====\n')

        bookingName = input("\n\nPlease enter your first name: ")
        while not bookingName.isalpha():
            bookingName = input("Sorry, your name should not have numbers in it.\nPlease enter your first name: ")

        bookingSurname = input("Please enter your last name: ")
        while not bookingSurname.isalpha():
            bookingSurname = input("Sorry, your name should not have numbers in it.\nPlease enter your last name: ")

        bookingEmail = input("Please enter your email: ")
        while '@' not in bookingEmail or '.' not in bookingEmail:
            bookingEmail = input("Sorry, your email does not have the required characters '@' or '.'.\nPlease enter your email: ")

        bookingInfo['email'] = bookingEmail
        bookingInfo['first_name'] = bookingName
        bookingInfo['last_name'] = bookingSurname

    def printTicket(a, b, c, d, e):
        os.system('cls')
        global bookingInfo, cardDetails, amountOfPeopleCurrentlyInThemePark, payInCash
        fullName = string.capwords(bookingInfo['first_name'] + " " + bookingInfo['last_name'])

        if payInCash == True:
         print('=== Thank you for purchasing a ticket to our lovely attractions! ===\n')
         print(f"[PAYMENT METHOD] Paid in cash.\n")
         print(f"[BOOKING INFORMATION]:\n> Booking Name: {fullName}\n> Booking Email: {bookingInfo['email']}\n")
         print(f"[TICKETS PURCHASED]:\n> Number of Adult tickets: {a}\n> Number of Children tickets: {b}\n> Number of Senior tickets: {c}\n> Number of wristbands: {d}\n> Total amount of people: {e}")
        else:
         print('=== Thank you for purchasing a ticket to our lovely attractions! ===\n')
         print(f"[CARD DETAILS]:\n> Card Number: {cardDetails['cardNumber']}\n> CVV: {cardDetails['cvv']}\n> Expiry Day: {cardDetails['expiry_day']}\n> Expiry Month: {cardDetails['expiry_month']}\n")
         print(f"[BOOKING INFORMATION]:\n> Booking Name: {fullName}\n> Booking Email: {bookingInfo['email']}\n")
         print(f"[TICKETS PURCHASED]:\n> Number of Adult tickets: {a}\n> Number of Children tickets: {b}\n> Number of Senior tickets: {c}\n> Number of wristbands: {d}\n> Total amount of people: {e}")

        amountOfPeopleCurrentlyInThemePark += e

        input('Press {ENTER} to continue with the program.')


    def customerScreen():
     
     os.system('cls')

     if amountOfPeopleCurrentlyInThemePark < themepark['capacity']:
       print(f"There are currently {themepark['capacity'] - amountOfPeopleCurrentlyInThemePark} tickets.")
     else:
        print("Sorry, the theme park is at capacity.")
        exit()

     print(f"Here, you can find our current prices!\n[ADULT]: £{themepark['adult']}\n[CHILDREN]: £{themepark['child']}\n[SENIOR]: £{themepark['senior']}\n[WRISTBANDS]: £{themepark['wristband']}.\n")

     while True:
        try:
            numberOfAdults = int(input("How many adults (people over the age of 16) are going? "))
            break
        except ValueError:
            print("Sorry, that's an invalid request. Please enter a valid number.")

     while True:
        try:
            numberOfChildren = int(input("How many children (people under the age of 16) are going? "))
            break
        except ValueError:
            print("Sorry, that's an invalid request. Please enter a valid number.")

     while True:
        try:
            numberOfSeniors = int(input("How many seniors (people over the age of 50) are going? "))
            break
        except ValueError:
            print("Sorry, that's an invalid request. Please enter a valid number.")

     totalAmountOfPeopleGoing = numberOfAdults + numberOfChildren + numberOfSeniors

     if totalAmountOfPeopleGoing > themepark['capacity'] or themepark['capacity'] == 0:
        print("I'm sorry, unfortuantly there isn't enough tickets avaliable to service your request,\nplease come back again soon!")
        input()
        exit()

     while True:
        try:
            numberOfWristbands = int(input(f"How many wristbands would you like? (I recommend {totalAmountOfPeopleGoing} as that's how many people are going.) "))
            break
        except ValueError:
            print("Sorry, that's an invalid request.")

     while numberOfWristbands > totalAmountOfPeopleGoing:
        print("Sorry, that's more than the amount of tickets you've provided.")
        numberOfWristbands = int(input("How many wristbands would you like? "))

     print(f"The total cost comes to: £{calculateTotalPrice(numberOfAdults, numberOfChildren, numberOfSeniors, numberOfWristbands)}.")
     input('Press [ENTER] to continue.')

     saveBookingInformation()
     Payment()
     printTicket(numberOfAdults, numberOfChildren, numberOfSeniors, numberOfWristbands, totalAmountOfPeopleGoing)


    def adminPanel():
       os.system('cls')

       print("===== ADMIN PANEL =====\n")
       global adminLogin, isLockedOut, prices

       if isLockedOut == True:
          print("You can't be here, you're locked out.")
          input("Press {ENTER} to continue.")
          exit

       user = str(input("Admin username? "))
       password = str(input("Admin password? "))
       twofactorauth = int(input("2FA code? "))

       c = 0

       while user != adminLogin['user'] and password != adminLogin['pass'] and twofactorauth != adminLogin['2fa']:
             
             if c == 3:
                print("Sorry, you have been temporarily timed out due to 3 invalid attempts.")
                time.sleep(30)
             if c == 5:
                print("You've been locked out of the admin panel.")
                isLockedOut = True
                input('Press {ENTER} to continue.')
             print(f"You've typed either an invalid username, password, or 2FA code, you have {5 - c} attempt(s) left.")
             c = c + 1

             user = str(input("Admin username? "))
             password = str(input("Admin password? "))
             twofactorauth = int(input("2FA code? "))

       os.system('cls')

       print("===== MODIFICATION PANEL =====")

       while True:
            choice = str(input("\nWhat value would you like to modify? "))
            choice = choice.lower()

            if choice not in ['adult', 'child', 'wristband', 'senior', 'capacity']:
             print("Sorry, that's an invalid choice.")
            else:
             break
       
       while True:
          try:
             modifiedValue = int(input(f"What would you like to change the {choice} value to? "))
             oldValue = themepark[choice]
             themepark[choice] = modifiedValue
             print(f"You've successfully changed the {choice} prices to {modifiedValue} instead of {oldValue}.")
             input('\nPress {ENTER} to continue.')
             break
          except choice not in ['adult', 'child', 'wristband', 'senior', 'capacity'] or ValueError:
             print("Error, something went wrong.")

    def menu():
       
       global firstTimeLoggedOn

       os.system('cls')

       if firstTimeLoggedOn == True:
          firstTimeLoggedOn = False
          for x in range (1, 100):
             print(f"Starting up... [{x}%].\nmade by yusuf. (mini esp project.)")
             os.system('cls')
          input("Done! Press {ENTER} to continue!")

       os.system('cls')
       print("Welcome to Yusuf's amazing Themepark!")
       print("\n[Admin Controls]: 1\n[Purchase a Ticket]: 2")



       while True:
        try:
          choice = int(input("Choose with a number listed above: "))
          break
        except:
          print("Sorry, that's an invalid responce.")

       if choice == 2:
          customerScreen()
       elif choice == 1:
          adminPanel()

    while True:
       menu()

while True:
   main()

"""
###########################################################################################################################
###########################################################################################################################
"""