
def is_divisible_by(number, divisor):
  return number % divisor == 0
  
def says(number):
  if is_divisible_by(number, 15):
    return 'fizzbuzz'
  if is_divisible_by(number, 3):
    return 'fizz'
  if is_divisible_by(number, 5):
    return 'buzz'