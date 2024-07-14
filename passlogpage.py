import streamlit as st
import mysql.connectorimport streamlit as st
import mysql.connector
from mysql.connector import Error
import re

# Define your CSS style


# Function to get database connection
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Replace with your MySQL host
            user='root',       # Replace with your MySQL username
            password='Montu@030906',   # Replace with your MySQL password
            database='logd'           # Replace with your database name
        )
        if connection.is_connected():
            st.success("You are connected to our Community")
    except Error as e:
        st.error(f"Error connecting to MySQL Platform: {e}")
    return connection

# Function to validate password
def is_valid_password(password):
    # Validate length and special character
    if len(password) < 8:
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Function to add a new user
def add_user(username, password):
    try:
        connection = get_db_connection()
        if connection is None:
            st.error("Failed to connect to the database")
            return

        # Validate password
        if not is_valid_password(password):
            st.error("Password must be at least 8 characters long and contain at least one special character.")
            return

        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        st.success("Account created successfully!")
        st.info("Go to the Login page to log in")
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if connection is not None and connection.is_connected():
            connection.close()

# Function to authenticate user
def authenticate_user(username, password):
    try:
        connection = get_db_connection()
        if connection is None:
            st.error("Failed to connect to the database")
            return None
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        return user
    except Error as e:
        st.error(f"Error: {e}")
        return None
    finally:
        if connection is not None and connection.is_connected():
            connection.close()

def main():
    menu = ["Home", "Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.header("WELCOME")
    elif choice == "Login":
        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            user = authenticate_user(username, password)
            if user:
                st.success(f"Welcome {username}!")
            else:
                st.error("Invalid username or password")
    elif choice == "Register":
        st.subheader("Create a New Account")

        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')

        if st.button("Register"):
            if new_username and new_password:
                add_user(new_username, new_password)
            else:
                st.error("Please fill out both fields")

if __name__ == '__main__':
    main()

from mysql.connector import Error
import re

# Define your CSS style


# Function to get database connection
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Replace with your MySQL host
            user='root',       # Replace with your MySQL username
            password='Montu@030906',   # Replace with your MySQL password
            database='logd'           # Replace with your database name
        )
        if connection.is_connected():
            st.success("You are connected to our Community")
    except Error as e:
        st.error(f"Error connecting to MySQL Platform: {e}")
    return connection

# Function to validate password
def is_valid_password(password):
    # Validate length and special character
    if len(password) < 8:
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

# Function to add a new user
def add_user(username, password):
    try:
        connection = get_db_connection()
        if connection is None:
            st.error("Failed to connect to the database")
            return

        # Validate password
        if not is_valid_password(password):
            st.error("Password must be at least 8 characters long and contain at least one special character.")
            return

        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        st.success("Account created successfully!")
        st.info("Go to the Login page to log in")
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if connection is not None and connection.is_connected():
            connection.close()

# Function to authenticate user
def authenticate_user(username, password):
    try:
        connection = get_db_connection()
        if connection is None:
            st.error("Failed to connect to the database")
            return None
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        return user
    except Error as e:
        st.error(f"Error: {e}")
        return None
    finally:
        if connection is not None and connection.is_connected():
            connection.close()

def main():
    menu = ["Home", "Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.header("WELCOME")
    elif choice == "Login":
        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            user = authenticate_user(username, password)
            if user:
                st.success(f"Welcome {username}!")
            else:
                st.error("Invalid username or password")
    elif choice == "Register":
        st.subheader("Create a New Account")

        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')

        if st.button("Register"):
            if new_username and new_password:
                add_user(new_username, new_password)
            else:
                st.error("Please fill out both fields")

if __name__ == '__main__':
    main()
