"""
Blood Bank Management System
This package handles blood donation management, supervisor and donor interactions.
"""

# Version information
__version__ = '1.0.0'

# Configuration constants
CONFIG = {
    'BLOOD_TYPES': ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
    'MIN_DONOR_AGE': 18,
    'MAX_DONOR_AGE': 65,
    'MIN_WEIGHT': 50,  # in kg
    'MIN_HEMOGLOBIN': 12.5,  # in g/dL
    'DONATION_INTERVAL_DAYS': 56,  # minimum days between donations
}

# Database paths
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(DATA_DIR, 'blood_bank_data.json')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# GUI Theme settings
GUI_THEME = {
    'PRIMARY_COLOR': '#ff4444',  # Red theme for blood bank
    'SECONDARY_COLOR': '#ffffff',
    'FONT_FAMILY': 'Arial',
    'HEADING_SIZE': 14,
    'NORMAL_SIZE': 10,
    'BUTTON_COLOR': '#ff6666',
    'BUTTON_TEXT_COLOR': '#ffffff',
}

# Message types
MESSAGE_TYPES = {
    'APPOINTMENT_CONFIRMATION': 'appointment_confirmation',
    'DONATION_REMINDER': 'donation_reminder',
    'GENERAL_UPDATE': 'general_update',
    'EMERGENCY_REQUEST': 'emergency_request'
}