import asyncio
import aiohttp
import time
import os

from aiohue.discovery import discover_nupnp


def read_username():
    with open(os.path.join(os.getcwd(), "USERNAME"), "r") as f:
        username = f.readline()

    return username


async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)


async def run(websession: aiohttp.ClientSession):
    bridges = await discover_nupnp(websession)

    bridge = bridges[0]

    # Need to press the hue bridge button to create user
    username = read_username()
    if username == '':
        print('Press Button on Phillips Hue Bridge. Waiting for 3 seconds...')
        time.sleep(3)
        username = await bridge.create_user('kictech')
        print(f'User Created: {username}')

        with open(os.path.join(os.getcwd(), "USERNAME"), "w") as f:
            f.write(username)
    else:
        bridge.username = username

    # Initialize Bridge
    await bridge.initialize()

    # Use Light Object
    assert len(bridge.lights._items) == 1
    for lightid in bridge.lights:
        light = bridge.lights[lightid]

    # print the state of the light Object
    print(light.state)

    # Turn on the light Object
    await light.set_state(on=not light.state['on'])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
