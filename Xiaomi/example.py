from miio import Vacuum

# Fin IP using Xiaomi App
IP = ''
# Find Token using Xiaomi App
TOKEN = ''


if __name__ == '__main__':
    vac = Vacuum(IP, TOKEN)
    vac.start()
