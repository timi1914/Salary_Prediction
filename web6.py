import streamlit as st

def main():
    st.title("Age Input App")
    st.write("Please enter your age.")

    age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)

    if st.button("Submit"):
        st.write("Your age is:", age)

if __name__ == "__main__":
    main()
