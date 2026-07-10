# Develop a Python script for the User Management module that performs the following operations:
# Create a new role
# Create a new user
# Assign the created role to the user
# Configure and enable the required permissions for the user


role = input("Enter Role Name: ")

if role == "Admin":
    print("Role Created")

    user = input("Enter User Name: ")

    if user == "Dhiva":
        print("User Created")

        assign = input("Assign Role (yes/no): ")

        if assign == "yes":
            print("Role Assigned")

            permission = input("Enable Permission (yes/no): ")

            if permission == "yes":
                Permission_Enabled={"Dashboad Access":"Enabled",
                                   "Content":"Enabled",
                                   "Transaction browser":"Enabled"}
                
                print("Permission Enabled", Permission_Enabled)
            else:
                print("Permission Not Enabled")

        else:
            print("Role Not Assigned")

    else:
        print("Invalid User")

else:
    print("Invalid Role")   
    