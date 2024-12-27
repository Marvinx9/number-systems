# Representation numbers on binary system:

# Conversion to decimal base from binary base in low code

def start_program():
  user_input = input("\nEnter a decimal integer that i will convert to binary.\n:")  
  binary_result = check_user_input(user_input)
  
  print(f"\nThe number entered {user_input} in binary base is: {binary_result}")
  
def check_user_input(input):
  try:
    val = int(input)
    return decimal_to_binary(val)
  except ValueError:
    try:
      val = float(input)
      print("No.. Input is not a number. It's a float number = ", val)
    except ValueError:
      print("No.. input is not a number. It's a string = ", input)

def decimal_to_binary(val):
  if val == 0:
    return "0"
  binary = []
  
  while val > 0:
    remainder = val % 2
    binary.append(str(remainder))
    val = val // 2
  if len(binary) is not None:
    binary.reverse()
    return ''.join(binary)
  else:
    return

if __name__ == "__main__":
  start_program()