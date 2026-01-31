import json
import os

FILE_NAME = "custom_data.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return {
            "Chest": [],
            "Back": [],
            "Legs": [],
            "Shoulders": [],
            "Arms": []
        }

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


custom_exercises = load_data()


def add_custom_exercise(muscle, name, desc):
    custom_exercises[muscle].append([name, desc])
    save_data(custom_exercises)


def get_custom_exercises(muscle):
    return custom_exercises[muscle]
