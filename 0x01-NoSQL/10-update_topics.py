#!/usr/bin/env python3
""" A Python function that changes all topics of a school doc based on name """


def update_topics(mongo_collection, name, topics):
    """ Updates collection """
    mongo_collection.update_one({'name': name}, {"$set": {'topics': topics}})
