from ecies.utils import generate_key
from ecies import encrypt, decrypt
import codecs

async def genkeys():
    secp_k = generate_key()
    sk_bytes = secp_k.secret  # bytes
    pk_bytes = secp_k.public_key.format(True)
    with open("eccseasyencryption.key", "wb") as pub_key_file:
        pub_key_file.write(sk_bytes)
    with open("eccpeasyencryption.key", "wb") as priv_key_file:
        priv_key_file.write(pk_bytes)
    keys = [sk_bytes, pk_bytes]
    return keys

async def callskey():
  try:
    key = open("eccseasyencryption.key", "rb").read()
    if str(key) == "b''":
      await genkeys()
      key = open("eccseasyencryption.key", "rb").read()
    return key
  except:
    await genkeys()
    key = open("eccseasyencryption.key", "rb").read()
    return key

async def callpkey():
  try:
    key = open("eccpeasyencryption.key", "rb").read()
    if str(key) == "b''":
      await genkeys()
      key = open("eccpeasyencryption.key", "rb").read()
    return key
  except:
    await genkeys()
    key = open("eccpeasyencryption.key", "rb").read()
    return key

async def eccencrypt(slogan):
    data = codecs.encode(slogan)
    pk_bytes = await callpkey()  # bytes
    encrypted = encrypt(pk_bytes, data)
    return encrypted

async def eccdecrypt(coded_slogan):
    sk_bytes = await callskey()  # bytes
    decrypted_byted = decrypt(sk_bytes, coded_slogan)
    decrypted = codecs.decode(decrypted_byted)
    return decrypted
