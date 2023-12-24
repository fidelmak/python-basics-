##  Asynchronous programming in Python


Asynchronous programming in Python allows you to write concurrent code that is efficient and non-blocking. The `asyncio` module in Python provides a framework for writing asynchronous programs. Asynchronous programming is particularly useful for tasks that involve waiting for external resources, such as I/O operations or network requests.

Here's a brief explanation with examples to get you started with asynchronous programming in Python:

### 1. Basic Asynchronous Function:

Define an asynchronous function using the `async def` syntax. To perform asynchronous operations, use `await` inside the function.

```python
import asyncio

async def async_function():
    print("Start asynchronous function")
    await asyncio.sleep(2)  # Simulate an asynchronous operation (e.g., I/O or network)
    print("End asynchronous function")

# Run the asynchronous function
asyncio.run(async_function())
```

### 2. Multiple Asynchronous Functions:

Run multiple asynchronous functions concurrently using `asyncio.gather()`.

```python
import asyncio

async def async_function_1():
    print("Async Function 1")

async def async_function_2():
    print("Async Function 2")

async def main():
    await asyncio.gather(async_function_1(), async_function_2())

# Run the main asynchronous function
asyncio.run(main())
```

### 3. Asynchronous I/O Operations:

Asynchronous programming is beneficial for I/O-bound tasks. The following example simulates multiple I/O operations concurrently.

```python
import asyncio

async def fetch_data(url):
    print(f"Fetching data from {url}")
    await asyncio.sleep(2)  # Simulate fetching data from a URL
    print(f"Data fetched from {url}")

async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    await asyncio.gather(*(fetch_data(url) for url in urls))

# Run the main asynchronous function
asyncio.run(main())
```

### 4. Asynchronous with `async with`:

Use the `async with` statement for asynchronous resource management.

```python
import asyncio

class AsyncResource:
    async def __aenter__(self):
        print("Entering asynchronous context")
        await asyncio.sleep(2)  # Simulate entering an asynchronous context

    async def __aexit__(self, exc_type, exc, tb):
        print("Exiting asynchronous context")

async def main():
    async with AsyncResource():
        print("Inside asynchronous context")

# Run the main asynchronous function
asyncio.run(main())
```

### 5. Asynchronous with `async for`:

Use the `async for` statement for asynchronous iteration.

```python
import asyncio

async def async_iterator():
    for i in range(5):
        yield i
        await asyncio.sleep(1)  # Simulate asynchronous iteration delay

async def main():
    async for value in async_iterator():
        print(f"Received: {value}")

# Run the main asynchronous function
asyncio.run(main())
```

These examples demonstrate the basic concepts of asynchronous programming in Python using `asyncio`. Asynchronous programming becomes more powerful when dealing with concurrent tasks, especially those involving I/O operations or network requests.
