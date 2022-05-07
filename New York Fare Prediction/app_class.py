import joblib
import streamlit as st

regressionModel = joblib.load('regression.pkl')

def fare_generator(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):
       prediction = regressionModel.predict([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count]])
       
       output = prediction

       return output

def main():
    st.title ('New York Fair Prediction App')
    pickup_longitude = float(st.number_input('pick up longitude'))
    pickup_latitude = float(st.number_input('pick up latitude'))
    dropoff_longitude = float(st.number_input('dropoff longitude'))
    dropoff_latitude = float(st.number_input('dropoff latitude'))
    passenger_count = float(st.number_input('passenger count'))

    result = ''

    if st.button('predict'):
        result = fare_generator (pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count)
        st.success(f'The fair is {result}')

if __name__ == '__main__':
    main()

