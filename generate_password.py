import streamlit_authenticator as stauth

# Your real passwords
passwords = [
    "MdCardstel$2026",
    "Hr@Admin2026",
    "PA$Secure_92"
]

# Generate hashes
hashed_passwords = stauth.Hasher(passwords).generate()

print(hashed_passwords)
