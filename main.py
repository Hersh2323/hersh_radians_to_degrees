import math
pi_var = math.pi
pi_var_print = str(pi_var)
#print('Using pi value of: ' + pi_var_print)

# converts desired input from radians to degrees from user input
print('executing main.py')

while True:
    try:
        radians_input = float(input("Please enter radians to convert to degrees: "))
    except ValueError:
        print("USER INPUT ERROR: Please enter a floating point number.")
        continue
    else:
        break

radians_input_str = str(radians_input)
#print('Attempting to convert ' + radians_input_str + ' radians to degrees . . .')

pre_math = 180/pi_var
#print('pre_math: ' + str(pre_math))
solved_degrees = radians_input*pre_math
print(radians_input_str + ' radians is equal to: ' + str(solved_degrees) + ' degrees')