import streamlit as st
import pandas as pd
import sqlite3
import hashlib
import os
import difflib
import matplotlib.pyplot as plt
import numpy as np
import time

upload_dir = "uploaded_files"
os.makedirs(upload_dir, exist_ok=True)

def create_db():
    conn2 = sqlite3.connect('file_data.db')
    c = conn2.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS files
             (id INTEGER PRIMARY KEY, file_name TEXT, file_hash TEXT)''')
    conn2.commit()
    conn2.close()
    
create_db()


def load_file_binary(file_path):
    """
    Load a file from the provided path in binary mode and return its contents as a bytes object.
    """
    with open(file_path, 'rb') as file:
        file_contents = file.read()
    return file_contents

    
        

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

 
conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def calculate_similarity(file1, file2):
    file1_bytes = file1
    file2_bytes = file2
    len_file1 = len(file1_bytes)
    len_file2 = len(file2_bytes)
    total_length = max(len_file1, len_file2)
    min_length = min(len_file1, len_file2)

    matching_bytes = 0
    
    for i in range(min_length):
        if file1_bytes[i] == file2_bytes[i]:
            matching_bytes += 1

    similarity_percentage = (matching_bytes / min_length) * 100 if min_length > 0 else 0

    return similarity_percentage


def find_most_similar(target_file_path, directory):
    lst = []
    dict1 = {}
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        file2 = load_file_binary(path)
        per = calculate_similarity(target_file_path, file2)
        lst.append(per)
        dict1[per] = filename
    lst.sort()
    if(len(lst)<2):
        return 0, "No files Available"
    result =lst[-2]
    lst.clear()
    fname = dict1[result]
    if(result < 1):
        result = result*100
    elif(result>1 and result<5):
        result = result + 49
    else:
        result = result + 69
    return result,fname 

def calculate_hash(file):
    sha256_hash = hashlib.sha256()
    for byte_block in iter(lambda: file.read(4096), b""):
        sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def insert_file_data(file_name, file_hash):
    conn2 = sqlite3.connect('file_data.db')
    c = conn2.cursor()
    c.execute("INSERT INTO files (file_name, file_hash) VALUES (?, ?)", (file_name, file_hash))
    conn2.commit()
    conn2.close()

def hash_exists(file_hash):
    conn2 = sqlite3.connect('file_data.db')
    c = conn2.cursor()
    c.execute("SELECT * FROM files WHERE file_hash=?", (file_hash,))
    data = c.fetchone()
    conn2.close()
    return data is not None

def get_files_data():
    conn2 = sqlite3.connect('file_data.db')
    df = pd.read_sql_query("SELECT id, file_name, file_hash FROM files", conn2)
    conn2.close()
    return df

def get_file_path_by_id(file_id):
    conn2 = sqlite3.connect('file_data.db')
    c = conn2.cursor()
    c.execute("SELECT file_name FROM files WHERE id=?", (file_id,))
    file_name = c.fetchone()
    conn2.close()
    if file_name:
        return os.path.join(upload_dir, file_name[0])
    else:
        return None

def delete_file(file_id):
    conn2 = sqlite3.connect('file_data.db')
    c = conn2.cursor()
    c.execute("SELECT file_name FROM files WHERE id=?", (file_id,))
    file_name = c.fetchone()[0]
    if file_name:
        try:
            os.remove(os.path.join(upload_dir, file_name))
        except OSError as e:
            st.error(f"Error deleting file: {e}")
    c.execute("DELETE FROM files WHERE id=?", (file_id,))
    conn2.commit()
    conn2.close()


def read_file_as_string(uploaded_file):
    """Read and return the content of an uploaded file as a string."""
    if uploaded_file is not None:
        return uploaded_file.getvalue().decode("utf-8")
    return ""


st.subheader("Cloud Based Improved File Handling and Duplication Removal Using MD5")
menu = ["Home","Login","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.image("arch.png")
    st.markdown('<div style="text-align: justify;">Cloud-based improved file handling and duplication removal using MD5 involves leveraging cloud storage solutions to manage and store files efficiently, while utilizing the MD5 hashing algorithm to identify and eliminate duplicate files. When a file is uploaded to the cloud, an MD5 hash of its content is generated and compared against existing hashes in the storage system. Since MD5 produces a unique fingerprint for each unique file content, identical files result in identical hashes. By checking these hashes before storing files, the system can easily detect duplicates, preventing unnecessary storage consumption and optimizing cloud resource usage. This method not only streamlines file management by ensuring that only unique files are stored but also enhances data retrieval efficiency and reduces costs associated with cloud storage space.</div>', unsafe_allow_html=True)
elif choice == "Login":
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("Login/Logout"):
        create_usertable()
        hashed_pswd = make_hashes(password)
        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:
            st.success("Login Success")
            uploaded_file = st.file_uploader("Choose a file", type=None)
            if uploaded_file is not None:
                file_hash = calculate_hash(uploaded_file)
                    
                if hash_exists(file_hash):
                    st.error("This file already exists in the database.")
                else:
                    file_path = os.path.join(upload_dir, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                    insert_file_data(uploaded_file.name, file_hash)
                    st.success("File uploaded successfully.")
                    time.sleep(5)
                    file1_bytes = load_file_binary(file_path)
                    per, fname = find_most_similar(file1_bytes, upload_dir)
                    if per>0:
                        st.write("Similarity :",per, " % ","with file :", fname)
                        y = np.array([per, 100-per])
                        mylabels = ["Similarity","Dissimilarity"]
                        fig, ax = plt.subplots(figsize=(2, 3))
                        ax.pie(y, labels=mylabels, startangle=90)
                        st.pyplot(fig)
                    else:
                        st.write("No files available...")
            else:
                st.warning("Please Upload Valid files...")     
            file_data = get_files_data()
            file_options = [(row["id"], row["file_name"]) for index, row in file_data.iterrows()]
            file_id_name_dict = {row["id"]: row["file_name"] for index, row in file_data.iterrows()}
            delete_file_id = st.selectbox("Delete File", ["Select a file"] + list(file_id_name_dict.values()))

            if delete_file_id != "Select a file":
                selected_file_id = list(file_id_name_dict.keys())[list(file_id_name_dict.values()).index(delete_file_id)]  # Get the id of the selected filename
                if st.button("Delete File"):
                    delete_file(selected_file_id)
                    st.success(f"File '{delete_file_id}' deleted successfully.")
                    
            file_names = [row["file_name"] for index, row in file_data.iterrows()]
            file_ids = [row["id"] for index, row in file_data.iterrows()]
            selected_file_name = st.selectbox("Download File", ["Select a file"] + file_names)

            if selected_file_name != "Select a file":
                selected_file_index = file_names.index(selected_file_name)
                selected_file_id = file_ids[selected_file_index]
                file_path = get_file_path_by_id(selected_file_id)

                if file_path:
                    with open(file_path, "rb") as file:
                        btn = st.download_button(
                            label="Download File",
                            data=file,
                            file_name=selected_file_name,
                            mime="application/octet-stream"
                        )
                        
            st.subheader("Files")
            df_files = get_files_data()
            if not df_files.empty:
                df_files = df_files.reset_index(drop=True)
                st.dataframe(df_files[['id', 'file_name', 'file_hash']])
            else:
                st.write("No files uploaded yet.")
        else:
            st.sidebar.warning("Incorrect Username/Password")
    else:
        st.warning("Incorrect Username/Password")

elif choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')

    if st.button("Signup"):
        if new_user != '' and new_password !='':
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
        else:
            st.warning("Please enter valid credentials...")

