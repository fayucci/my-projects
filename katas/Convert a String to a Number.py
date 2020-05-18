def string_to_number(s):
   return int(s)

assert string_to_number('123') == 123

assert string_to_number('-7') == -7

try: string_to_number('fatima')
except ValueError: assert True
else: assert False, 'deberia arrojar valueError'

try: string_to_number('3.14')
except ValueError: assert True
else: assert False, 'deberia arrojar valueError'

try: string_to_number('')
except ValueError: assert True
else: assert False, 'deberia arrojar valueError'