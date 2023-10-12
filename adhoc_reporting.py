import streamlit as st
import os

# Streamlit UI
st.title('SMFG Reporting App')

# Get the username from user input
username = st.text_input('Username', key='username')

# User input fields
with st.container():
    col1, col2 = st.columns(2)  # Create two columns

    from_date = col1.date_input('From Date', key='from_date')
    to_date = col2.date_input('To Date', key='to_date')
    
    customer_id = col1.text_input('Customer ID (comma-separated)', key='customer_id')
    batch_id = col2.text_input('Batch ID (comma-separated)', key='batch_id')

    app_ref_no = col1.text_input('App Ref No (comma-separated)', key='app_ref_no')
    lead_id = col2.text_input('Lead ID (comma-separated)', key='lead_id')

    gl_codes = col1.text_input('GL Code (comma-separated)', key='gl_codes')
    lan = col2.text_input('LAN (comma-separated)', key='lan')

# Report selection dropdown
reports = st.selectbox('Select a report', ['Report 1', 'Report 2', 'Report 3'])

# Submit button
if st.button('Submit'):
    if not username:
        st.error('Username cannot be empty. Please enter your username.')
    else:
        # Define the folder path
        local_folder = r'D:\\PQIS'
        
        # Ensure the folder exists or create it
        os.makedirs(local_folder, exist_ok=True)
        
        # Create a unique filename based on the username and report
        file_name = f"{username}_{reports.replace(' ', '_')}.txt"

        st.success(f"file : {file_name} ")
        # Define the full file path
        file_path = os.path.join(local_folder, file_name)
        st.write(f"File Path: {file_path.replace('/', '\\')}")
        
        # Write the user inputs to the file
        with open(file_path, 'w') as file:
            file.write(f"Username: {username}\n")
            file.write(f"Report: {reports}\n")
            file.write(f"From Date: {from_date}\n")
            file.write(f"To Date: {to_date}\n")
            file.write(f"Customer ID: {customer_id}\n")
            file.write(f"Batch ID: {batch_id}\n")
            file.write(f"App Ref No: {app_ref_no}\n")
            file.write(f"Lead ID: {lead_id}\n")
            file.write(f"GL Codes: {gl_codes}\n")
            file.write(f"LAN: {lan}\n")

        st.success(f'User inputs have been saved to: {file_path}')
