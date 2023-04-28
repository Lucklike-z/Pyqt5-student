import hashlib


def encode_md5(passwd):
    passwd = str(passwd)
    md5_encoder = hashlib.md5()
    md5_encoder.update(passwd.encode('utf-8'))
    encrypted_str = md5_encoder.hexdigest()
    return encrypted_str
