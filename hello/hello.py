import streamlit as st

# CSS styles
css = """
<style>
    .title {
        color: #2e4053;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .input-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        background-color: #f5f5f5;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
    }
    .input-label {
        font-size: 1.2em;
        color: #34495e;
        margin-bottom: 10px;
    }
    .btn {
        display: block;
        width: 100%;
        padding: 10px;
        margin-top: 20px;
        font-size: 1.2em;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn:hover {
        background-color: #2980b9;
    }
    .result-container {
        max-width: 400px;
        margin: 20px auto;
        padding: 20px;
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        background-color: #ffffff;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
    }
    .result {
        font-size: 1.1em;
        color: #34495e;
        margin-bottom: 5px;
    }
</style>
"""

def multiplication_table(num):
    table = []
    for i in range(1, 11):
        table.append(f"{num} x {i} = {num * i}")
    return table

def main():
    st.markdown(css, unsafe_allow_html=True)  # Inject CSS
    st.markdown('<h1 class="title">Multiplication Table Generator</h1>', unsafe_allow_html=True)
    
    # Input container
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label class="input-label">Enter a number:</label>', unsafe_allow_html=True)
    number = st.number_input('', min_value=1, max_value=100, step=1, format="%d")
    
    # Button to generate table
    if st.button('Generate Table', class_='btn'):
        st.markdown('</div>', unsafe_allow_html=True)  # Close input container
        # Result container
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        # Display the multiplication table
        table = multiplication_table(number)
        for row in table:
            st.markdown(f'<p class="result">{row}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)  # Close result container

if __name__ == '__main__':
    main()
