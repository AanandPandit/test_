import streamlit as st

# Function to generate multiplication table
def multiplication_table(number, limit):
    table = []
    for i in range(1, limit + 1):
        table.append(f"{number} x {i} = {number * i}")
    return table

# Streamlit app with CSS
def main():
    st.title("Multiplication Table Generator")

    # CSS styles
    st.markdown(
        """
        <style>
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .generate-btn {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            display: block;
            margin: 20px auto;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input fields
    number = st.number_input("Enter a number:", min_value=1, value=1)
    limit = st.number_input("Enter limit:", min_value=1, value=10)

    # Generate button
    if st.button("Generate Table", class="generate-btn"):
        # Calculate table
        table = multiplication_table(number, int(limit))

        # Display table
        st.markdown("### Multiplication Table")
        for row in table:
            st.write(row)

if __name__ == "__main__":
    main()
