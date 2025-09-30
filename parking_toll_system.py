# Folder structure:
# parking_toll/
# ├── vehicle.py
# ├── parking_lot.py
# ├── main.py
# └── tests/
#     ├── test_vehicle.py
#     └── test_parking_lot.py

# vehicle.py
from datetime import datetime

class Vehicle:
    def __init__(self, number_plate, vehicle_type, zone="Regular", subscription=False):
        self.number_plate = number_plate
        self.vehicle_type = vehicle_type  # Car, Bike, Truck
        self.zone = zone  # Regular, VIP, Handicapped
        self.subscription = subscription  # Monthly pass
        self.entry_time = None
        self.exit_time = None

    def enter_parking(self):
        self.entry_time = datetime.now()

    def exit_parking(self):
        self.exit_time = datetime.now()

    def parking_duration_hours(self):
        if not self.entry_time or not self.exit_time:
            return 0
        duration = self.exit_time - self.entry_time
        return duration.total_seconds() / 3600


# parking_lot.py
from datetime import time
from vehicle import Vehicle

class ParkingLot:
    BASE_RATES = {
        "Car": 20,
        "Bike": 10,
        "Truck": 30
    }

    ZONE_MULTIPLIER = {
        "Regular": 1,
        "VIP": 1.5,
        "Handicapped": 0.5
    }

    PEAK_START = time(8, 0)
    PEAK_END = time(20, 0)
    PEAK_MULTIPLIER = 1.2
    MONTHLY_SUBSCRIPTION_RATE = 2000  # flat monthly fee

    def __init__(self):
        self.vehicles = []

    def vehicle_entry(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only Vehicle instances allowed")
        vehicle.enter_parking()
        self.vehicles.append(vehicle)

    def vehicle_exit(self, number_plate):
        for vehicle in self.vehicles:
            if vehicle.number_plate == number_plate:
                vehicle.exit_parking()
                fee = self.calculate_fee(vehicle)
                return fee
        raise ValueError("Vehicle not found")

    def calculate_fee(self, vehicle):
        if vehicle.subscription:
            return self.MONTHLY_SUBSCRIPTION_RATE

        hours = max(1, round(vehicle.parking_duration_hours()))
        base_rate = self.BASE_RATES.get(vehicle.vehicle_type, 20)
        zone_multiplier = self.ZONE_MULTIPLIER.get(vehicle.zone, 1)
        peak_multiplier = self._get_peak_multiplier(vehicle)

        fee = hours * base_rate * zone_multiplier * peak_multiplier
        return round(fee)

    def _get_peak_multiplier(self, vehicle):
        if not vehicle.entry_time:
            return 1
        entry_hour = vehicle.entry_time.time()
        if self.PEAK_START <= entry_hour <= self.PEAK_END:
            return self.PEAK_MULTIPLIER
        return 1


# main.py
import time
from vehicle import Vehicle
from parking_lot import ParkingLot

def main():
    lot = ParkingLot()

    # Sample vehicles
    car_vip = Vehicle("KA01VIP1234", "Car", zone="VIP")
    bike_handicapped = Vehicle("KA02HND5678", "Bike", zone="Handicapped")
    truck_regular = Vehicle("KA03TR9999", "Truck", subscription=True)

    lot.vehicle_entry(car_vip)
    lot.vehicle_entry(bike_handicapped)
    lot.vehicle_entry(truck_regular)

    print("Vehicles entered parking lot...")

    # Simulate parking duration
    time.sleep(2)

    print(f"VIP Car fee: ₹{lot.vehicle_exit('KA01VIP1234')}")
    print(f"Handicapped Bike fee: ₹{lot.vehicle_exit('KA02HND5678')}")
    print(f"Truck with subscription fee: ₹{lot.vehicle_exit('KA03TR9999')}")

if __name__ == "__main__":
    main()


# tests/test_vehicle.py
from datetime import datetime, timedelta
from vehicle import Vehicle

def test_vehicle_entry_exit():
    v = Vehicle("KA01AB1234", "Car")
    v.enter_parking()
    assert v.entry_time is not None
    v.exit_time = v.entry_time + timedelta(hours=2)
    assert v.parking_duration_hours() == 2


# tests/test_parking_lot.py
from datetime import datetime, timedelta, time
from vehicle import Vehicle
from parking_lot import ParkingLot

def test_vehicle_fee_regular():
    lot = ParkingLot()
    car = Vehicle("KA01REG", "Car")
    lot.vehicle_entry(car)
    car.exit_time = car.entry_time + timedelta(hours=2)
    fee = lot.calculate_fee(car)
    assert fee == 40

def test_vehicle_fee_vip_peak():
    lot = ParkingLot()
    car = Vehicle("KA02VIP", "Car", zone="VIP")
    car.entry_time = datetime.combine(datetime.today(), time(10, 0))  # Peak hour
    car.exit_time = car.entry_time + timedelta(hours=1)
    fee = lot.calculate_fee(car)
    assert fee == 36  # 20 * 1.5 * 1.2

def test_vehicle_fee_subscription():
    lot = ParkingLot()
    truck = Vehicle("KA03SUB", "Truck", subscription=True)
    lot.vehicle_entry(truck)
    fee = lot.calculate_fee(truck)
    assert fee == lot.MONTHLY_SUBSCRIPTION_RATE

def test_vehicle_not_found():
    lot = ParkingLot()
    try:
        lot.vehicle_exit("NOTEXIST")
        assert False
    except ValueError as e:
        assert str(e) == "Vehicle not found"

def test_invalid_vehicle_type():
    lot = ParkingLot()
    class Dummy:
        pass
    try:
        lot.vehicle_entry(Dummy())
        assert False
    except TypeError:
        assert True