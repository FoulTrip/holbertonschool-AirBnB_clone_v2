#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine import db_storage
import os

storage = os.getenv("HBNB_TYPE_STORAGE")

if storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
