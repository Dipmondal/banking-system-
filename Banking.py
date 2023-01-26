import os,random,time, pyfiglet

from os import path

if not os.path.exists("banking_system"):

	os.mkdir("banking_system")if os.path.exists("banking_system"):

	os.chdir("banking_system")

	if not os.path.exists("user_data"):

		os.mkdir("user_data")

	if os.path.isdir("user_data"):

		os.chdir("user_data")

print(os.getcwd())	

"""with open(".logo.txt","r") as f:

	logo = f.read()

	f.close()

"""

path = os.getcwd()

logo = pyfiglet.figlet_format("DEEPX BANK")

def pin():

	os.system("clear")

	print(logo,"\n\n")

	print("\t___________________________CHANGE PIN___________________________")

	with open("name.txt","r") as f:

		r_name = f.read()

		f.close()

	with open("mobile_number.txt","r") as f:

		r_mobile = f.read()

		f.close()

	with open("age.txt","r") as f:

		r_age = f.read()

		f.close()

	name = input("enter your name : ")

	mobile = int(input("enter your mobile number : "))

	age = int(input("enter your age : "))

	if name == r_name:

		if mobile== r_mobile:

			if age == r_age:

				with open("pin.txt","w") as f:

					new_pin = int(input("enter your new pin :"))

					if len(new_pin) != 4:

						print("please enter 4 digit number")

						pin()

					f.write()

					f.close()

			else:

				print("age not match!")

		else:

			print("mobile number not match !")

	else:

		print("name not match!")

		pin()

	if input("do you want to Continue y||n : ") == "y":

		pass

	else:

		pin()

def send():

	os.system("clear")

	print(logo,"\n\n")

	print("\t___________________________SEND MONEY___________________________")

	with open("name.txt","r") as n:

		print(f"welcome {n.read()}")

		n.close()

	with open("register.txt","r") as r:

		register = r.read()

		r.close()

	with open("deposit.txt","r") as depo:

		deposited = int(depo.read())

		depo.close()

	if deposited == "0":

		print("insufficient balance! ")

		main()

	print(f"your balance is {deposited}")

	try:

		amount = int(input("Enter amount : "))

		receiver = str(input("account number : "))

	except:

		print("not match!")

	if str(receiver) != str(register):

		os.chdir("..")

		if os.path.isdir(receiver):

			os.chdir(receiver)

			with open("deposit.txt","r") as d:

				recever_money = int(d.read())

				d.close()

			totalr = int(int(amount)+int(recever_money))

			with open("deposit.txt","w") as f1:

				f1.write(str(totalr))

				f1.close()

			os.chdir("..")

			os.chdir(str(register))

			with open("deposit.txt","w") as f2:

				final = int(int(deposited)-int(amount))

				print(f"current balance is {final}")

				f2.write(str(final))

				f2.close()

		else:

			print("account not found")

	else:

		print("please enter valid account !")

		time.sleep(0.4)

		main()

def deposit():

	os.system("clear")

	print(logo,"\n\n")

	#print("\t___________________________DEPOSIT___________________________")

	with open("deposit.txt","r") as depo:

		deposited = depo.read()

		depo.close()

	print(f"your balance is  {deposited}")

	money= str(input("deposit some money : "))

	if len(money)==0:

		print("please enter amount")

	else:

		with open("deposit.txt","w") as depo:

		

			depo.write(money)

			depo.close()

		old = int(deposited)

		new = int(money)

		

		depositeds= old+new

		with open("deposit.txt","w") as depo:

			#money= str(input("deposit some money : "))

			depo.write(str(depositeds))

			depo.close()

		with open("deposit.txt","r") as f:

			balance= f.read()

			f.close()

		print(f"your current balance is {balance}")

	if input("do you want to Continue y||n : ") == "y":

		pass

	else:

		deposit()

def withdraw():

	os.system("clear")

	print(logo,"\n\n")

	print("\t___________________________WITHDRAW___________________________")

	with open("deposit.txt","r") as depo:

		deposited = depo.read()

		depo.close()

	if deposited == "0":

		print("your balance is too low")

		print("please deposit some money")

		main()

	with open("deposit.txt","w") as depo:

		money= str(input("enter your amount : "))

		if len(money) == 0:

			print("please enter valid amount")

			withdrawmai

		depo.write(money)

		depo.close()

	old = int(deposited)

	new = int(money)

	

	depositeds= old-new

	print(f"new balance is {depositeds}")

	with open("deposit.txt","w") as depo:

		#money= str(input("deposit some money : "))

		depo.write(str(depositeds))

	depo.close()

	if input("do you want to Continue y||n : ") == "y":

		pass

	else:

		withdraw()

def check_balance():

	os.system("clear")

	print(logo,"\n\n")

	print("\t___________________________CHECK BALANCE___________________________")

	with open("deposit.txt","r") as f:

		current_money = f.read()

		f.close()

	print(f"your current balance is {current_money}")

	if input("do you want to Continue y||n ") == "y":

		pass

	else:

		check_balance()

def account_number():

	os.system("clear")

	print(logo,"\n\n")

	print("\t___________________________ACCOUNT NUMBER___________________________")

	with open("register.txt","r") as f:

		bl=f.read()

		f.close()

	print(f"your account number : {bl}")

	if input("do you want to Continue y||n ") == "y":

		pass

	else:

		main()

def number():

	os.system("clear")

	print(logo,"\n\n")

	print("\t________________MOBILE NUMBER___________________")

	number = int(input("enter your new mobile number : "))

	with open("mobil.txt","w") as f:

		f.write(number)

		f.close()

	if num[0]=="0":

		with open("mobil.txt","r") as f:

			r_num = f.read()

			f.close()

			if r_num[0] != "0":

				final_num = "0"+num

				with open("mobil.txt","w") as f:

					f.write(final_num)

					f.close()

