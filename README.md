# Contact Book System

The Contact Book System is a Python application that allows users to manage their contacts. It provides functionalities such as registration, login, adding, deleting, updating, and searching for contact details.

This project uses MySQL for the first time as a data storage solution.

Developed by Ahmed Raza.  
Contact: razarais28@gmail.com

## Features

- **Registration**: Users can register themselves by providing a unique username, a strong password, and a security question.
- **Login**: Registered users can log in to access the contact book functionalities.
- **Add Contact**: Users can add new contacts with details such as name, email, and phone number.
- **Delete Contact**: Users can delete existing contacts.
- **Update Contact**: Users can update the details of existing contacts.
- **Search Contact**: Users can search for specific contacts by their ID.
- **Security**: The system ensures secure storage of user credentials and contact details.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ahmedrazarais/contact-book.git
    ```

2. Navigate to the project directory:

    ```bash
    cd contact-book
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the database connection:
    - Update the `server_details.py` file with your MySQL database host, username, and password.

5. Run the application:

    ```bash
    python main.py
    ```

## Usage

1. **Registration**:
   - Choose the option to register.
   - Provide a unique username, a strong password, and a security question answer.

2. **Login**:
   - After registration, log in using your username and password.

3. **Contact Management**:
   - Once logged in, you can:
     - View all contact details.
     - Add a new contact.
     - Delete an existing contact.
     - Update contact details.
     - Search for a specific contact by ID.

4. **Exiting the System**:
   - Choose the option to exit the system when done.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
