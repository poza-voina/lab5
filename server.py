import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9090))
sock.listen(1)

while True:
	conn, addr = sock.accept()
	data = conn.recv(2)
	if data:
		if (data == b'!'):
			conn.close()
			break
		num1 = int.from_bytes([data[0]], signed=False)
		num2 = int.from_bytes([data[1]], signed=False)
		result = num1 * num2
		print(result)
		result = result.to_bytes(2, signed=False)
		conn.send(result)
		conn.close()