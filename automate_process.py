import subprocess

def automate_process():
    subprocess.run(["python", "rectifier_simulation.py"])
    subprocess.run(["python", "energy_storage.py"])
    subprocess.run(["python", "power_management.py"])

if __name__ == "__main__":
    automate_process()
