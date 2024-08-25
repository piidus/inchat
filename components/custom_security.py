
import rsa

def generate_keys():
    # Generate RSA private and public keys
    (public_key, private_key) = rsa.newkeys(2048)
    return private_key, public_key


def generate_message(input_text, public_key, private_key):
    # Convert input text to bytes
    message = str(input_text).encode('utf-8')

    # Encrypt the message using the public key
    encrypted_message = rsa.encrypt(message, public_key)

    # Decrypt the message using the private key
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    
    return encrypted_message, decrypted_message

if __name__ == '__main__':
    private_key, public_key = generate_keys()
    
    encrypted_message, decrypted_message = generate_message('Hello, World!', public_key, private_key)

    # Print results
    print("Public Key:\n", public_key.save_pkcs1().decode('utf-8'))
    print("Private Key:\n", private_key.save_pkcs1().decode('utf-8'))
    print("Encrypted Message:\n", encrypted_message)
    print("Decrypted Message:\n", decrypted_message.decode('utf-8'))
