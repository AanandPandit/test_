import streamlit as st

def main():
    st.title('Addition of Two Numbers')
    
    # Input fields for two numbers
    num1 = st.number_input('Enter the first number:')
    num2 = st.number_input('Enter the second number:')
    
    # Add the numbers
    result = num1 + num2
    
    # Display the result
    st.write('The result of {} + {} = {}'.format(num1, num2, result))

if __name__ == '__main__':
    main()
