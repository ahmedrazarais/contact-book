# importing mysql connector and database password user from server details.py file
import mysql.connector
from login import Login




# making a class user and inherits with login
class User(Login):
    def __init__(self):
        self.user_table=""    # assign it as empty in initial
        super().__init__()

    
    # mehtod to craete table for user with hiws username
    def table_for_user(self):
        try:
            self.create_connection()
            self.cursor.execute(f"USE {self.database}")
            table_query=f"""CREATE TABLE IF NOT EXISTS {self.user_table}(
            id INT PRIMARY KEY,
            names VARCHAR (30),
            emails VARCHAR (50),
            numbers VARCHAR (50)
            )"""
            self.cursor.execute(table_query)
        except mysql.connector.Error as e:
            print(f"Error:{e}")


    # making a mehtod to retrieve data froimn user table
    def retrieve_data(self):
        try:
            self.create_connection()
            self.cursor.execute(f"USE {self.database}")
            self.cursor.execute(f"SELECT * FROM {self.user_table}")
            data=self.cursor.fetchall()
            return data
        except mysql.connector.Error as e:
            print(f"Error: {e}")

 
    # mehtod to take id (primary key) input
    def id_input(self):
        data=self.retrieve_data() # calling mehtod to get data list from table
        # taking id input
        while True:
            try:
                id_input=int(input("Enter Id to assign to employee (enter 0 to back):"))
                if id_input==0:   # if want to go back
                    print("Return To previous Options..\n")
                    return
                
                if id_input<=0:
                    print("Id Must not be zero or less than zero\n")

                # check id must not be repeated beacuse of primary key
                if data:
                    found = False
                    for row in data:
                        if id_input==row[0]:  # If id matches
                            found=True
                            break
                    if found:
                        print("Please Select another Id This id already exists.\n")
                    # if id not matches
                    else:
                        print("Id assign successfully\n")
                        return id_input
                # for initial when no data enter
                else:
                    print("Id assign successfully\n")
                    return id_input

            # if getting id rather than in number
            except ValueError:
                print("Please Enter In Digit Id must be in digit")
    
    # mehtod to take name input
    def get_valid_name(self):
        while True:
            name = input("Please enter your name (enter 0 to go back):").strip()
            
            if name == '0':
                return   # User wants to go back
            elif len(name) < 3:
                print("\nName must be at least 3 characters long.\n")
            elif not all(char.isalpha() or char.isspace() for char in name):
                print("\nName must contain only alphabets and space.\n")
            else:
                return name
    

    # mehtod to take gmail input
    def get_valid_gmail(self):
        while True:
            gmail = input("Enter Person's gmail (enter 0 to go back): ").strip()
            special_characters = '!#$%^&*()_+|}{":<?/,\';\\][=-]}'
            

            if gmail=="0":
                print("Going back To previous menu")
                return
            if gmail == '':
                print('\nRequired field cannot be left blank\n')
            elif gmail.startswith(' '):
                print('The entered gmail is not valid\n')
            elif not (6 < len(gmail) < 30):
                print('\nLength must be between 6 and 30 characters long\n')
            elif not gmail.endswith('@gmail.com'):
                print('\nMake sure @gmail.com must be at last\n')
            elif gmail.startswith('@gmail.com'):
                print('\nEnter valid Gmail\n')
            elif gmail.endswith('.@gmail.com'):
                print('\nSorry, the last character before @gmail.com must be a letter or number\n')
            elif any(char in special_characters for char in gmail):
                print('\nOnly letters and numbers are allowed\n')
            else:
                break

        return gmail
    

    def get_valid_phone_number(self):
        while True:
            phone_number = input("Enter your phone number (enetr 0 to back):").strip()
            if phone_number == '0':
                return   # User wants to go back
            elif not phone_number.isdigit():
                print("Phone number must contain only digits.\n")
            elif len(phone_number) != 11:
                print("Phone number must be 11 digits long.\n")
            else:
                return phone_number


    
    # make  amehtod to insert data in user table
    def insert_data_in_user_table(self,id,name,email,number):
        try:
            self.create_connection()
            self.cursor.execute(f"USE {self.database}")
            insert_query=f"INSERT INTO {self.user_table} (id,names,emails,numbers) VALUES (%s,%s,%s,%s)"
            self.cursor.execute(insert_query,(id,name,email,number))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error {e}")

    

    # mehtod to add process
    def add_person_details(self):
        id=self.id_input()
        if id:
            name=self.get_valid_name()
            if name:
                email=self.get_valid_gmail()
                if email:
                    number=self.get_valid_phone_number()
                    if number:
                        # after all input write in user table
                        self.insert_data_in_user_table(id,name,email,number)
                        print("Details Added Successfully.For More Details Go To View Details.\n")
                        return
                    else:
                        print("Number not recieve for further process\n")
                else:
                    print("Gmail not recieve for further process\n")
            else:
                print("Name not recieve for further process\n")
        else:
            print("Id not recieve for further process\n")

    # mehtod to diplay user cdsata
    def display_data_to_user(self):
        data=self.retrieve_data()
        if not data:
            print("There is no person's Details Added Yet! Your Contact Book Is empty\n\n")
            return
        else:
            print("\t\tContact-Book Details\n\n")
            print("Id\t\tName\t\tGmail\t\t\t\tNumber")
            print("------------------------------------------------------------------------------")
            for id,name,email,number in data:
                print(f"{id}\t\t{name}\t\t{email}\t\t{number}")
            print()
    


    # mehtod to delete any person'sdetails
    def delete_record_from_table(self):
        data=self.retrieve_data()
        if not data:
            print("There is no person's Details Added Yet! Your Contact Book Is empty,Can't Delete anything\n\n")
            return

        else:
            self.display_data_to_user()
            while True:
                try:
                    detail_id=int(input("Enter the id to delete record (enter 0 to back):"))
                    if detail_id==0:
                        print("Going back To Previous menu..\n")
                        return
                    found=False
                    for details in data:
                        if detail_id==details[0]:
                            print("Id Found.Wait for a second..\n")
                            found=True
                            break

                    if found:
                        try:
                            delete_query=f"DELETE FROM {self.user_table} WHERE id=%s "
                            self.cursor.execute(delete_query,(detail_id,))
                            self.connection.commit()
                            print(f"Person's Details Having {detail_id} has been deleted.\n")
                            return
                        except mysql.connector.Error as e:
                            print(f"Error as {e}")
                    else:
                        print("Invalid Id No Person having that id\n")

                except ValueError:
                    print("Please Enter In Digits\n")

     # mehtod for update details
    def update_data(self):
        data=self.retrieve_data() # calling mehtod to get data list from table
        # taking id input
        # check if data contains any value
        if data:
            self.display_data_to_user()
            print()
            while True:
                try:
                    row_id=int(input("Enter id of row you want to Update Its Details (enter 0 to back) :"))
                    if row_id==0:
                        print("Return to previous menu..")
                        return
                    # match with databse id
                    # Search for the row with the provided ID
                    found = False
                    for row in data:
                        if row_id==row[0]:  # If id matches
                            found=True
                            break
                    # if id found
                    if found:
                        print(f"Now what you update is update for employee with id {row_id}")
                        print("\t\tWelcome To update Details Area\n")
                        # When ifd found then display choices
                        while True:
                            print("\t1.Update Person's Name.")
                            print("\t2.Update Person's Gmail.")
                            print("\t3.Update Person's Number.")
                            print("\t4.Exit From Update Area\n.")
                        # taking input of choice in update area
                            update_choice=input("Enter Your Choice In Update area:").strip()
                            if update_choice=="1":
                                  name=self.get_valid_name()
                                  if name:
                                      self.cursor.execute(f"UPDATE {self.user_table} SET names=%s WHERE id=%s", (name,row_id))
                                      self.connection.commit()
                                      print("Upadte has been done successfully.\n")
                                      self.display_data_to_user()

                            elif update_choice=="2":
                                city=self.get_valid_gmail()
                                if city:
                                      self.cursor.execute(f"UPDATE {self.user_table} SET emails=%s WHERE id=%s", (city, row_id))
                                      self.connection.commit()
                                      print("Upadte has been done successfully.\n")
                                      self.display_data_to_user()
                            elif update_choice=="3":
                                subject=self.get_valid_phone_number()
                                if subject:
                                      self.cursor.execute(f"UPDATE {self.user_table} SET numbers=%s WHERE id=%s", (subject,row_id))
                                      self.connection.commit()
                                      print("Upadte has been done successfully.\n")
                                      self.display_data_to_user()

                            elif update_choice=="4":
                                print("Return from Update Area..\n")
                                return
                            else:
                                print("Invalid Choice.Please Select From Given Choices\n")

                    else:
                        print("Id Not Match.Please Enter Valid Id.\n")

                except ValueError:
                    print("Please Enter In Digits.\n")

        else:
           print("\nSorry!The database  is empty at this moment.Can't Update Anything rightnow!.\n")



    # mehtod to search for any specific user
    def search_aany_record(self):
        data=self.retrieve_data() # calling mehtod to get data list from table
        # taking id input
        # check if data contains any value
        if data:
            self.display_data_to_user()
            print()
            while True:
                try:
                    row_id=int(input("Enter id of row you want to See Its Details (enter 0 to back) :"))
                    if row_id==0:
                        print("Return to previous menu..")
                        return
                    # match with databse id
                    # Search for the row with the provided ID
                    found = False
                    for id,name,email,number in data:
                        if row_id==id:  # If id matches
                            found=True
                            break
                    # if id found
                    if found:
                        print(f"\nID : {id}")
                        print(f"Name : {name}")
                        print(f"Gmail : {email}")
                        print(f"Number : {number}\n")
                        return
                    else:
                        print("Invlid id no id found.please enter a valid id.\n")
         

                except ValueError:
                    print("Please Enter In Digits.\n")
        else:
            print("Sorry.Your Contact Book Is empty you can't search anything at this moment")

    # make a main page for users
    def main_page(self):
        # calling login mehtod from login class to take username from there and make a table in database with taht username for user
        username=self.details_to_check_for_login()
        self.user_table=username # assign usertable to username to make a table in database
        self.table_for_user()
        if username:
            print("\t\tWelcome To Contact Book App\n")
            while True:
                print("\t1.View All Contact Details.")
                print("\t2.Add Any Contact Details.")
                print("\t3.Delete Any Contact Details.")
                print("\t4.Update Any Contact Details.")
                print("\t5.Search Any Specific Contact Details.")
                print("\t6.Exit:exit from Contact Book Application.\n\n")
                # Taking user choice
                user_choice=input("Enter Your Choice In contact-book app:").strip()
                # calling respective mehtods on user choice
                if user_choice=="1":
                    self.display_data_to_user()
                elif user_choice=="2":
                    self.add_person_details()
                elif user_choice=="3":
                    self.delete_record_from_table()
                elif user_choice=="4":
                    self.update_data()
                elif user_choice=="5":
                    self.search_aany_record()
                elif user_choice=="6":
                    print("\ncontact Book Application Is Closed Now.")
                    print("See You Soon\n")
                    return
                else:
                    print("Invalid Choice.Please Enter Valid Choice.\n")
        else:
            print("\nTo Access The Cointact-Book Application.You Must log-in First\n")
            