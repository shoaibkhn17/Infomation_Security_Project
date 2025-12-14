# Secure Message Transfer (Python)

This project demonstrates secure message transfer between two computers using
**public-key cryptography (RSA)** in Python.

## Features
- RSA key generation
- Message encryption with public key
- Message decryption with private key
- Client-server socket communication

## How it works
1. Server generates RSA keys.
2. Client encrypts message using server's public key.
3. Server decrypts message using its private key.

## Requirements
- Python 3.x
- cryptography library

Install dependencies:
```bash
pip install cryptography
```

## Files
- key_generator.py
- server.py
- client.py

## Usage
Run server first, then client.
