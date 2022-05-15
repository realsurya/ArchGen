import os

class ArchGen:
    def clear(self):
        os.system('clear')

    def __init__(self):
        self.clear()

        print('-----------------------Welcome To ArchGen-----------------------\n')
        print('ArchGen is a simple installer script which creates a minimal\nenvironment with minimal hassle.\n')
        print('Arch Linux is a great way to learn the inner workings of a\nLinux distro. Therefore, it is highly recommended that users\nattempt to install Arch Linux manually at lease once using\nthe excellent wiki.')
        print('All to say, this script is not a replacement for that learning\nexperience. The target audience are those who understand the\ninstallation process, but don\'t have the energy to redo it.')

installer = ArchGen()
