def timer1(function):
    def wrapper(t):
        import time     
        start_time = time.time()
        function(t)
        print(f'It takes {time.time() - start_time} seconds')
    return wrapper

class timer2:
    def __init__(self, function):
        self.function = function
        
    def __call__(self, t):
        import time
        start_time = time.time()
        self.function(t)
        print(f'It takes {time.time() - start_time}')

    
@timer1
def AnyFunction(t):
    import time
    time.sleep(t)

AnyFunction(1)

@timer2
def AnyFunction(t):
    import time
    time.sleep(t)
    return 5 

AnyFunction(1)
