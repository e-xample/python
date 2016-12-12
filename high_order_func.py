# using: utf-8

def print_func(func):
  print func('foo', 'bar')

def gen_hello(a, b):
  return 'hello' + a + b

def gen_world(a, b):
  return 'world' + a + b

def main():
  print_func(gen_hello)
  print_func(gen_world)

if __name__ == '__main__':
  main()
