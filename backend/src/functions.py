import mysql.connector
from mysql.connector import connect, Error
import hashlib
from datetime import datetime


def connectDB():

    try:
        with connect(
            host="localhost",
            user="root",
            password="yourpasswd",
            database="url_db",
            port="3306"
        ) as connection:
            print("Connected to url_db")
    except Error as e:
        print(e)

    return connection


def shortener(string):

    # Encode the string into byte format
    string = string.encode()

    # Hash Byte String into a hash object with SHA256
    hashed = hashlib.sha256(string).hexdigest()

    def encode(hashed):
        # Converting hexadecimal values into integers

        hashed = int(hashed, 16)
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)

        ret = []

        while hashed > 0:
            val = hashed % base
            ret.append(characters[val])
            hashed = hashed // base

        return "".join(ret[:-7:-1])

    shortened_url = encode(hashed)

    return shortened_url
