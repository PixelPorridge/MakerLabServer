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
@app.route("/read-id", methods=["GET"])
def read_id():
    while True:
        id = tag.readID()

        if id:
            return id


# Set Champion
@app.route("/set-champion", methods=["POST"])
def set_champion():
    data = request.json

    while True:
        id = tag.readID()

        if id:
            data["_id"] = id

            if db.champions.find_one({"_id": id}):
                db.champions.update_one({"_id": id}, {"$set": data})
            else:
                db.champions.insert_one(data)

            return "Success!"


# Update Champion
@app.route("/update-champion", methods=["POST"])
def update_champion():
    data = request.json

    db.champions.update_one({"_id": data["_id"]}, {"$set": data})

    return "Success!"


# Get Champion
@app.route("/get-champion", methods=["GET"])
def get_champion():
    while True:
        id = tag.readID()

        if id:
            data = db.champions.find_one({"_id": id})

            if data:
                return data


# Set Spell
@app.route("/set-spell", methods=["POST"])
def set_spell():
    data = request.json

    while True:
        id = tag.readID()

        if id:
            data["_id"] = id

            if db.spells.find_one({"_id": id}):
                db.spells.update_one({"_id": id}, {"$set": data})
            else:
                db.spells.insert_one(data)

            return "Success!"


# Get Spell
@app.route("/get-spell", methods=["GET"])
def get_spell():
    while True:
        id = tag.readID()

        if id:
            data = db.spells.find_one({"_id": id})

            if data:
                return data


# Clear Database
@app.route("/clear-database", methods=["GET"])
def clear_database():
    db.champions.delete_many({})
    db.spells.delete_many({})

    return "Success!"
