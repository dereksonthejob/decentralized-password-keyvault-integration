from keychain import Keychain

# Create a new instance of the Keychain class
keychain = Keychain()

# Add a password to the keychain
keychain.add_password("example_account", "example_password")

# Retrieve a password from the keychain
password = keychain.get_password("example_account")
print(password)
