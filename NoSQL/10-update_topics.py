#!/usr/bin/env python3
"""
Module 10-update_topics
Provides a function to update the topics of a school document by name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the school name.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
