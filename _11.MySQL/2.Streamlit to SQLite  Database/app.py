import streamlit as st
import sqlite3

def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name TEXT, age INTEGER, email TEXT)''')
    conn.commit()
    conn.close()

def save_data_to_sql(name, age, email, address):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    conn.close()

def main():
    create_table()
    st.title("Data Entry Form")
    name = st.text_input("Name")
    age = st.number_input("Age")
    email = st.text_input("Email")
  
    if st.button("Save"):
        save_data_to_sql(name, age, email)
        st.success("Data saved to SQLite database.")

if __name__ == '__main__':
    main()
