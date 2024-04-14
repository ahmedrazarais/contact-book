# importing mysql connector and database password user from server details.py file
import mysql.connector
from registration import Registration



# class for login procedure inherits with rergistration
class Login(Registration):
    def __init__(self):
        super().__init__()




    # write a mehtod for update password
    def update_password(self,username,new_password,answer):
        try:
            self.create_connection()
            self.cursor.execute(f"USE {self.database}")
            query = "UPDATE accounts SET password=%s WHERE usernames=%s AND security=%s"
            self.cursor.execute(query, (new_password, username, answer))
            self.connection.commit()
            print("Password updated successfully")

        except mysql.connector.Error as e:
            print(f"Error : {e}")











    # taking username input for check in table
    def details_to_check_for_login(self):
        # calling fetch data mehtod from registartion class to matchg account details
        data=self.fetch_data_from_accounts_table()
        found=False
        while True:
            username=input("Enter username for login (enter 0 to go back):").strip()
            if username=="0":
                return
            for user,pswd,ans in data:
                if user==username:
                    print("username found ")
                    found=True
                    break
                else:
                    print("Invalid username.please enter valid username\n")
            if found:
                while True:
                    password=input("Enter password for login (enter 0 to go back):").strip()
                    if password=="0":
                        return
                    
                    if pswd==password:
                            print("wait a minute...Login successfull\n")
                            return username
                    else:
                        print("Invalid password\n")
                        while True:
                            forgot=input("Are You Forgot password (Y/N):").strip().upper()
                            if forgot not in ["Y","N"]:
                                    print("\nPlease Enter correct word.\n")
                            elif forgot=="N":
                                    break
                            else:
                                print("Answer Security question and access to change password ")
                                answer=input("What is your favourite food?:").strip()
                                if ans==answer:
                                    print("Now you can reset password")
                                    new_password=self.get_password()
                                    if new_password:
                                        self.update_password(username, new_password, answer)
                                        return username
                                    else:
                                        print("Back to main menu..\n")
                                        return
                                    
                                else:
                                    print("Wrong answer.Access Denied..\n")
                                    break

