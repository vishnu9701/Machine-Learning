import streamlit as st
import csv
        
def save_data_to_csv(data):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    st.title("Data Entry Form")
    name = st.text_input("Name")
    age = st.number_input("Age")
    email = st.text_input("Email")
    
    if st.button("Save"):
        data = [name, age, email]
        save_data_to_csv(data)
        st.success("Data saved to CSV file.")

if __name__ == '__main__':
    main()
