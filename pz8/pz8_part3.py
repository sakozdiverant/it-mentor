# -*- coding: utf-8 -*-
# Написать асинхронный код, который делает 50 get запросов к
# https://example.com/ . Записать все статусы ответов в файл и убедиться, что
# количество запросов соответствует заданному количеству. Необходимо учесть,
# чтобы одновременно выполнялось не больше 10 запросов. Для выполнения запросов
# использовать библиотеку aiohttp. Все значения, количество запросов, лимит одновременно
# выполняемых запросов и url должны передаваться как параметры.

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

async def main(output_file='response_statuses.txt'):
    url = "https://example.com/"
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

        with open(output_file, 'w') as f:
            for status in results:
                f.write(f'{status}\n')

    print(f"Выполнено {num_requests} запросов за {end_time - start_time:.2f} секунды")
    print(f"Результат сохранен в {output_file}")
    #print(results)

if __name__ == "__main__":
    asyncio.run(main())
