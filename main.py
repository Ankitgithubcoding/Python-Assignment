import streamlit as st

# 1. Displaying Text
st.write("Welcome to My First Streamlit App!")

# 2. Adding a Header
st.header("This is a Header")

# 3. Using a Button
if st.button("Click Me!"):
    st.write("Button Clicked!")

# 4. Displaying a Simple List
fruits = ["Apple", "Banana", "Cherry"]
st.write(f"My favorite fruits are: {', '.join(fruits)}")

# 5. Adding an Image
image_url = "C:\Users\hp\OneDrive\Desktop\Python Assignment Live Project\Python-Assignment\camp.jpg"
st.image(image_url, caption="This is an example image")
