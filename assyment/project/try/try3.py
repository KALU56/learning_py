import sqlite3

class Donor:
    def __init__(self):
        self.conn = sqlite3.connect("blood_bank.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact TEXT,
                blood_type TEXT,
                medical_history TEXT,
                eligibility_status TEXT
            )
        """)
        self.conn.commit()

    def register_donor(self, name, contact, blood_type, medical_history):
        eligibility = self.check_eligibility(medical_history)
        self.cursor.execute("""
            INSERT INTO donors (name, contact, blood_type, medical_history, eligibility_status)
            VALUES (?, ?, ?, ?, ?)
        """, (name, contact, blood_type, medical_history, eligibility))
        self.conn.commit()

    def update_donor(self, donor_id, **kwargs):
        for key, value in kwargs.items():
            self.cursor.execute(f"UPDATE donors SET {key} = ? WHERE id = ?", (value, donor_id))
        self.conn.commit()

    def track_donation_history(self, donor_id):
        self.cursor.execute("""
            SELECT * FROM donations WHERE donor_id = ?
        """, (donor_id,))
        return self.cursor.fetchall()

    def check_eligibility(self, medical_history):
        # Placeholder for real eligibility logic
        return "Eligible" if "none" in medical_history.lower() else "Not Eligible"
class Supervisor:
    def __init__(self):
        self.conn = sqlite3.connect("blood_bank.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS supervisors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                role TEXT,
                access_level INTEGER
            )
        """)
        self.conn.commit()

    def register_supervisor(self, name, role, access_level):
        self.cursor.execute("""
            INSERT INTO supervisors (name, role, access_level)
            VALUES (?, ?, ?)
        """, (name, role, access_level))
        self.conn.commit()

    def approve_donation(self, donation_id, approval_status):
        self.cursor.execute("""
            UPDATE donations SET approval_status = ?
            WHERE id = ?
        """, (approval_status, donation_id))
        self.conn.commit()

    def generate_report(self):
        self.cursor.execute("""
            SELECT * FROM donations
        """)
        return self.cursor.fetchall()
class Appointment:
    def __init__(self):
        self.conn = sqlite3.connect("blood_bank.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER,
                date TEXT,
                time TEXT,
                status TEXT,
                FOREIGN KEY (donor_id) REFERENCES donors(id)
            )
        """)
        self.conn.commit()

    def book_appointment(self, donor_id, date, time):
        self.cursor.execute("""
            INSERT INTO appointments (donor_id, date, time, status)
            VALUES (?, ?, ?, 'Scheduled')
        """, (donor_id, date, time))
        self.conn.commit()

    def manage_slots(self, appointment_id, status):
        self.cursor.execute("""
            UPDATE appointments SET status = ?
            WHERE id = ?
        """, (status, appointment_id))
        self.conn.commit()

    def send_reminders(self, donor_id):
        # Placeholder for email/SMS reminders
        pass
class DonationProcess:
    def __init__(self):
        self.conn = sqlite3.connect("blood_bank.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER,
                date TEXT,
                quantity REAL,
                outcome TEXT,
                approval_status TEXT,
                FOREIGN KEY (donor_id) REFERENCES donors(id)
            )
        """)
        self.conn.commit()

    def record_donation(self, donor_id, date, quantity, outcome):
        self.cursor.execute("""
            INSERT INTO donations (donor_id, date, quantity, outcome, approval_status)
            VALUES (?, ?, ?, ?, 'Pending')
        """, (donor_id, date, quantity, outcome))
        self.conn.commit()

    def update_outcome(self, donation_id, outcome):
        self.cursor.execute("""
            UPDATE donations SET outcome = ?
            WHERE id = ?
        """, (outcome, donation_id))
        self.conn.commit()

    def track_collection(self, donation_id):
        # Placeholder for detailed tracking
        pass
