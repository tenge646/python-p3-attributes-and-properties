#!/usr/bin/env python3

#dog.py
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed

        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = ""
        
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = ""

