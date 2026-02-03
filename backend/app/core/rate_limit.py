import time
from typing import Dict


class TokenBucket:
    def __init__(self, rate_per_sec: float, capacity: int) -> None:
        self.rate_per_sec = rate_per_sec
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.time()

    def consume(self, tokens: int = 1) -> bool:
        now = time.time()
        elapsed = now - self.last_refill
        refill = elapsed * self.rate_per_sec
        if refill > 0:
            self.tokens = min(self.capacity, self.tokens + refill)
            self.last_refill = now
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False


_buckets: Dict[str, TokenBucket] = {}


def get_bucket(name: str, rate_per_sec: float, capacity: int) -> TokenBucket:
    if name not in _buckets:
        _buckets[name] = TokenBucket(rate_per_sec=rate_per_sec, capacity=capacity)
    return _buckets[name]
