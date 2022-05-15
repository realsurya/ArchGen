import os

class ArchGen:
    def clear(self):
        os.system('clear')

    @staticmethod
    def awaitConf():
        if input("Continue? (y/n): ") != 'y':
            exit

    def __init__(self):
        self.clear()

        print('-----------------------Welcome To ArchGen-----------------------\n')
        print('ArchGen is a simple installer script which creates a minimal\nenvironment with minimal hassle.\n')
        print('Arch Linux is a great way to learn the inner workings of a\nLinux distro. Therefore, it is highly recommended that users\nattempt to install Arch Linux manually at least once using\nthe excellent wiki.\n')
        print('All to say, this script is not a replacement for that learning\nexperience. The target audience are those who understand the\ninstallation process, but don\'t have the energy to redo it.\n')
        self.awaitConf()

    def setNetwork(self):
        self.clear()
        print('-----------------------Network Connection-----------------------\n')
        print('a network connection is required to proceed. If you have already\nconnected via ethernet, you may skip. Otherwise, setup wifi now.')
        if input('Use WiFi? (y/n): ') == 'y':
            os.system('iwctl device list')
            adapter = input('Enter Desired Device Name (ex. wlan0): '')

            confAdapter = 'Use Device "' + adapter + '? (y/n): '
            if input(confAdapter) == 'n':
                adapter = input('Enter Desired Device Name (ex. wlan0): '')

installer = ArchGen()
