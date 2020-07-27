import numpy as np 
import pandas as pd 
import streamlit as st
import pickle
import sqlite3
from app import *



random_forest=pickle.load(open('main_filexx','rb'),encoding='utf-8')
filess=pickle.load(open('main_filexx','rb'),encoding='utf-8')

# Creating Database
conn=sqlite3.connect("authentication.db")
connect=conn.cursor()
def table():
	connect.execute('CREATE TABLE IF NOT EXISTS AUTHENTICATION(username TEXT,password TEXT)')
def user_data(username,password):
	connect.execute('INSERT INTO AUTHENTICATION(username,password) VALUES (?,?)',(username,password))
	conn.commit()
def user_info(username,password):
	connect.execute('SELECT * FROM AUTHENTICATION WHERE username =? AND password = ?',(username,password))
	data = connect.fetchall()
	return data


#Signup and Signin Page

def security():
    st.title("First you have to sign up and then Signin.")
    options=['About','Sign Up','Login']
    choice=st.sidebar.selectbox("Options",options)
    if choice=="Sign Up":
        st.subheader("SignUp ")
        username=st.text_input("Create New account ")
        Password=st.text_input("Enter your password",type='password')
        if st.button("Submit"):
            table()
            user_data(username,Password)
            st.success("Submitted . Now you can go for Log in option ")
    elif choice=="Login":
        st.subheader("Login Page")
        enter_username=st.text_input("Enter the Username")
        enter_password=st.text_input("Enter the password",type='password')
        if st.button("Submit"):
            table()
            information=user_info(enter_username,enter_password)
            if information:
                st
                open_ml()
            else:
                st.warning("Incorrect password or username.")
    elif choice =='About':
        st.header("You have to follow steps by step. ")
        st.header("Step 1.First you have to go signup option.")
        st.header("Step 2.Second go to sign in page and type the same information as you submit in Sign up page")
        st.header("After succesfully sign in . you can do your predictions.")     


def open_ml():
    choice=st.sidebar.radio("Algorithms",("Random Forest","Linear Regression"))
    bedrooms=st.text_input('No of bedreeoms ')
    bathrooms=st.text_input('No of bathrooms')
    sqft_living=st.text_input("Living room Area ")
    sqft_lot=st.text_input("Area of lot ")
    floors=st.text_input("Number of floors")
    waterfront=st.selectbox("Water view ",["Yes","No"])
    if waterfront=="Yes":
        waterfront=1
    else:
        waterfront=0
    condition=st.selectbox(" Rating" , [1, 2,3,4,5])
    sqft_above=st.text_input('sqft_aboves')
    yr_built=st.text_input('In which year was bulid ?  ')
    lat=st.text_input('lat')
    sqft_living15=st.text_input('living root square foot ')
    sqft_lot15=st.text_input('Lot Square Foot ')

    if st.button("Price"):
        prediction=predicting_price(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,sqft_above,yr_built,lat,sqft_living15,sqft_lot15)
        st.success("The house prics is {}".format(np.round(prediction),2))
    if st.button("About"):
        st.write("Made By Harsh")
        st.write("Credit goes to Krish Sir ")
    parameters=[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,sqft_above,yr_built,lat,sqft_living15,sqft_lot15]
    
            
def predicting_price(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,sqft_above,yr_built,lat,sqft_living15,sqft_lot15):
    parameters=[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,sqft_above,yr_built,lat,sqft_living15,sqft_lot15]
    if choice=="Random Forest":
        house_price=random_forest.predict([parameters])
        print(house_price)
    elif choice=="XGBoost":
        house_price=xg_boos.predict([[parameters]])
        print(house_price)
    elif choice=="Linear Regression":
        house_price=linear.predict([parameters])
    return house_price

            

if __name__=='__main__':
    security()
   



 