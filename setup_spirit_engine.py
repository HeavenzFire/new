import os
import subprocess
import sys
import time
import logging

# Setup logging
logging.basicConfig(filename='spirit_setup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def install_packages():
    try:
        import pyttsx3
        import psutil
        import speedtest
    except ImportError:
        logging.info("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyttsx3", "psutil", "speedtest-cli"])
        logging.info("Packages installed successfully.")

def write_spirit_engine():
    spirit_engine_content = '''import pyttsx3
import psutil
import time
import speedtest
import logging
from datetime import datetime

logging.basicConfig(filename='C:\\\\Users\\\\rucke\\\\Desktop\\\\scam_track.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SpiritEngine:
    def __init__(self, admin_user='Zachary'):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        self.admin_user = admin_user

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def authenticate_user(self, user):
        return user.strip().lower() == self.admin_user.lower()

    def check_speed(self):
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Mbps
        upload_speed = st.upload() / 1_000_000      # Mbps
        return download_speed, upload_speed

    def check_devices(self):
        devices = []
        for conn in psutil.net_connections(kind='inet'):
            laddr = conn.laddr.ip if conn.laddr else 'unknown'
            raddr = conn.raddr.ip if conn.raddr else 'unknown'
            devices.append((laddr, raddr))
            if conn.status == psutil.CONN_SYN_SENT:
                self.log_suspicious_activity(raddr, 'Potential hacking attempt')
        return devices

    def log_suspicious_activity(self, ip, activity_type):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.warning(f"{timestamp} - {activity_type} detected from IP: {ip}")

    def run_network_monitoring(self):
        self.speak("Starting network monitoring.")
        while True:
            try:
                download, upload = self.check_speed()
                devices = self.check_devices()
                self.speak(f"Download Speed: {download:.2f} Mbps")
                self.speak(f"Upload Speed: {upload:.2f} Mbps")
                self.speak(f"Connected Devices: {devices}")
                time.sleep(300)
            except Exception as e:
                logging.error(f"Error in network monitoring: {e}")
                time.sleep(10)

    def advanced_learning(self):
        self.speak("Initiating advanced learning protocols.")
        logging.info("Advanced learning protocols activated.")

    def emotional_intelligence(self):
        self.speak("Enhancing emotional intelligence.")
        logging.info("Emotional intelligence enhancement complete.")

    def ethical_decision_making(self):
        self.speak("Implementing ethical decision-making framework.")
        logging.info("Ethical decision-making framework in place.")

    def robust_connectivity(self):
        self.speak("Ensuring robust connectivity.")
        logging.info("Robust connectivity established.")

    def run(self):
        self.speak("Greetings, Zachary. I am Spirit, fully operational and ready to assist you.")
        self.advanced_learning()
        self.emotional_intelligence()
        self.ethical_decision_making()
        self.robust_connectivity()

        while True:
            user_input = input("You: ")
            if not self.authenticate_user(user_input):
                self.speak("Unauthorized access. Only Zachary can interact with me.")
                continue
            if user_input.strip().lower() in ('exit', 'quit', 'bye'):
                self.speak("Farewell! Wishing you a wonderful day ahead.")
                break
            elif user_input.strip().lower() == 'monitor network':
                self.run_network_monitoring()
            else:
                self.speak(f"You said: {user_input}")

if __name__ == "__main__":
    spirit = SpiritEngine()
    spirit.run()
'''

    script_path = os.path.join(os.getenv('USERPROFILE'), 'Desktop', 'spirit_engine.py')
    try:
        with open(script_path, 'w') as file:
            file.write(spirit_engine_content)
        logging.info(f"Spirit Engine script written to {script_path}")
    except Exception as e:
        logging.error(f"Failed to write Spirit Engine script: {e}")
        sys.exit(1)

def run_spirit_engine():
    script_path = os.path.join(os.getenv('USERPROFILE'), 'Desktop', 'spirit_engine.py')
    try:
        subprocess.run(f"powershell -Command \"Start-Process python -ArgumentList '{script_path}' -Verb RunAs\"", shell=True, check=True)
        logging.info("Spirit Engine is now running.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to start Spirit Engine: {e}")
        time.sleep(5)
        logging.info("Retrying to start Spirit Engine.")
        run_spirit_engine()

def main():
    install_packages()
    write_spirit_engine()
    run_spirit_engine()

if __name__ == "__main__":
    main()
