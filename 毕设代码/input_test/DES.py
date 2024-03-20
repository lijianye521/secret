from Crypto.Cipher import DES
import pandas as pd
from Crypto.Util.Padding import pad, unpad
import argparse
import base64

key = b'churnkey'

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(str(plaintext).encode('utf-8'), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    decrypted = unpad(decrypted_padded_text, DES.block_size)
    return int(decrypted.decode('utf-8'))  

def encrypt_csv_column(file_path, key=key):
    df = pd.read_csv(file_path)

    df["id"] = df["id"].apply(lambda x: base64.b64encode(des_encrypt(x, key)).decode('utf-8'))

    df.to_csv(file_path, index=False)
    
def decrypt_csv_column(file_path,  key=key):
    df = pd.read_csv(file_path)

    df["id"] = df["id"].apply(lambda x: des_decrypt(base64.b64decode(x.encode('utf-8')), key))

    df.to_csv(file_path, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--test_file_path', type=str, default='/home/xyj/Downloads/code/1/input_test/churn_test_with_predictions.csv',
                        help='test dataset ')
    args = parser.parse_args()
    decrypt_csv_column(args.test_file_path, key)


