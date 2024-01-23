#!/usr/bin/env python3
import pymongo
"""
returns id of new created school
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserting school
    """
    res = mongo_collection.insert_one(kwargs)
    doc_id = res.inserted_id

    return doc_id
