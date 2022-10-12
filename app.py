import streamlit as st
import joblib

model = joblib.load('spam-ham')   # we are loading the pipelined model using joblib
st.title('SPAM-HAM CLASSIFIER')  # it crates a title in webapp
ip = st.text_input('Enter the message') #it creates a textbox in the webapp
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])  # st.buttton will cfeate a buttton with the name predict
  # st.title(op[0]) # the 0th element in op variable is displayed as a title

  
  
  
  
