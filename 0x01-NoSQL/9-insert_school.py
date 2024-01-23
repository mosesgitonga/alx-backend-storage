#!/usr/bin/env python3
"""
returns id of new created school
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserting school
    """
    res = mongo_collection.insert_one(kwargs)
    doc_id = res.inserted_id

    return doc_id