def main():

	while True:

		os.system("clear")

		print(logo,"\n\n")

		print("\t________________MENU___________________")

		print("1 : Deposit Money")

		print("2 : Withdraw Money")

		print("3 : Send Money")

		print("4 : Check Balance")

		print("5 : Check Account Number")

		print("6 : Change Pin")

		print("7 : change number")

		print("8 : log out")

		choice = input("> ").lower()

		if choice == "1":

			deposit()

		elif choice == "2":

			withdraw()

		elif choice == "3":

			send()

		elif choice == "4":

			check_balance()

		elif choice == "5":

			account_number()

		elif choice == "6":

			pin()

		elif choice == "7":

			number()

		elif choice == "8":

			check_login_or_register()

		else:

			main()

def register():

	global path

	os.system("clear")

	print(logo,"\n\n")

	print("\t___________________________REGISTER___________________________")

#	os.chdir(dir)

	

	try:

		name = input("enter your name : ")

		age = int(input("enter your age : "))

		nasality = input("enter your nasality : ")

		protection= input("enter your profession : ")

		relationship = input("enter your relationship : ")

		source = input("enter your earning source : ")

		mobile = int(input("enter your mobile number : "))

		pin = int(input("enter your pin : "))

	except Exception as ex:

		print(ex)

	a=[]

	for _ in range(0,16):

		data = str(random.randint(1,9))

		a.append(data)

	register_num = "".join(a)

	os.mkdir(register_num)

	mobile_number = str(mobile)

	#os.chdir(path+"/banking_system/uesr_data/"+register_num)

	os.chdir(register_num)

	

	with open("mobile_number.txt","w") as f:

		f.write(str(mobile_number))

		f.close()

	if mobile_number[0] =="0":

		with open("mobile_number.txt","r") as f:

			r_num = f.read()

			f.close()

		if r_num[0] != "0":

			final_num = "0"+r_num

			with open("mobile_number.txt","w") as f:

				f.write(final_num)

				f.close()

	with open("mobile_number.txt","r") as f:

		len_n = f.read()

		f.close()

	Len = len(str(mobile_number))

	check_len_n = len(len_n)

	if Len != check_len_n:

		with open("mobile_number","w") as f:

			f.write(mobil_number)

			f.close()

		if mobil_number[0] =="0":

			with open("mobile_number.txt","r") as f:

				r_num = f.read()

				f.close()

			if r_num[0] != "0":

				final_num = "0"+r_num

				with open("mobile_number.txt","w") as f:

					f.write(final_num)

					f.close()

		

	with open("name.txt","w") as f:

		f.write(name)

		f.close()

	with open("nasality.txt","w") as f:

		f.write(nasality)

		f.close()

	with open("protection.txt","w") as f:

		f.write(protection)

		f.close()

	with open("relationship.txt","w") as f:

		f.write(relationship)

		f.close()

	with open("source.txt","w") as f:

		f.write(source)

		f.close()

	with open("age.txt","w") as f:

		f.write(str(age))

		f.close()

	with open("pin.txt","w") as f:

		f.write(str(pin))

		f.close()

	with open("register.txt","w") as f:

		f.write(str(register_num))

		f.close()

	with open("deposit.txt","w") as depo:

		money= str(input("first deposit some money : "))

		depo.write(money)

		depo.close()

	with open("register.txt","r") as f:

		rgs = f.read()

		f.close()

	print(f"your account number is {rgs}")

	print("please note your account number")

	time.sleep(2)

	os.system("clear")

	print(rgs)

	time.sleep(5)

	main()

def login():

	os.system("clear")

	print(logo,"\n\n")

	print("\t___________________LOGIN___________________")

	#os.chdir(path+"/banking_system/user_data")

	try:

		name = str(input("enter your name : "))

		registers = int(input("enter your account number : "))

		pins = int(input("enter your pin number : "))

	except Exception as ex:

		print(ex)

		login()

	register = str(registers)

	pin = str(pins)

	if len(register) == 16:

		if len(pin) == 4:

			if register.isdigit():

				if pin.isdigit():

					if os.path.isdir(register):

						os.chdir(register)

						with open("name.txt","r") as f:

							account_name = f.read()

							f.close()

						with open("register.txt","r") as f:

							account_register = f.read()

							f.close()

						with open("pin.txt","r") as f:

							account_pin = f.read()

							f.close()

						#print(f"name {account_name} register {account_register} pin{account_pin}")

						if account_name == name:

							if account_register == register:

								if account_pin == pin:

									main()

								else:

									print("pin number is not match !")

									time.sleep(1)

									login()

							else:

								print("register number is not match ! ")

								time.sleep(1)

								login()

						else:

							print("name not match !")

							time.sleep(1)

							login()

					else:

						print("account not exist")

						time.sleep(1)

						check_login_or_register()

				else:

					print("pin is not digit")

					time.sleep(1)

					login()

			else:

				print("register is not digit")

				time.sleep(1)

				login()

		else:

			print("pin number is not 4 digit")

			time.sleep(1)

			login()

	else:

		print("register number is not 16 digit")

		time.sleep(1)

		login()

def check_login_or_register():

	os.system("clear")

	print(logo,"\n\n")

	print("\t___________________LOGIN OR REGISTRATION___________________")

	check= input("1 : Login\n2 : Regieter\n").lower()

	if check == "1":

		print("login")

		login()

	elif check == "2":

		print("register")

		register()

	else:

		check_login_or_register()

check_login_or_register()
