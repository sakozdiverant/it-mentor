import asyncio
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

async def task1():
    print("1 task run")
    await asyncio.sleep(2)
    print("1 task stop")

async def task2():
    print("2 task run")
    await asyncio.sleep(4)
    print("2 task stop")
@timer
async def main():
    task1_coro = task1()
    task2_coro = task2()

    task1_task = asyncio.create_task(task1_coro)
    task2_task = asyncio.create_task(task2_coro)

    await task1_task
    await task2_task

if __name__ == "__main__":
    asyncio.run(main())