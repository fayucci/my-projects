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
def every_digit_is_odd(dni):
    generator = (int(dig) % 2 == 1 for dig in dni)
    return all(generator)

@benchmark
@benchmark
def every_digit_is_odd_2(dni):
    generator = [int(dig) % 2 == 1 for dig in dni]
    return all(generator)

new_function = benchmark(every_digit_is_odd_2)


#print(every_digit_is_odd('132364875'))
#print(every_digit_is_odd('1357995'))
##1print(every_digit_is_odd(''))

#map(lambda dig: int(dig) % 2 == 1, dni)

numbers = [str(x) for x in range(10000000)]

text_str = ''.join(numbers)

print(every_digit_is_odd(text_str))
print(every_digit_is_odd_2(text_str))