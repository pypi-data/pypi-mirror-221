from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=10, thread_name_prefix='quao-lib-')
