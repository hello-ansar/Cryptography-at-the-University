class DH_crypt(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


message = "The most secret message!"

s_public = 197
s_private = 199
m_public = 151
m_private = 157
First_guy = DH_crypt(s_public, m_public, s_private)
Second_guy = DH_crypt(s_public, m_public, m_private)



def generate_partial_key(self):
    partial_key = self.public_key1 ** self.private_key
    partial_key = partial_key % self.public_key2
    return partial_key


s_partial = First_guy.generate_partial_key()
print(s_partial)

m_partial = Second_guy.generate_partial_key()
print(m_partial)


def generate_full_key(self, partial_key_r):
    full_key = partial_key_r ** self.private_key
    full_key = full_key % self.public_key2
    self.full_key = full_key
    return full_key


s_full = First_guy.generate_full_key(m_partial)
print(s_full)

m_full = Second_guy.generate_full_key(s_partial)
print(m_full)


def encrypt_message(self, message):
    encrypted_message = ""
    key = self.full_key
    for c in message:
        encrypted_message += chr(ord(c) + key)
    return encrypted_message


m_encrypted = Second_guy.encrypt_message(message)
print(m_encrypted)


def decrypt_message(self, encrypted_message):
    decrypted_message = ""
    key = self.full_key
    for c in encrypted_message:
        decrypted_message += chr(ord(c) - key)
    return decrypted_message


message = First_guy.decrypt_message(m_encrypted)
print(message)
