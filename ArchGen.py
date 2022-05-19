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
        self.setNetwork()

    def setNetwork(self):
        self.clear()
        print('-----------------------Network Connection-----------------------\n')
        print('A network connection is required to proceed. If you have already\nconnected via ethernet, you may skip. Otherwise, setup wifi now.\n')
        if input('Use WiFi? (y/n): ') == 'y':
            os.system('iwctl device list')
            adapter = input('Enter desired device name (ex. wlan0): ')

            confAdapter = 'Use Device "' + adapter + '? (y/n): '
            while input(confAdapter) == 'n':
                adapter = input('Enter Desired Device Name (ex. wlan0): ')
                confAdapter = 'Use device "' + adapter + '? (y/n): '

            scanCmd = 'iwctl station ' + adapter + ' scan'
            os.system(scanCmd)
            listCmd = 'iwctl station ' + adapter + ' get-networks'
            os.system(listCmd)

            ssid = input('Enter SSID of desired network: ')
            confSSID = 'Connect to ' + ssid + ' ? (y/n)'
            while input(sonfSSID) != 'y'
                ssid = input('Enter SSID of desired network: ')
                confSSID = 'Connect to ' + ssid + ' ? (y/n)'

            connectCmd = 'iwctl station ' + adapter + ' connect ' + SSID
            os.system(connectCmd)

    def sysClock(self):
        self.clear()
        print('-----------------------Updating Sys Clock-----------------------\n')
        os.system('timedatectl set-ntp true')

    def diskPart(self):
        self.clear()
        print('-----------------------Partitioning Disks-----------------------\n')
        print('The suggested partition structure is:\n- (p1) EFI Partition (512M - type EFI System)\m- (p2) Root partition (2emaining space)\nNOTE: Swap is not needed.\n')
        self.awaitConf()

        os.system('fdisk -l')
        disk = input("Enter disk to partition (ex. /dev/sda)")




installer = ArchGen()
