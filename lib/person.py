#!/usr/bin/env python3
#person.py
APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
class Person:
    def __init__(self, name="", job=""):
        self.name = name.title() if isinstance(name, str) else ""

        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = ""

        self.job = job if job in APPROVED_JOBS else ""
        if not self.job:
            print("Job must be in list of approved jobs.")
            print("Name must be string between 1 and 25 characters.")  
