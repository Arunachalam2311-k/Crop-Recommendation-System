# Import libraries
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import os

# Set page configuration
st.set_page_config(page_title="Crop Recommendation", page_icon=":corn:", layout="wide")


# Load model and scalers
try:
    working_dir = os.path.dirname(os.path.abspath(__file__))
    minmax = pickle.load(open(r'D:\New folder (4)\minmaxscaler.pkl', 'rb'))
    standard = pickle.load(open(r'D:\New folder (4)\standscaler.pkl', 'rb'))
    model = pickle.load(open(r'D:\New folder (4)\model.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading model or scalers: {e}")
    st.stop()

# Crop dictionary
crop_dict = {
    1: ('Rice', '🌾'),2: ('Maize', '🌽'),3: ('Jute', '🌱'),4: ('Cotton', '🌿'),
    5: ('Coconut', '🥥'),6: ('Papaya', '🍃'),7: ('Orange', '🍊'),8: ('Apple', '🍏'),
    9: ('Muskmelon', '🍈'),10: ('Watermelon', '🍉'),11: ('Grapes', '🍇'),12: ('Mango', '🥭'),
    13: ('Banana', '🍌'), 14: ('Pomegranate', '🍎'),15: ('Lentil', '🌱'),16: ('Blackgram', '🌱'),
    17: ('Mungbean', '🌱'),18: ('Mothbeans', '🌱'), 19: ('Pigeonpeas', '🌱'),
    20: ('Kidneybeans', '🌱'),21: ('Chickpea', '🌱'),22: ('Coffee', '☕')}


# Create function for prediction
def crop_prediction(input_data):
    
    try:
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        std_data = standard.transform(input_data_reshaped)
        normalized_data = minmax.transform(std_data)
        prediction = model.predict(normalized_data)[0]
        return prediction
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None


st.markdown(
    '''
    <h1 style="color: green;">
        Crop Recommendation System <span style="font-size:30px;">&#127808;</span>
    </h1>
    ''', 
    unsafe_allow_html=True
)

st.write("Kindly provide the necessary inputs to receive your crop prediction")

# Form for input parameters
with st.form(key="crop_form"):
    col1,col2 =st.columns(2)
    # st.write("Enter the required parameters:")

    with col1:
        N = st.number_input("N (Nitrogen)", min_value=0.0, max_value=100.0, step=0.1,value=None)
        P = st.number_input("P (Phosphorus)", min_value=0.0, max_value=100.0, step=0.1,value=None)
        K = st.number_input("K (Potassium)", min_value=0.0, max_value=100.0, step=0.1,value=None)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=100.0, step=0.1,value=None)
    with col2:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=500.0, step=0.1,value=None)
        ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1,value=None)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=1000.0, step=1.0,value=None)
        submit_button = st.form_submit_button(label="Enter")

# Handle validation for missing input
if submit_button:
    # Check if all inputs are filled
    if None in [N, P, K, temperature, humidity, ph, rainfall]:
        st.error("Please fill in all the fields.")
    else:
        # Proceed with prediction if all inputs are filled
        result = crop_prediction([N, P, K, temperature, humidity, ph, rainfall])

        if result is not None and result in crop_dict:
            crop_name = crop_dict[result]  # Unpack the tuple correctly
            st.success(f"The predicted crop type is: **{crop_name}**")
            
        else:
            st.error("Sorry, we could not determine the best crop to be cultivated with the provided data.")



















# # Import libraries
# import pandas as pd
# import numpy as np
# import streamlit as st
# import pickle
# import os

# # Set page configuration
# st.set_page_config(page_title="Crop Recommendation", page_icon=":corn:", layout="wide")


# # Load model and scalers
# try:
#     working_dir = os.path.dirname(os.path.abspath(__file__))
#     minmax = pickle.load(open(r'D:\New folder (4)\minmaxscaler.pkl', 'rb'))
#     standard = pickle.load(open(r'D:\New folder (4)\standscaler.pkl', 'rb'))
#     model = pickle.load(open(r'D:\New folder (4)\model.pkl', 'rb'))
# except FileNotFoundError as e:
#     st.error(f"Error loading model or scalers: {e}")
#     st.stop()

# import streamlit as st

