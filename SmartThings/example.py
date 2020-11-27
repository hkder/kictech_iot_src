import aiohttp
import asyncio
import pysmartthings

from const import (
    PERSONAL_ACCESS_TOKEN
)


async def main(token):
    session = aiohttp.ClientSession()
    # async with aiohttp.ClientSession() as session:
    api = pysmartthings.Api(session, token)

    # Gets the list of devices connected to the PAT
    devices = await api.get_devices()
    device = devices[1]

    # An example of posting commands to a registered device
    # Documentation of Commands are available at https://smartthings.developer.samsung.com/docs/api-ref/st-api.html#section/Overview
    # Capabilities Documentation can be found at https://smartthings.developer.samsung.com/docs/api-ref/capabilities.html
    deviceid = device['deviceId']
    capabilities = device['components'][0]['capabilities']
    switch_capability = 'switch'
    component_id = device['components'][0]['id']
    command = 'off'
    status = await api.get_device_status(deviceid)

    res = await api.post_device_command(deviceid, component_id, switch_capability, command, None)
    print(res)

    # res = await api.post_device_command(deviceid, component_id, 'fanSpeed', 'setFanSpeed', [2])
    # print(res)

    await session.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(PERSONAL_ACCESS_TOKEN))
