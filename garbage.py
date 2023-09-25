# Package Imports
from flask import Flask, request
from flask_cors import CORS
from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

# Flask Setup
app = Flask(__name__)
CORS(app)

# PiicoDev RFID Setup
tag = PiicoDev_RFID()

# Constants
NUMBER_LENGTH = 2
ACCURACY = 3


# Write Tag Data
@app.route("/write-tag", methods=["POST"])
def write_tag():
    code = encode(request.json)
    written = False
    accuracy_counter = 0

    while True:
        if not written:
            written = tag.writeText(code)
        else:
            tag_code = tag.readText()

            if tag_code == code:
                accuracy_counter += 1
            else:
                accuracy_counter = 0
                written = False

            if accuracy_counter >= ACCURACY:
                return code


# Read Tag Data
@app.route("/read-tag")
def read_tag():
    code = ""
    read = False
    accuracy_counter = 0

    while True:
        if not read:
            code = tag.readText()

            if code:
                read = True
        else:
            tag_code = tag.readText()

            if tag_code == code:
                accuracy_counter += 1
            else:
                accuracy_counter = 0
                read = False

            if accuracy_counter >= ACCURACY:
                return code


# Encode Data
def encode(data: list) -> str:
    code = ""

    for number in data:
        code += "0" * (NUMBER_LENGTH - len(str(number))) + str(number)

    return code


# Decode Data
def decode(code: str) -> list:
    data = []

    for index in range(0, len(str), NUMBER_LENGTH):
        data += int(code[index:index + NUMBER_LENGTH])

    return data
