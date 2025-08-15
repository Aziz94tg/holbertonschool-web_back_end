#!/usr/bin/env python3
"""
Module 8-all
Provides a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    List all documents in the given MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of all documents in the collection.
        If the collection is empty, returns an empty list.
    """
    return list(mongo_collection.find())