# # Crop dictionary with image URLs for each crop
# crop_dict = {
#     1: ('Rice', 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Golden_Rice.jpg'),
#     2: ('Maize', 'https://upload.wikimedia.org/wikipedia/commons/0/0c/Maize.jpg'),
#     3: ('Jute', 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Jute_Plant.jpg'),
#     4: ('Cotton', 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Cotton_plant.jpg'),
#     5: ('Coconut', 'https://upload.wikimedia.org/wikipedia/commons/3/34/Coconut_tree.jpg'),
#     6: ('Papaya', 'https://upload.wikimedia.org/wikipedia/commons/d/d6/Papaya_tree.jpg'),
#     7: ('Orange', 'https://upload.wikimedia.org/wikipedia/commons/3/39/Orange.jpg'),
#     8: ('Apple', 'https://upload.wikimedia.org/wikipedia/commons/a/a4/Apple_tree.jpg'),
#     9: ('Muskmelon', 'https://upload.wikimedia.org/wikipedia/commons/0/0d/Muskmelon.jpg'),
#     10: ('Watermelon', 'https://upload.wikimedia.org/wikipedia/commons/e/ed/Watermelon.jpg'),
#     11: ('Grapes', 'https://upload.wikimedia.org/wikipedia/commons/1/1d/Grapes.jpg'),
#     12: ('Mango', 'https://upload.wikimedia.org/wikipedia/commons/c/c7/Mango_tree.jpg'),
#     13: ('Banana', 'https://upload.wikimedia.org/wikipedia/commons/9/94/Banana_tree.jpg'),
#     14: ('Pomegranate', 'https://upload.wikimedia.org/wikipedia/commons/3/37/Pomegranate.jpg'),
#     15: ('Lentil', 'https://upload.wikimedia.org/wikipedia/commons/a/a7/Lentil.jpg'),
#     16: ('Blackgram', 'https://upload.wikimedia.org/wikipedia/commons/e/e2/Blackgram.jpg'),
#     17: ('Mungbean', 'https://upload.wikimedia.org/wikipedia/commons/1/14/Mungbean.jpg'),
#     18: ('Mothbeans', 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Moth_beans.jpg'),
#     19: ('Pigeonpeas', 'https://upload.wikimedia.org/wikipedia/commons/4/42/Pigeonpea.jpg'),
#     20: ('Kidneybeans', 'https://upload.wikimedia.org/wikipedia/commons/4/45/Kidney_beans.jpg'),
#     21: ('Chickpea', 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Chickpeas.jpg'),
#     22: ('Coffee', 'https://upload.wikimedia.org/wikipedia/commons/6/60/Coffee_plant.jpg')
# }

# # Example to display crop name and image for a specific crop (e.g., Rice)
# crop_name, crop_image_url = crop_dict[1]  # 1 is for Rice
# st.success(f"The predicted crop is: {crop_name}")
# st.image(crop_image_url, caption=crop_name, use_column_width=True)



# # Create function for prediction
# def crop_prediction(input_data):
    
#     try:
#         input_data_as_numpy_array = np.asarray(input_data)
#         input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
#         std_data = standard.transform(input_data_reshaped)
#         normalized_data = minmax.transform(std_data)
#         prediction = model.predict(normalized_data)[0]
#         return prediction
#     except Exception as e:
#         st.error(f"Error during prediction: {e}")
#         return None


# st.markdown(
#     '''
#     <h1 style="color: green;">
#         Crop Recommendation System <span style="font-size:30px;">&#127808;</span>
#     </h1>
#     ''', 
#     unsafe_allow_html=True
# )

# st.write("Kindly provide the necessary inputs to receive your crop prediction")
# # Form for input parameters
# with st.form(key="crop_form"):
#     col1, col2 = st.columns(2)

#     with col1:
#         N = st.number_input("N (Nitrogen)", min_value=0.0, max_value=100.0, step=0.1, value=None)
#         P = st.number_input("P (Phosphorus)", min_value=0.0, max_value=100.0, step=0.1, value=None)
#         K = st.number_input("K (Potassium)", min_value=0.0, max_value=100.0, step=0.1, value=None)
#         temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=100.0, step=0.1, value=None)

#     with col2:
#         humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=500.0, step=0.1, value=None)
#         ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1, value=None)
#         rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=1000.0, step=1.0, value=None)
#         submit_button = st.form_submit_button(label="Enter")

# # Handle validation for missing input
# if submit_button:
#     # Check if all inputs are filled
#     if None in [N, P, K, temperature, humidity, ph, rainfall]:
#         st.error("Please fill in all the fields.")
#     else:
#         # Proceed with prediction if all inputs are filled
#         result = crop_prediction([N, P, K, temperature, humidity, ph, rainfall])

#         if result is not None and result in crop_dict:
#             crop_name, crop_image_url = crop_dict[result]  # Unpack the tuple correctly
#             st.success(f"The predicted crop is: {crop_name}")
#             st.image(crop_image_url, caption=crop_name, use_column_width=True)
#         else:
#             st.error("Sorry, we could not determine the best crop to be cultivated with the provided data.")


