import streamlit as st
import random
import string

def generator_password(lenght, use_digits, use_special):
    characters =string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
      characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(lenght)) 
st.title("Password Generator")

lenght = st.slider("Select password lenght", min_value=6, max_value=30, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generated Password"):
   password = generator_password(lenght, use_digits, use_special)
   st.write(f"Generated Password:", {password})

   st.write("build with by Sherkhan")
