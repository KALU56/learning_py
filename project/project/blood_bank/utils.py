from datetime import datetime, timedelta
import re

def validate_email(email):
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format."""
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None

def calculate_next_eligible_date(last_donation_date):
    """Calculate next eligible donation date."""
    last_date = datetime.strptime(last_donation_date, '%Y-%m-%d')
    return (last_date + timedelta(days=56)).strftime('%Y-%m-%d')

def format_datetime(date_string):
    """Format datetime string for display."""
    dt = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
    return dt.strftime('%Y-%m-%d %H:%M')

def get_age(birth_date):
    """Calculate age from birth date."""
    born = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def generate_appointment_slots(date, start_time='09:00', end_time='17:00', duration=30):
    """Generate available appointment slots for a given day."""
    slots = []
    start = datetime.strptime(f"{date} {start_time}", '%Y-%m-%d %H:%M')
    end = datetime.strptime(f"{date} {end_time}", '%Y-%m-%d %H:%M')
    
    current = start
    while current < end:
        slots.append(current.strftime('%H:%M'))
        current += timedelta(minutes=duration)
    
    return slots

def blood_compatibility_check(donor_type, recipient_type):
    """Check blood type compatibility."""
    compatibility_chart = {
        'O-': ['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+'],
        'O+': ['O+', 'A+', 'B+', 'AB+'],
        'A-': ['A-', 'A+', 'AB-', 'AB+'],
        'A+': ['A+', 'AB+'],
        'B-': ['B-', 'B+', 'AB-', 'AB+'],
        'B+': ['B+', 'AB+'],
        'AB-': ['AB-', 'AB+'],
        'AB+': ['AB+']
    }
    return recipient_type in compatibility_chart.get(donor_type, [])