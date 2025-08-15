#!/usr/bin/env python3
"""
Module 9-insert_school
Provides a function to insert a new document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the given MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Key-value pairs representing the document fields.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
