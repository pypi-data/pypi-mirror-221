def seconds_count(function):
    def wrapper(*args, **kwargs):

        import time

        start = time.time()
        respone = function(*args, **kwargs)
        elapsed_time = time.time() - start
        print(f">>> {elapsed_time:.10f}")
        return respone 

    return wrapper