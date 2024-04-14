from server_connection import Connection
from database_creation import Database_Creation
from registration import Registration
from login import Login
from users import User




# Creating instances of classes and calling methods
connection = Connection()
creation = Database_Creation()
register=Registration()
login=Login()
user=User()

# main function
def main():
    creation.create_database()
    creation.create_table_for_accounts()
    print("\n\t\tWelcome To Contact Book System.\n")
    while True:
        print("\t1.Register Yourself")
        print("\t2.Login To access system")
        print("\t3.Exit From system\n\n")
        # taking choice
        choice=input("Enter Your Desired Choice:").strip()
        # calling respectrice mehtods
        if choice=="1":
            register.registration_Process()
        elif choice=="2":
            user.main_page()
        elif choice=="3":
            print("Exiting From System..\n")
            creation.close_connection()
            return
        else:
            print("Invalid Choice.Please Select From Given Choice\n")

main()
# importing mysql connector and database password user from server details.py file