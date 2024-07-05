import streamlit as st

def multiplication_table(num):
    table = []
    for i in range(1, 11):
        table.append(f"{num} x {i} = {num * i}")
    return table

def main():
    st.title('Multiplication Table Generator')
    
    # Input field for number
    number = st.number_input('Enter a number:', min_value=1, max_value=100, step=1)
    
    # Button to generate table
    if st.button('Generate Table'):
        # Display the multiplication table
        table = multiplication_table(number)
        for row in table:
            st.write(row)

if __name__ == '__main__':
    main()
