from helpers import *
import streamlit as st

st.title('Calculator of two numbers')


st.title('calculator of two numbers')

#n1 = int(input("Enter first number"))
n1 = int(st.number_input("Enter first number"))
#n2 = int(input("Enter second number"))
n2 = int(st.number_input("Enter second number"))
st.write("Select the operation to do on the two numbers")
st.write("Type 1 - Multiplication")
st.write("Type 2 - Addition")
st.write("Type 3 - Divide")
st.write("Type 4 - subtraction")
st.write("Type 5 - power/exponential")
#operator = int(input("Enter the option from above"))
operator = int(st.number_input("Enter the option from above"))

if operator == 1:
    st.write(multiply(n1,n2))
elif operator == 2:
    st.write(add(n1,n2))
elif operator == 3:
    st.write(divide(n1,n2))
elif operator == 4:
    st.writerint(sub(n1,n2))
elif operator == 5:
    st.write(power(n1,n2))
elif operator == 6:
    st.write(floordivision(n1,n2))
else:
    st.write("Please select valid option")



