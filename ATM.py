# Develop a Python program that simulates an ATM system with the following functionalities:
# Change the ATM PIN
# Check the account balance
# Display the transaction history
# User Login (Account Number + PIN Authentication)


ATM_PIN = input("Enter your PIN: ")

# Customer Details
if ATM_PIN == "123":
    a = {
        "Name": "Dhivagar",
        "Age": "29",
        "Account Number": "76545676566567655"
    }
    print(a)

# Change PIN
elif ATM_PIN == "1234":
    print("Please change your PIN")
    new_pin = input("Enter a New PIN: ")
    ATM_PIN = new_pin
    print("Your new PIN is:", ATM_PIN)

# Invalid PIN
else:
    print("Invalid PIN")
        