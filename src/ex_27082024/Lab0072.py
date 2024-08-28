import time


def time_decor(func):

    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"Time taken by function {end_time - start_time}")
    return wrapper()
@time_decor
def test_ui_1():
    print("Add function , time taken by this function")
    time.sleep(2)

    
@time_decor
def test_ui_2():
    print("Add function , time taken by this function")
    time.sleep(5)
