from helpers import *
import streamlit as st

st.title('Calculator of two numbers')


st.title('calculator of two numbers')

#n1 = int(input("Enter first number"))
n1 = int(st.number_input("Enter first number"))
#n2 = int(input("Enter second number"))
n2 = int(st.number_input("Enter second number"))
st.write("Select the operation to do on the two numbers")

operator = st.selectbox("Operation",['Multiply','Add','Subtraction','Divide','Power','Floor division'])


if st.button("Show Result"):

    if operator == 'Multiply':
        st.write(multiply(n1,n2))
    elif operator == 'Add':
        st.write(add(n1,n2))
    elif operator == 'Divide':
        st.write(divide(n1,n2))
    elif operator == 'Subtraction':
        st.writerint(sub(n1,n2))
    elif operator == 'Power':
        st.write(power(n1,n2))
    elif operator == 'Floor division':
        st.write(floordivision(n1,n2))
    else:
        st.write("Please select valid option")



