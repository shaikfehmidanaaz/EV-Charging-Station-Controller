# EV Charging Station Controller
# Python Project for EEE Students

class EVChargingStation:

    def __init__(self, charger_power, battery_capacity, tariff):
        self.charger_power = charger_power      # kW
        self.battery_capacity = battery_capacity  # kWh
        self.tariff = tariff                    # ₹/kWh

    def calculate_energy(self, initial_soc, target_soc):
        soc_difference = target_soc - initial_soc
        energy = (soc_difference / 100) * self.battery_capacity
        return energy

    def calculate_charging_time(self, energy):
        return energy / self.charger_power

    def calculate_cost(self, energy):
        return energy * self.tariff

    def start_charging(self, initial_soc, target_soc):

        print("\n======================================")
        print("       EV CHARGING STATION")
        print("======================================")

        print(f"Initial Battery SOC : {initial_soc:.1f}%")
        print(f"Target Battery SOC  : {target_soc:.1f}%")
        print(f"Charger Power       : {self.charger_power:.2f} kW")
        print(f"Battery Capacity    : {self.battery_capacity:.2f} kWh")

        # Calculate energy required
        energy = self.calculate_energy(
            initial_soc,
            target_soc
        )

        # Calculate charging time
        charging_time = self.calculate_charging_time(energy)

        # Calculate cost
        cost = self.calculate_cost(energy)

        print("\n----------- CHARGING DETAILS -----------")
        print(f"Energy Required     : {energy:.2f} kWh")
        print(f"Charging Time       : {charging_time:.2f} hours")
        print(f"Charging Cost       : ₹{cost:.2f}")

        print("\nCharging Status      : CHARGING")

        print("\n======================================")
        print("       CHARGING COMPLETED")
        print("======================================")

        print(f"Final Battery SOC   : {target_soc:.1f}%")
        print(f"Total Energy        : {energy:.2f} kWh")
        print(f"Total Cost          : ₹{cost:.2f}")


# Main program

print("======================================")
print("     EV CHARGING STATION CONTROLLER")
print("======================================")

# User input

charger_power = float(
    input("Enter Charger Power (kW): ")
)

battery_capacity = float(
    input("Enter Battery Capacity (kWh): ")
)

initial_soc = float(
    input("Enter Initial Battery SOC (%): ")
)

target_soc = float(
    input("Enter Target Battery SOC (%): ")
)

tariff = float(
    input("Enter Electricity Tariff (₹/kWh): ")
)

# Validate inputs

if charger_power <= 0:
    print("Charger power must be greater than zero.")

elif battery_capacity <= 0:
    print("Battery capacity must be greater than zero.")

elif initial_soc < 0 or initial_soc > 100:
    print("Initial SOC must be between 0 and 100.")

elif target_soc < 0 or target_soc > 100:
    print("Target SOC must be between 0 and 100.")

elif target_soc <= initial_soc:
    print("Target SOC must be greater than initial SOC.")

elif tariff < 0:
    print("Tariff cannot be negative.")

else:
    station = EVChargingStation(
        charger_power,
        battery_capacity,
        tariff
    )

    station.start_charging(
        initial_soc,
        target_soc
    )
