def string_numbers_till_n(n):
  str = "0"
  for i in range(n):
    str = str + " " + (i+1)
  return str

print(string_numbers_till_n(5))
