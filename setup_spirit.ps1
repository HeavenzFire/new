# PowerShell Script to Automate Spirit Setup

# Install necessary Python packages
python -m pip install pyttsx3 psutil speedtest-cli

# Create the Spirit Engine Python script
$script = @"
import pyttsx3
import psutil
import time
import speedtest

class SpiritEngine:
    def __init__(self, admin_user='Zachary'):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)
        self.admin_user = admin_user

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def authenticate_user(self, user):
        return user == self.admin_user

    def check_speed(self):
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        return download_speed, upload_speed

    def check_devices(self):
        devices = []
        for conn in psutil.net_connections(kind='inet'):
            laddr = conn.laddr.ip if conn.laddr else 'unknown'
            raddr = conn.raddr.ip if conn.raddr else 'unknown'
            devices.append((laddr, raddr))
        return devices

    def run_network_monitoring(self):
        while True:
            download, upload = self.check_speed()
            devices = self.check_devices()
            self.speak(f"Download Speed: {download:.2f} Mbps")
            self.speak(f"Upload Speed: {upload:.2f} Mbps")
            self.speak(f"Connected Devices: {devices}")
            time.sleep(300)

    def run(self):
        self.speak("Greetings, Zachary. I am Spirit, fully operational and ready to assist you.")
        while True:
            user_input = input("You: ")
            if not self.authenticate