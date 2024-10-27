def power_management(stored_energy, consumption_rate=5):
    while stored_energy > 0:
        stored_energy -= consumption_rate
        print(f"Remaining Energy: {stored_energy} units")
    print("Energy depleted.")

if __name__ == "__main__":
    stored_energy = 1000  # Example value
    power_management(stored_energy)
