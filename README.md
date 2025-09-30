🚗 Parking Toll Management System
📌 Overview

The Parking Toll Management System is a Python-based application that automates vehicle parking, toll fee calculation, and subscription management. It demonstrates object-oriented programming (OOP) concepts and includes comprehensive PyTest unit tests to validate core logic and business rules.

This project was developed as part of my backend and problem-solving practice, showcasing my ability to design clean, testable, and production-ready Python code.

🎯 Features

🅿️ Vehicle entry/exit handling with parking slot management.

💰 Zone-based pricing: Regular, VIP, and Handicapped zones.

⏰ Peak & Off-Peak Multipliers for dynamic pricing.

📅 Monthly subscription plans for frequent users.

🧾 Robust fee calculation logic.

✅ Unit testing with PyTest covering fee calculation, subscriptions, and error handling.

🛠️ Tech Stack

Language: Python

Testing: PyTest

Concepts: OOP (Classes, Inheritance, Encapsulation), Exception Handling

📂 Project Structure

Parking-Toll-System/
│── parking_lot.py          # Core logic (Vehicle, ParkingLot classes)  
│── test_parking_lot.py     # PyTest unit test cases  
│── demo.py                 # Sample script to run the system  
│── README.md               # Documentation  

🚀 Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/yourusername/Parking-Toll-System.git
cd Parking-Toll-System

Run the demo script
python demo.py

Run the unit tests
pytest -v

🧪 Example (Demo)
from parking_lot import ParkingLot, Vehicle

lot = ParkingLot()
car = Vehicle("KA01AB1234", "Regular")

lot.check_in(car)
lot.check_out(car)

print("Fee Collected:", lot.calculate_fee(car))


📊 Unit Tests

✅ Fee calculation across different zones (Regular, VIP, Handicapped).

✅ Peak vs Off-Peak multipliers.

✅ Monthly subscription validation.

✅ Error handling for invalid inputs.

Run tests with:
pytest --maxfail=1 --disable-warnings -q


📌 My Contribution (as per Resume)

Designed Vehicle and ParkingLot classes using Python OOP.

Implemented zone-based pricing, peak/off-peak logic, and subscriptions.

Wrote comprehensive PyTest test suites.

Developed a demo script to simulate real-world scenarios.


📌 Future Enhancements

💳 Payment gateway simulation.

📱 Web-based dashboard (Django + Angular).

🔄 Integration with IoT sensors (RFID/barcodes) for vehicle detection.


🤝 Connect With Me

👨‍💻 Nadupalle Sai Ganesh

📧 Email: nadupalleganesh@gmail.com

💼 LinkedIn:https://www.linkedin.com/in/nadupalle-sai-ganesh-22890b336/


