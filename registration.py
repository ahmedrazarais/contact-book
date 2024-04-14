
# importing mysql connector and database password user from server details.py file

import mysql.connector
from database_creation import Database_Creation



# making a class for registration of users and inherits with database creation class
class Registration(Database_Creation):
    def __init__(self):
        super().__init__()



    # making a mehtod to fetch data from table
    def fetch_data_from_accounts_table(self):
        try:
            
            self.create_connection()
            self.cursor.execute(f"USE {self.database}")
            self.cursor.execute("SELECT * FROM accounts")
            data=self.cursor.fetchall()
            self.connection.commit()
            return data
        except mysql.connector.Error as e:
            print(f"Error : {e}")



    # mehtod to write data of user in accounts table
    def write_data_of_accounts(self,username,password,answer):
        try:
            self.create_connection()
            self.cursor.execute(f"USE {self.database}")
            query="INSERT INTO accounts (usernames,password,security) VALUES (%s,%s,%s)"
            self.cursor.execute(query,(username,password,answer))
            self.connection.commit()
            print("Congratulations Account Created successfully.\n")

        except mysql.connector.Error as e:
            print(f"Error: {e}")


    def get_username(self):
        contents = self.fetch_data_from_accounts_table()
        # calloing this mehtod to check that in account table no username duplication
        while True:
            username = input("Enter username for registration (enter 0 to go back): ")
            username_lower = username.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
            
            if username_lower == "0":
                print("Going back to previous menu...")
                return None
            
            if not username:
                print("Username cannot be empty.")
                continue
            
            if contents is None:

                print("No existing accounts found. Username is available.")
                print("Now proceed to enter password....")
                return username_lower
            
            # Check if username already exists
            username_exist = any(account[0] == username_lower for account in contents)
            
            if not username_exist:
                print("Username is available. Now proceed to enter password....\n")
                return username_lower
            else:
                print("Sorry, this username is already taken. Please choose another one or login.\n")


    # mehtoid to take password input
    def get_password(self):
        while True:
            password=input("Enter Strong Password For Registration (enter 0 to go back):")
            if password=="0":
                print("Going back To previous menu...\n")
                return
            # conditions for password.
            if len(password)>=6 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password ):
                print("Password Set successfully\n")
                return password    # if condition met then return the password 
                
            else:
                print("\nPassword must contain atleast 6 characters with mix of digitis alphabets.\n")
  
   
    # mehtod to take security answer input
    def security_question(self):
        while True:

            secutity_answer=input("What is favourite Food (enter 0 to back):")
            # if he want to go back
            if secutity_answer=="0":
                print("Going back To previous menu...\n")
                return
            # checking must be something in input
            if len(secutity_answer)<1:
                print("Answer is mandatory for security purpose:\n")
            else:
                print("security answer set successfully!...wait for a second\n")
                return secutity_answer
            
    # mehtod for registration process

    def registration_Process(self):
        # calling all mehtodsa of registaration and checking whether get input or not
        username=self.get_username()
        if username:
            password=self.get_password()
            if password:
                answer=self.security_question()
                if answer:
                 # after getting all valid input write user data in table
                  
                   self.write_data_of_accounts(username,password,answer)
                    
                else:
                    print("Security answer not recieved yet!!\n")

            else:
                print("Password not set yet!\n")
        else:
            print("Username not set yet!\n")