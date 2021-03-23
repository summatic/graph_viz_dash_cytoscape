class RQueue:
    """

    Code snippet from https://m.blog.naver.com/wideeyed/221370229153
    """

    def __init__(self, name, conn):
        self.key = name
        self.redis = conn

    @property
    def size(self):
        return self.redis.llen(self.key)

    def is_empty(self):
        return self.size == 0

    def put(self, element):
        self.redis.lpush(self.key, element)

    def get(self, timeout=None):
        _, element_value = self.redis.brpop(self.key, timeout=timeout)
        return element_value

    def inquire(self):
        """Get element without pop"""
        if self.is_empty():
            return None

        return self.redis.lindex(self.key, -1)
