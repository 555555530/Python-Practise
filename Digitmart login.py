# Develop a Python script to validate the login functionality of the DigitMart/DigitKart application using both valid and invalid credentials. 
# After a successful login, verify that all mandatory modules are displayed and accessible.

URL = input("Enter a URL: ")
Username = input("Enter a Username: ")
Pass = input("Enter your Password: ")


if URL=="Digitmart.ai":
    print("Digitmart portal screen landed")
    
    if Username=="Dhiva" or "Dhivagar":
        print("User created:" ,Username)
        
        if Username=="":
            print("Please Enter a username")    
            
            if Pass=="1234" or "2345":
                print("You have Successfully Loggedin!")
                
                if Pass=="":
                    print("Please enter your Password")
                
            else:
                print("Invalid Password")                   
    
    else:
        print("Invalid Username")
else:
    print("Invalid URL")        

# if URL == "" or Username == "" or Pass == "":
#     print("Please enter all the credentials.")
    
# elif URL == "devdm.digitmart.ai" and Username == "Dhiva" and Pass == "1234":
#     print("You have Successfully Logged In.")
    
# else:
#     print("Invalid credentials.")     