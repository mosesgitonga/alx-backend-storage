#!/usr/bin/env python3
"""
change school topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update topics
    """
    filter_name = {}
    filter_name['name'] = name

    update_operation = {"$set": {"topics": topics}}
    res = mongo_collection.update_many(filter_name, update_operation)
    return res
