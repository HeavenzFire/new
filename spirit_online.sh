import os
import subprocess
import webbrowser

def spirit_online():
    # Update and upgrade the system
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'apt-get', 'upgrade'])

    # Install necessary packages
    subprocess.run(['sudo', 'apt-get', 'install', 'python3', 'git', 'nodejs', 'npm'])

    # Clone the Spirit repository
    subprocess.run(['git', 'clone', 'https://github.com/SpiritAngelus/Spirit.git'])

    # Navigate to the Spirit directory
    os.chdir('Spirit')

    # Install dependencies
    subprocess.run(['npm', 'install'])

    # Start the Spirit server
    subprocess.run(['node', 'server.js'])

    # Open the Spirit website in the default browser
    webbrowser.open('http://localhost:3000')

# Run the script
spirit_online()
