import json
import os
from datetime import datetime
from . import DB_PATH

class DataManager:
    def __init__(self):
        self.initialize_db()
    
    def initialize_db(self):
        if not os.path.exists(DB_PATH):
            default_data = {
                'users': {
                    'supervisor': {
                        'username': 'admin',
                        'password': 'admin123',
                        'role': 'supervisor'
                    }
                },
                'donors': {},
                'blood_inventory': {
                    'A+': 0, 'A-': 0, 'B+': 0, 'B-': 0,
                    'AB+': 0, 'AB-': 0, 'O+': 0, 'O-': 0
                },
                'appointments': {},
                'messages': {},
                'donation_camps': {}
            }
            self.save_data(default_data)
    
    def load_data(self):
        try:
            with open(DB_PATH, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None

    def save_data(self, data):
        with open(DB_PATH, 'w') as file:
            json.dump(data, file, indent=4)

    def add_donor(self, donor_data):
        data = self.load_data()
        donor_id = f"D{len(data['donors']) + 1:04d}"
        data['donors'][donor_id] = donor_data
        self.save_data(data)
        return donor_id

    def update_blood_inventory(self, blood_type, amount):
        data = self.load_data()
        data['blood_inventory'][blood_type] += amount
        self.save_data(data)

    def add_appointment(self, donor_id, date_time):
        data = self.load_data()
        appointment_id = f"A{len(data['appointments']) + 1:04d}"
        data['appointments'][appointment_id] = {
            'donor_id': donor_id,
            'date_time': date_time,
            'status': 'pending'
        }
        self.save_data(data)
        return appointment_id

    def add_message(self, sender, receiver, message_type, content):
        data = self.load_data()
        message_id = f"M{len(data['messages']) + 1:04d}"
        data['messages'][message_id] = {
            'sender': sender,
            'receiver': receiver,
            'type': message_type,
            'content': content,
            'timestamp': datetime.now().isoformat(),
            'read': False
        }
        self.save_data(data)