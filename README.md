# Playwright Python automation and browser automation scripts

This repository provides Playwright Python automation benchmarks and browser automation scripts comparing synchronous and asynchronous execution models. The repository also includes baseline concurrency examples for web scraping with Playwright and Selenium.

## Architecture

The project has two directories containing nine Python scripts:

Root scripts test browser performance across two target URLs (`https://playwright.dev/python/docs/library` and `http://playwright.dev`):
- `del.py`: Spawns two threads with Python `threading.Thread`. Each thread launches Firefox via `selenium.webdriver.Firefox()`, loads one target URL, prints the page title, prints the thread execution time, and closes the browser.
- `del2.py`: Spawns two threads with Python `threading.Thread`. Each thread launches Chromium in headed mode with `sync_playwright()`, loads one target URL, prints the page title, prints elapsed time, and closes the browser.
- `getting started.py`: Runs an asynchronous event loop with Python `asyncio`. The script uses `async_playwright()` to launch Chromium in headed mode and executes two tasks concurrently with `asyncio.gather()`, printing titles and execution times.

Prerequisite scripts in `prerequisites/` demonstrate Python concurrency mechanics:
- `prerequisites/async.py`: Runs coroutines with `asyncio.run()`, `asyncio.gather()`, and non-blocking `asyncio.sleep(2)`.
- `prerequisites/decorators.py`: Implements a wrapper decorator around a target function.
- `prerequisites/event loop.py`: Spawns two threads where each thread creates an independent event loop with `asyncio.new_event_loop()` and consumes values from a generator yielding integers 1 to 4.
- `prerequisites/future.py`: Manages an `asyncio.Future` across two coroutines, resolving the future after a 3 second delay.
- `prerequisites/generative functions.py`: Defines a generator function that yields sequential integers starting from 0.
- `prerequisites/sync.py`: Measures execution time for three sequential calls to a blocking function with two 1-second `time.sleep` calls, totaling 6 seconds of sleep.

## Setup

1. Install Python 3.7 or newer.
2. Install the required Python packages:
   ```bash
   pip install playwright selenium
   ```
3. Install the Playwright Chromium browser binary:
   ```bash
   playwright install chromium
   ```
4. For Selenium Firefox execution in `del.py`, install Firefox and place `geckodriver` in your system PATH.

## Usage

Run the browser automation scripts from the repository root:

```bash
python3 del.py
python3 del2.py
python3 "getting started.py"
```

Run the concurrency prerequisite scripts:

```bash
python3 prerequisites/async.py
python3 prerequisites/decorators.py
python3 "prerequisites/event loop.py"
python3 prerequisites/future.py
python3 "prerequisites/generative functions.py"
python3 prerequisites/sync.py
```

## Configuration

The scripts use hardcoded values in the source code:
- Browser display mode: `del2.py` line 7 and `getting started.py` line 8 set `headless=False`. Set `headless=True` to run Chromium in headless mode.
- Target URLs: `del.py`, `del2.py`, and `getting started.py` pass `"https://playwright.dev/python/docs/library"` and `"http://playwright.dev"` as arguments. Change these string arguments to test different websites.
