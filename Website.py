import streamlit as st
import joblib
import pandas as pd


# Load the model and columns
@st.cache_resource
def load_model():
    model = joblib.load('iris_model.pkl')
    columns = joblib.load('iris_columns.pkl')
    return model, columns

# Create the Streamlit app
def main():
    model, columns = load_model()
    st.title("Iris Flower Prediction")
    st.write("This app predicts the species of iris flowers based on their features.")

    # Create input fields for the features
    inputs = {}
    for col in columns:
        inputs[col] = st.number_input(f"Enter {col}", min_value=0.0, max_value=10.0, step=0.1)

    # Make a prediction when the button is clicked
    if st.button("Predict"):
        features = pd.DataFrame([inputs])
        prediction = model.predict(features)
        st.write(f"Predicted species: {prediction[0]}")
# Run the app
if __name__ == "__main__":
    main()