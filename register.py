import streamlit as st
st.set_page_config(
     page_title='Ayushmithra Register',
     layout="centered"
)
def cs_body():
    st.title("Welcome to Ayushmithra")
    st.header("Create Your Account with Ayushmithra")
    print()
    a,b, = st.columns(2)
#Form Starts
    with st.form(key='submit'):
        a,b=st.columns(2)
        a.text_input("Name*")
        a.text_input("Phone Number*")
        a.text_input("Address (For Contact Purpose alone)*")
        a.file_uploader("Aadhar Card (Must be in PDF Format)*")
        a.file_uploader("Passport Size Photo (Must be Clear)*")
        
        a.camera_input("Your Live Pic*")


        
        b.text_input('Username*')
        b.text_input('Password*')
        b.text_input("Re-Type Password*")
        b.file_uploader("College ID Card (Must be in PDF Format)*")
        b.file_uploader("Your Signature (Must be in JPG File)*")
        b.date_input("Date of Birth*")
        b.date_input("Year of Passed out*")
        
        

        b.markdown("I Declare here by all the given informations are True and Original")
        st.form_submit_button('Create Account with Ayushmithra')  
# Form Ends
cs_body()