import pickle
import streamlit as st

# Example data
data = {"name": "Linda", "age": 25, "city": "New York"}

# Save data to a file using pickle
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Load data from the file
with open("data.pkl", "rb") as f:
    d = pickle.load(f)

# Print the loaded data
st.write(d)
