atm_pin = 1234
pin_code = int(input("Kindly enter your ATM 4 digit pin: "))

if pin_code == atm_pin:
    print("Your balance is $1000")
else:
    print("Wrong credentials!!! Please try again")
