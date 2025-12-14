import socket
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Load private key
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server listening...")
conn, addr = server.accept()
print("Connected by", addr)

encrypted_msg = conn.recv(4096)

decrypted_msg = private_key.decrypt(
    encrypted_msg,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted message:", decrypted_msg.decode())
conn.close()
