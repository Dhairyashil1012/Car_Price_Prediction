import streamlit as st
import pickle

with open ("Car_Price.pkl","rb") as file:
    model = pickle.load(file)

st.title("Car Price Prediction !")

def get_value(key,dict):
    for key in dict:
        return dict[key]

st .write("2014,145500,Diesel,Individual,Manual,First Owner,23.40,74.00,5.0 :- Actual Price = 450000")

Fuel_Mapping = {'Diesel':0, 'Petrol':1, 'LPG':2, 'CNG':3}
Seller_Mapping = {'Individual':0, 'Dealer':1, 'Trustmark Dealer':2}
Transmission_Mapping = {'Manual':0, 'Automatic':1}
Owner_Mapping = {'First Owner':0, 'Second Owner':1, 'Third Owner':2,'Fourth & Above Owner':3, 'Test Drive Car':4}

Year = st.number_input('Year',0,4000)
KM_Driven = st.number_input("KM Driven",0,400000)

Fuel = st.selectbox("Select Fuel", options=list(Fuel_Mapping.keys()))
Fuel = get_value(Fuel,Fuel_Mapping)

Seller_Type = st.selectbox("Select Seller", options=list(Seller_Mapping.keys()))
Seller_Type = get_value(Seller_Type,Seller_Mapping)

Transmission = st.selectbox("Transmission", options=list(Transmission_Mapping.keys()))
Transmission = get_value(Transmission,Transmission_Mapping)

Owner = st.selectbox("Owner", options=list(Owner_Mapping.keys()))
Owner = get_value(Owner,Owner_Mapping)

Mileage = st.number_input("Mileage kmpl/kg")
Power = st.number_input("Max_Power bhp")
Seats = st.number_input("Seats",0,10)

Input_Data = [[Year,KM_Driven,Fuel,Seller_Type,Transmission,Owner,Mileage,Power,Seats]]

if st.button("Car Price Predict"):
    Prediction = model.predict(Input_Data)

    # Display prediction
    st.write(f'The Predicted Price is: INR  {Prediction[0]:,.2f}')