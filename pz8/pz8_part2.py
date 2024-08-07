# -*- coding: utf-8 -*-
# Реализуйте асинхронный метод, который будет отправлять запросы в http://google.com по http
# с ограничением не более 10 запросов в единицу времени.

import aiohttp
import asyncio
import time

max_requests = 10

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def bound_fetch(sem, session, url):
    async with sem:
        return await fetch(session, url)

async def main():
    url = "http://google.com"
    num_requests = 50
    sem = asyncio.Semaphore(max_requests)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            task = asyncio.create_task(bound_fetch(sem, session, url))
            tasks.append(task)
            #print(task)

        start_time = time.time()
        results = await asyncio.gather(*tasks)
        end_time = time.time()

    print(f"Выполнено {num_requests} запросов за {end_time - start_time:.2f} секунды")
    #print(results)


if __name__ == "__main__":
    asyncio.run(main())
#Выполнено 50 запросов за 5.12 секунды