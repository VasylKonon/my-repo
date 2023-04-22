def retry(max_retries, exc):
    def decorator(func):
        def inner(*args, **kwargs):
            retries = 0
            while max_retries >= retries:
                try:
                    return func(*args, *kwargs)
                except Exception:
                    retries += 1
                    if retries > max_retries:
                        raise exc
        return inner
    return decorator
