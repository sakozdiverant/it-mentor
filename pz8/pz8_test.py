import pytest
import os
import aiohttp
import asyncio
from pz8_part1 import find_divisors, create_file
from pz8_part2 import fetch, bound_fetch, main, max_requests


def test_find_divisors():
    assert find_divisors(1) == [1]
    assert find_divisors(6) == [1, 2, 3, 6]
    assert find_divisors(15) == [1, 3, 5, 15]
    assert find_divisors(28) == [1, 2, 4, 7, 14, 28]


@pytest.mark.parametrize("index", range(1, 11))
def test_create_file(index):
    filename = f'file_{index}.txt'
    if os.path.exists(filename):
        os.remove(filename)
    create_file(index)
    assert os.path.isfile(filename)
    with open(filename, 'r') as f:
        content = f.read()
        assert content == str(index)
    os.remove(filename)



@pytest.mark.asyncio
async def test_fetch():
    url = "http://example.com"
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, url)
        assert "Example Domain" in response

@pytest.mark.asyncio
async def test_bound_fetch():
    url = "http://example.com"
    sem = asyncio.Semaphore(max_requests)
    async with aiohttp.ClientSession() as session:
        response = await bound_fetch(sem, session, url)
        assert "Example Domain" in response

@pytest.mark.asyncio
async def test_main():
    url = "http://example.com"
    num_requests = 5
    sem = asyncio.Semaphore(max_requests)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            task = asyncio.create_task(bound_fetch(sem, session, url))
            tasks.append(task)

        start_time = time.time()
        results = await asyncio.gather(*tasks)
        end_time = time.time()

    assert len(results) == num_requests
    for result in results:
        assert "Example Domain" in result

    print(f"Выполнено {num_requests} запросов за {end_time - start_time:.2f} секунды")

