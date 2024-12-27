# Representation numbers on decimal system:

# Conversion to binary base from decimal base in low code

def binary_to_decimal(array_binary):
  soma = 0
  for i in range(len(array_binary)):
    val = array_binary[i]*(2**(((len(array_binary))-(i+1))))
    soma+=val
  return soma
 


def start_program():
   user_input = input("\nEnter a binary string that i will convert to decimal.\n:")  
   decimal_response = check_user_input(user_input)
   print(f"\nThe number entered {user_input} in decimal base is: {decimal_response}")
  
def check_user_input(input):
  try:
    val = int(input)
    binary = str(input)
    array_binary = list(map(int, binary))
    if all(b in [0, 1] for b in array_binary):
      return binary_to_decimal(array_binary)
  except ValueError:
    try:
      val = float(input)
      print("No.. Input is not a binary. It's a float number = ", val)
    except ValueError:
      print("No.. input is not a binary. It's a string = ", input)

if __name__ == "__main__":
  start_program()