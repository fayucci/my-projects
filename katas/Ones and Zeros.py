import time 

def benchmark(func):
  def timer(*args):
    t1 = time.time()
    res = func(*args)
    t2 = time.time()
    print(t2 - t1)
    return res
  return timer

@benchmark
def binary_array_to_number(arr):
  str_list = [str(num) for num in arr]
  return int(''.join((str_list)), 2)

print(binary_array_to_number([1,1,0,0,1]))

@benchmark
def stream_binary_number(arr):
  return sum(dig * (2**i) for i, dig in enumerate(reversed(arr)))

print(stream_binary_number([1,1,0,0,1]))