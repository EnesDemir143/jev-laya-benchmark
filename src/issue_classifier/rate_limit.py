from __future__ import annotations

import asyncio
import time


class AsyncRateLimiter:
    """Space request *starts* so they do not exceed `rate` per second.

    Concurrency is a separate cap (semaphore). This limiter is the RPM guard:
    15 req/s stays under the documented 1,200 RPM / 20 req/s ceiling.
    """

    def __init__(self, rate: float) -> None:
        if rate <= 0:
            raise ValueError("rate must be > 0")
        self._interval = 1.0 / rate
        self._lock = asyncio.Lock()
        self._next = 0.0

    async def acquire(self) -> None:
        async with self._lock:
            now = time.monotonic()
            wait = self._next - now
            if wait > 0:
                await asyncio.sleep(wait)
                now = time.monotonic()
            self._next = now + self._interval
