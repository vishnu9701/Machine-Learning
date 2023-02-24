import streamlit as st
import mysql.connector
import pymysql
def create_table():
  
    conn = pymysql.connect(host='localhost',user='root',password='vedu',db='data')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name VARCHAR(255), age INT, email VARCHAR(255), address VARCHAR(255))''')
    conn.commit()
    conn.close()

def save_data_to_sql(name, age, email, address):
    conn = pymysql.connect(host='localhost',user='root',password='vedu',db='data')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age, email, address) VALUES (%s, %s, %s, %s)", (name, age, email, address))
    conn.commit()
    conn.close()

def main():
    create_table()
    st.title("Data Entry Form")
    name = st.text_input("Name")
    age = st.number_input("Age")
    email = st.text_input("Email")
    address = st.text_area("Address")
    if st.button("Save"):
        save_data_to_sql(name, age, email, address)
        st.success("Data saved to MySQL database.")

if __name__ == '__main__':
    main()
