#Claculator App
import math

print("         ==Basic Calcultor==\n\n")

def feature():
	
	print('💠 Choose the operation:\n------------------')
	print("'+' --(1)\n'-' --(2)\n'*' --(3)\n'÷' --(4)\n'^'(exponential) --(5)\n'√'(Sqare_root) --(6)\n'Trigonometric_ratio' --(7)\n'Exit' --(e)\n------------------")
	return
	
while True:
	feature()
	choose = input('\n: ')
	
#Addition
	
	if choose == '1':
		add1 = input('\n◽Enter the 1st number:')
		add2 = input('◽Enter the 2nd number:')
		if not add1 or not add2:
			print('Please enter a number.')
		else:
			print(f"\n◽ {add1} + {add2} = {int(add1) + int(add2)}\n------------------\n\n")
			
#Substraction

	elif choose == '2':
		sub1 = input('\n◽Enter the 1st number:')
		sub2 = input('◽Enter the 2nd number:')
		if not sub1 or not sub2:
			print('Please enter a number.')
		else:
			print(f"\n◽ {sub1} - {sub2} = {int(sub1) - int(sub2)}\n------------------\n\n")
			
#Multiplication

	elif choose == '3':
		mul1 = input('\n◽Enter the 1st number:')
		mul2 = input('◽Enter the 2nd number:')
		if not mul1 or not mul2:
			print('Please enter a number.')
		else:
			print(f"\n◽ {mul1} × {mul2} = {int(mul1) * int(mul2)}\n------------------\n\n")
			
#Division

	elif choose == '4':
		div1 = input('\n◽Enter the 1st number:')
		div2 = input('◽Enter the 2nd number:')
		if not div1 or not div2:
			print('Please enter a number.')
		else:
			print(f"\n◽ {div1} ÷ {div2} = {float(div1) / float(div2)}\n------------------\n\n")
			
#Exponention

	elif choose == '5':
		exp1 = input('\n◽Enter the 1st number:')
		exp2 = input('◽Enter the 2nd number:')
		if not exp1 or not exp2:
			print('Please enter a number.')
		else:
			print(f"\n◽ {exp1} ∧ {exp2} = {int(exp1) ** int(exp2)}\n------------------\n\n")
			
#Square Roots

	elif choose == '6':
		sqrt_num = int(input('\n◽Enter the number:'))
		print(f"\n◽Square root of {sqrt_num} : {math.sqrt(sqrt_num)}\n------------------\n\n")
		
#Trigonometric Ratios(sin, cos, tan)

	elif choose == '7':
		tri_ang = int(input('\n◽Enter a valid angle:'))
		ratio_choice = input(f"\n◽Choose ratio:\n\n◽sin(s)\n◽cos(c)\n◽tan(t)\n◽or type 'all' for all trigonometric values of the angle {tri_ang}\n:")
		if ratio_choice == 's':
			print(f"\n◽sin{tri_ang} = {math.sin(tri_ang)}\n------------------\n\n") 
		
		elif ratio_choice == 'c':
			 print(f"\n◽cos{tri_ang} = {math.cos(tri_ang)}\n------------------\n\n")
		
		elif ratio_choice == 't':
			 print(f"\n◽tan{tri_ang} = {math.tan(tri_ang)}\n------------------\n\n")
				 
		elif ratio_choice == 'all':
			
			print(f'\n◽sin{tri_ang} = {math.sin(tri_ang)}\n◽cos{tri_ang} = {math.cos(tri_ang)}\n◽tan{tri_ang} = {math.tan(tri_ang)}\n------------------\n\n')
			
#Exit the programme

	elif choose == 'e':
			 print(f'\nQuitting...')
			 break
			 
			 
		
	

