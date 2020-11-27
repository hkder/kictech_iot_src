from aqman import AqmanUser, AqmanDevice
from aqman import UserInfo, Device
import asyncio
from const import ID, PASSWORD


async def main():
    """Show example on controlling your AQMAN101"""
    devices = []

    async with AqmanUser(ID, PASSWORD) as aqmanuser:
        info: UserInfo = await aqmanuser.devices_info()
        print(info)
        devices = info.devices

    for device in devices:
        async with AqmanDevice(ID, PASSWORD, device) as aqmandevice:
            device: Device = await aqmandevice.state()
            print(device)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
