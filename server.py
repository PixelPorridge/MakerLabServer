# Package Imports
from flask import Flask, request
from flask_cors import CORS
from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

# File Imports
from tags import *

# Flask Setup
app = Flask(__name__)
CORS(app)

# PiicoDev RFID Setup
tag = PiicoDev_RFID()

# Constants
SCAN_COUNT = 200


@app.route("/scan-tag")
def scan_tag():
    for i in range(SCAN_COUNT):
        id = tag.readID()

        if id:
            return "Tag ID: " + id

    return "Scan Tag Request Timeout!", 500


@app.route("/reset-champion")
def reset_champion():
    return "Reset Champion Request Failed!", 500


@app.route("/set-champion")
def set_champion():
    return "Set Champion Request Failed!", 500


@app.route("/set-spell")
def set_spell():
    return "Set Spell Request Failed!", 500
