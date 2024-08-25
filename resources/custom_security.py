from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate RSA private and public keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Serialize the private key with PEM encoding
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Serialize the public key with PEM encoding
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Encrypt a message
message = b"Hello, World!"
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the message
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Print results
print("Private Key:\n", private_pem.decode('utf-8'))
print("Public Key:\n", public_pem.decode('utf-8'))
print("Encrypted Message:\n", encrypted_message)
print("Decrypted Message:\n", decrypted_message.decode('utf-8'))

# import rsa

# def generate_keys():
#     # Generate RSA private and public keys
#     (public_key, private_key) = rsa.newkeys(2048)
#     return private_key, public_key


# def generate_message(input_text, public_key, private_key):
#     # Convert input text to bytes
#     message = str(input_text).encode('utf-8')

#     # Encrypt the message using the public key
#     encrypted_message = rsa.encrypt(message, public_key)

#     # Decrypt the message using the private key
#     decrypted_message = rsa.decrypt(encrypted_message, private_key)
    
#     return encrypted_message, decrypted_message

# if __name__ == '__main__':
#     private_key, public_key = generate_keys()
    
#     encrypted_message, decrypted_message = generate_message('Hello, World!', public_key, private_key)

#     # Print results
#     print("Public Key:\n", public_key.save_pkcs1().decode('utf-8'))
#     print("Private Key:\n", private_key.save_pkcs1().decode('utf-8'))
#     print("Encrypted Message:\n", encrypted_message)
#     print("Decrypted Message:\n", decrypted_message.decode('utf-8'))
