#!/usr/bin/python3
"""This module creates a Review class"""
from base_model import BaseModel


class Review(BaseModel):
    """A class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
