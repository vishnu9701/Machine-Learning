import streamlit as st
import sqlite3

# create a connection to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# create the users table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

def create_user(username, password):
    # check if user already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result:
        return False
    # create new user
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    return True

def login(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result:
        return True
    else:
        return False

def main():
    st.title("Login/Signup")

    # create a sidebar with links to the login and signup pages
    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login(username, password):
                st.success("Logged in as {}".format(username))
            else:
                st.error("Incorrect username or password")

    elif choice == "Sign Up":
        st.subheader("Create a new account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Sign Up"):
            if create_user(username, password):
                st.success("Account created")
            else:
                st.error("Username already exists")

if __name__ == '__main__':
    main()
