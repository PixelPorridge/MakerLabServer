# Package Imports
from flask import Flask, request
from flask_cors import CORS
from PiicoDev_RFID import PiicoDev_RFID

# File Imports
from modules.tags import *
from modules.champions import *
from modules.spells import *

# Flask Setup
app = Flask(__name__)
CORS(app)

# PiicoDev RFID Setup
tag = PiicoDev_RFID()


@app.route("/scan-tag")
def scan_tag():
    id = tag.readID()

    if id:
        return "Tag ID: " + id
    else:
        return "Scan Tag Request Failed!", 500


@app.route("/reset-champion")
def reset_champion():
    return "Reset Champion Request Failed!", 500


@app.route("/reset-spell")
def reset_spell():
    return "Reset Spell Request Failed!", 500


@app.route("/set-champion")
def set_champion():
    return "Set Champion Request Failed!", 500


@app.route("/set-spell")
def set_spell():
    return "Set Spell Request Failed!", 500
