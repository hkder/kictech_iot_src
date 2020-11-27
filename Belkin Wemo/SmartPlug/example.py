import pywemo


def main():
    # discover wemo devices
    devices = pywemo.discover_devices()
    print(devices)

    device = devices[0]
    url = 'http://'+device.deviceinfo.hostname+'/setup.xml'
    mac = device.mac

    # Instantiate Pywemo Switch
    switch = pywemo.Switch(url=url, mac=mac)

    # Turn on Switch
    switch.on()

    # Turn off Switch
    # switch.off()


if __name__ == '__main__':
    main()
