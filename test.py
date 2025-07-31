from flask import Flask, render_template, request, redirect, url_for, flash, session
import base64
import os
import numpy as np
import mysql.connector
import re
import razorpay
import razorpay.errors
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import timedelta, datetime
from werkzeug.utils import secure_filename
import cv2
import random
import string
from io import BytesIO
from flask import send_file
from PIL import Image, ImageDraw, ImageFont
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from googleapiclient.discovery import build
from google.oauth2 import service_account
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bson.objectid import ObjectId
from flask import Flask, jsonify
from bson import ObjectId
from bson.errors import InvalidId
from flask_pymongo import PyMongo
from flask_pymongo import PyMongo
from flask_pymongo import PyMongo
import tensorflow as tf
from tensorflow import keras
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# MongoDB connection (added from ChronoTunes)
key = "6Kto5LxwDqchjAc0"
uri = "mongodb+srv://abhirajbanerjee02:6Kto5LxwDqchjAc0@cluster-chronotunes.pkxxz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-ChronoTunes"
mongoClient = MongoClient(uri, server_api=ServerApi('1'))
collection = mongoClient['users']['chronoTunes']
song_db = mongoClient['songs']
playlist_collection = mongoClient['mood_detection_playlist_data']['user_playlists']


def create_drive_service():
    SERVICE_ACCOUNT_FILE = 'credentials.json'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

service = create_drive_service()
genre = 'Classical'
mood = 'happy'
collection = song_db[genre.lower()]
mood_regex = {"$regex": f"^{mood}$", "$options": "i"}
mongo_songs = list(collection.find({ "mood": mood_regex }, {"filename": 1},{"file_data": 1}))
all_pickle_names = [song['file_data'] for song in mongo_songs if 'file_data' in song]
print(all_pickle_names)
print(mongo_songs[0]["file_data"])