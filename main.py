import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCFPALEVIiwvWSREvVdBOzNd1VeyqQWt9o")

# Load the text generation model
@st.cache(allow_output_mutation=True)
def load_text_model() -> genai.GenerativeModel:
    model = genai.GenerativeModel('gemini-pro')
    return model

# Define input prompt for hyperglycemia
input_prompt = """
               As an expert pharmacist specializing in toxicological effects, side effects, and drug-drug interactions, your task involves analyzing input text describing various drugs. Provide information on the potential toxicological effects, side effects, and interactions between the mentioned drugs. Consider the context of individuals with specific health conditions. If there are notable interactions, specify the recommendations or precautions to be taken. Use English and Arabic languages for the response.
               """

def generate_gemini_text_response(text_model, user_input):
    try:
        response = text_model.generate_content([input_prompt, user_input])
        return response.text
    except Exception as e:
        st.error(f"Error generating text response: {e}")
        return None

# Display header
st.set_page_config(
    page_title="ُEDA AI Chat",
    page_icon="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png",
    layout="wide",
)

st.markdown('''
<img src="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png" width="250" height="100">''', unsafe_allow_html=True)

st.markdown('''
Powered by Google AI <img src="https://seeklogo.com/images/G/google-ai-logo-996E85F6FD-seeklogo.com.png" width="20" height="20"> Streamlit <img src="https://global.discourse-cdn.com/business7/uploads/streamlit/original/2X/f/f0d0d26db1f2d99da8472951c60e5a1b782eb6fe.png" width="22" height="22"> Python <img src="https://i.ibb.co/wwCs096/nn-1-removebg-preview-removebg-preview.png" width="22" height="22">''', unsafe_allow_html=True)

# Load the text model
text_model = load_text_model()

# User input for the food description
user_input = st.text_area("Enter text describing a drug:")

# Generate response button
if st.button("Generate Response"):
    response = generate_gemini_text_response(text_model, user_input)
    st.text("Generated Response:")
    st.write(response)
