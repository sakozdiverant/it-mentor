import json
import os
import asyncio
from ping3 import ping

def load_addresses(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_addresses(file_path, addresses):
    with open(file_path, 'w') as file:
        json.dump(addresses, file, indent=4)

async def async_ping(address):
    response = await asyncio.to_thread(ping, address, timeout=2)
    return address if response is not None else None

async def ping_addresses(addresses):
    tasks = [async_ping(address) for address in addresses]
    results = await asyncio.gather(*tasks)
    return [address for address in results if address]

def compare_addresses(old_addresses, new_addresses):
    new_alive = list(set(new_addresses) - set(old_addresses))
    disappeared = list(set(old_addresses) - set(new_addresses))
    return new_alive, disappeared

async def main():
    file_path = 'addresses.json'
    addresses_to_ping = [f'192.168.1.{i}' for i in range(1, 256)]

    old_alive_addresses = load_addresses(file_path)
    new_alive_addresses = await ping_addresses(addresses_to_ping)

    if old_alive_addresses:
        new_alive, disappeared = compare_addresses(old_alive_addresses, new_alive_addresses)
        print(f"New alive addresses: {new_alive}")
        print(f"Disappeared addresses: {disappeared}")
    else:
        print("First run. Saving initial alive addresses.")

    save_addresses(file_path, new_alive_addresses)

if __name__ == "__main__":
    asyncio.run(main())
