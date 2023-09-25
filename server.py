# Package Imports
import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
from pymongo import MongoClient

# Load Environment Variables
load_dotenv()

# Flask Setup
app = Flask(__name__)
CORS(app)

# PiicoDev RFID Setup
tag = PiicoDev_RFID()

# MongoDB Setup
client = MongoClient(os.getenv("MONGODB_CONNECTION"))
db = client.game


# Read Tag
@app.route("/read-tag", methods=["GET"])
def read_tag():
    while True:
        id = tag.readID()

        if id:
            return id


# Set Champion
@app.route("/set-champion", methods=["POST"])
def set_champion():
    data = request.json
    champions = db.champions

    while True:
        id = tag.readID()

        if id:
            data["_id"] = id

            if champions.find_one({"_id": id}):
                champions.update_one({"_id": id}, {"$set": data})
            else:
                champions.insert_one(data)

            return "Success!"


# Get Champion
@app.route("/get-champion", methods=["GET"])
def get_champion():
    champions = db.champions

    while True:
        id = tag.readID()

        if id:
            data = champions.find_one({"_id": id})

            if data:
                return data


# Set Spell
@app.route("/set-spell", methods=["POST"])
def set_spell():
    data = request.json
    spells = db.spells

    while True:
        id = tag.readID()

        if id:
            data["_id"] = id

            if spells.find_one({"_id": id}):
                spells.update_one({"_id": id}, {"$set": data})
            else:
                spells.insert_one(data)

            return "Success!"


# Get Spell
@app.route("/get-spell", methods=["GET"])
def get_spell():
    spells = db.spells

    while True:
        id = tag.readID()

        if id:
            data = spells.find_one({"_id": id})

            if data:
                return data
