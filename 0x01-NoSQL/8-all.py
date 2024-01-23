#!/usr/bin/env python3
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List[dict]:
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.

    Returns:
        List[dict]: A list of dictionaries representing the documents in the collection.
    """
    cursor = mongo_collection.find({})
    documents = list(cursor)
    cursor.close()

    return documents