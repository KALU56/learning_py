import sys
import os

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from blood_bank.main import main

if __name__ == "__main__":
    main()