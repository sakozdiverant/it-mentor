import pytest
import aiohttp
import asyncio
import os
import time
from pz8_part3 import fetch, bound_fetch, main, max_requests


@pytest.mark.asyncio
async def test_fetch():
    url = "https://example.com/"
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, url)
        assert "Example Domain" in response


@pytest.mark.asyncio
async def test_bound_fetch():
    url = "https://example.com/"
    sem = asyncio.Semaphore(max_requests)
    async with aiohttp.ClientSession() as session:
        response = await bound_fetch(sem, session, url)
        assert "Example Domain" in response


@pytest.mark.asyncio
async def test_main():
    output_file = 'test_response_statuses.txt'
    if os.path.exists(output_file):
        os.remove(output_file)

    await main(output_file=output_file)
    assert os.path.isfile(output_file)


    with open(output_file, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 50
        for line in lines:
            assert "Example Domain" in line
    os.remove(output_file)
