def string_numbers_till_n(n):
  string_var = "0"
  for i in range(n):
    string_var = string_var + " " + str(i+1)
  return string_var

print(string_numbers_till_n(5))
