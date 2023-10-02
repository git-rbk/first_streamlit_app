import streamlit as st
import pyodbc

# Database connection setup
#conn = pyodbc.connect(
#    'DRIVER={ODBC Driver 17 for SQL Server};'
#    'SERVER=LocalHost;'
#    'DATABASE=LMS;'
#    'UID=service_account;'
#    'PWD=pwd;'
#)

#cursor = conn.cursor()

# Streamlit UI
st.title('Adhoc Reporting App')

# User input fields
from_date = st.date_input('From Date', key='from_date')
to_date = st.date_input('To Date', key='to_date')
gl_codes = st.text_input('GL Code (comma-separated)', key='gl_codes')
lan = st.text_input('LAN (comma-separated)', key='lan')
customer_id = st.text_input('Customer ID (comma-separated)', key='customer_id')
batch_id = st.text_input('Batch ID (comma-separated)', key='batch_id')
app_ref_no = st.text_input('App Ref No (comma-separated)', key='app_ref_no')
lead_id = st.text_input('Lead ID (comma-separated)', key='lead_id')

# Report selection dropdown
reports = st.selectbox('Select a report', ['Report 1', 'Report 2', 'Report 3'])

# Submit button
if st.button('Submit'):
    username = st.session_state.username  # Set username (you should set this value as needed)
    st.write(f"Hello, {username}! Your {reports} will be placed in the shared folder in a few hours. Kindly wait. Thank you!")
    # Store user parameters in the database
    # cursor.execute('''
    #    INSERT INTO adhoc_reporting_parameters
    #    (from_date, to_date, gl_codes, lan, customer_id, batch_id, app_ref_no, lead_id, report_name)
    #    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    #''', (from_date, to_date, gl_codes, lan, customer_id, batch_id, app_ref_no, lead_id, reports))
    
    #conn.commit()

    # Display a confirmation message
    #st.success(f'Hello, {st.session_state.username}! Your {reports} will be placed in the shared folder in a few hours. Kindly wait. Thank you!')

# Close the database connection
#conn.close()
