# Chat Application with RSA Encryption

The Chat Application with RSA Encryption is a secure real-time chat system built with Python and Socket.IO, leveraging threading to support multiple clients concurrently. The application ensures data privacy and integrity through RSA asymmetric key encryption, making it suitable for confidential communications.

## Features
- **Real-Time Chat:** Enables instant messaging and real-time communication between connected clients.
- **Multiple Clients:** Utilizes threading to handle multiple client connections simultaneously.
- **TCP Connection:** Uses TCP as the connection protocol for reliable data transmission.
- **RSA Encryption:** Implements RSA asymmetric key encryption to ensure secure and confidential messaging between clients.
- **Key Exchange:** Facilitates secure key exchange between clients at the start of the chat session.

## Encryption Process
1. **Key Generation:** Generates RSA public and private key pairs for each client.
2. **Key Exchange:** Clients exchange their public keys during the initial handshake to establish a secure communication channel.
3. **Message Encryption:** Encrypts outgoing messages with the recipient's public key.
4. **Message Decryption:** Decrypts incoming messages using the recipient's private key.




