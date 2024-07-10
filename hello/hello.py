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

    # Generate button with class attribute
    if st.button("Generate Table", key="generate_btn", help="Click to generate table",):
        # Calculate table
        table = multiplication_table(number, int(limit))

        # Display table
        st.markdown("### Multiplication Table")
        for row in table:
            st.write(row)


if __name__ == "__main__":
    main()


#--------------------------------------------------------------------------------


# import streamlit as st
# from reportlab.pdfgen import canvas

# # Function to generate multiplication table
# def multiplication_table(number, limit):
#     table = []
#     for i in range(1, limit + 1):
#         table.append(f"{number} x {i} = {number * i}")
#     return table

# # Function to generate PDF
# def generate_pdf(number, limit, table):
#     buffer = io.BytesIO()
#     pdf = canvas.Canvas(buffer)
    
#     # Title
#     pdf.setFont("Helvetica-Bold", 18)
#     pdf.drawString(100, 750, "Multiplication Table")
    
#     # Content
#     pdf.setFont("Helvetica", 12)
#     y = 700
#     for row in table:
#         pdf.drawString(100, y, row)
#         y -= 20
    
#     pdf.showPage()
#     pdf.save()
#     buffer.seek(0)
    
#     return buffer

# # Streamlit app with PDF download
# def main():
#     st.title("Multiplication Table Generator")

#     # CSS styles (optional)
#     st.markdown(
#         """
#         <style>
#         h1 {
#             color: #2c3e50;
#             text-align: center;
#         }
#         .generate-btn {
#             background-color: #3498db;
#             color: white;
#             padding: 10px 20px;
#             font-size: 16px;
#             border-radius: 5px;
#             cursor: pointer;
#             display: block;
#             margin: 20px auto;
#             text-align: center;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # Input fields
#     number = st.number_input("Enter a number:", min_value=1, value=1)
#     limit = st.number_input("Enter limit:", min_value=1, value=10)

#     # Generate button with class attribute
#     if st.button("Generate Table", key="generate_btn", help="Click to generate table",):
#         # Calculate table
#         table = multiplication_table(number, int(limit))

#         # Display table
#         st.markdown("### Multiplication Table")
#         for row in table:
#             st.write(row)
        
#         # PDF download button
#         pdf_buffer = generate_pdf(number, int(limit), table)
#         st.download_button(
#             label="Download PDF",
#             data=pdf_buffer,
#             file_name="multiplication_table.pdf",
#             mime="application/pdf",
#         )

# if __name__ == "__main__":
#     main()
