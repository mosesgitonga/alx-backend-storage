#!/usr/bin/env python3
"""
where to learn python
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    searching for school
        Return schools to learn a topic
    """
    search_filter = {"topics": topic}
    schools = mongo_collection.find(search_filter)
    return schools
