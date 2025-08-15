#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Provides a function to retrieve all schools with a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of documents (schools) that contain the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))
