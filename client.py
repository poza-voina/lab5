import socket



def input_numbers():
	def checkNumber(number: str):
		if number.isnumeric():
			number = int(number)
			if (number >= 0 or number <= 255):
				return number
            
		return None

	while True:
		num1 = checkNumber(input("Введите первое число:"))
		if num1:
			break

	while True:
		num2 = checkNumber(input("Введите второе число:"))
		if num2:
			break
        
	return (num1, num2)

def numbers_to_bytes(num1, num2):
	return num1.to_bytes(1, signed=False) + num2.to_bytes(1, signed=False)


def main():
	while True:
		sock = socket.socket()
		sock.connect(('127.0.0.1', 9090))
		numbers = input_numbers()
		sock.send(numbers_to_bytes(*numbers))
		data = sock.recv(2)
		print(int.from_bytes(data, signed=False))
		sock.close()


main()