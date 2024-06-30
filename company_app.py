import streamlit as st
import json
import os

# Set page config to wide mode and dark theme
st.set_page_config(layout="wide", page_title="Company Product Search", page_icon="🔍")

# Custom CSS for dark theme and scrollable expander
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    .streamlit-expanderHeader {
        background-color: #262730;
        border: none !important;
    }
    .streamlit-expanderContent {
        background-color: #1E1E1E;
        border: 1px solid #4A4A4A;
        border-radius: 0 0 5px 5px;
        max-height: 300px;
        overflow-y: auto;
    }
    .streamlit-expanderContent::-webkit-scrollbar {
        width: 12px;
    }
    .streamlit-expanderContent::-webkit-scrollbar-track {
        background: #1E1E1E;
    }
    .streamlit-expanderContent::-webkit-scrollbar-thumb {
        background-color: #888;
        border-radius: 20px;
        border: 3px solid #1E1E1E;
    }
    .product-item {
        background-color: #2C2C2C;
        padding: 10px;
        margin: 5px 0;
        border-radius: 3px;
    }
    </style>
""", unsafe_allow_html=True)

# Set the title of the Streamlit app
st.title('Company Product Search')

# Load JSON data from file
json_file_path = 'company_product.json'  # Replace with your actual file path
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
else:
    st.error(f"JSON file not found"
             f" at {json_file_path}")
    st.stop()

# Add a text input for the company name
company_name = st.text_input('Enter company name:')

# Filter the DataFrame based on the input
company_names = list(data.keys())

if company_name:
    matching_companies = [company for company in company_names if company_name.lower() in company.lower()]

    if matching_companies:
        for company in matching_companies:
            with st.expander(company, expanded=True):
                for product in data[company]:
                    st.markdown(f"<div class='product-item'>{product}</div>", unsafe_allow_html=True)
    else:
        st.write('No products found for this company.')
else:
    st.write('Please enter a company name to search.')