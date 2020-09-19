def digit_sum(n):
  if (n>0):
    return int(n%10 +digit_sum(n//10));
  else:
    return int(n)

def run():
  n= int(input("Enter an int: "));
  print(f"sum of digits of {n} is {digit_sum(n)}.")

if __name__ == "__main__":
  run()