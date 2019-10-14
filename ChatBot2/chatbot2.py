import os, sys, ipscanner, socket
import multiprocessing as mp

def colored(color, text):
        r, g, b = color
        return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)

def clear():
        print("\033[2J")
        print("\033[0;0H")

def close():
	UDPSock.close()
	sys.exit()

print colored((255, 255, 255), "")
clear()

ip_list = []
cmd_list = ['\\commands: See list of commands', '\\exit: Exit Chat Bot V2', '\\online: See online devices', '\\clear: Clear the terminal screen', '\\status: See your name, ip, and port']

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

host = ""
port = int(raw_input("Set a port. Minimum is 1024 unless run as sudo, and the maximum is 65535. Default port is 1024\n>"))
buf = 1024
UDPSock = None

def setup_socket(addr):
	global UDPSock
	UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		UDPSock.bind(addr)
	except Exception as e:
        	print e
		print "Looks like your computer is already using that port, or that port is not permited."
		print "If the port is between the set ranges, try using the following command: `ps -fA | grep python`. If any of the processes show up as `ChatBot2`, try killing the process by running 'kill `process_number`'."
		print "*Replace `process_number` with the second number on the line that has the process you need to kill."
		close()

setup_socket((host, port))

#target_UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_ip = s.getsockname()[0]
s.close()

print("Your IP is {}".format(my_ip))

username = raw_input("What should everyone call you?\n>")
if len(username) < 3:
	print colored(RED, "Username must be greater than 2 characters")
	close()
elif len(username) > 20:
	print colored(RED, "Username cannot be greater than 20 characters")
	close()

def update_ips():
	global ip_list
	ip_list = ipscanner.map_network()
	for x, ip in enumerate(ip_list):
		if ip == my_ip:
			del ip_list[x]


def repeated_update_ips():
	while True:
		update_ips()


def listen():
	while True:
		try:
			received, addr = UDPSock.recvfrom(buf)
			ip, port = addr
			print (received)
		except:
			pass


def send_message(message):
	for ip in ip_list:
		UDPSock.sendto(message, (ip, port))


def main():
        global port
	print ("Scanning network...")
	update_ips()
	print ("Finished!")
	update = mp.Process(target=repeated_update_ips)
	update.start()
	receiving = mp.Process(target=listen)
	receiving.start()
	print("Type a message and hit enter to start. Type \\commands to see commands you can use.")
	send_message(colored(RED, "{} just barged into the chat room.".format(username)))
	while True:
		message = raw_input()
		if message == '\\exit':
			print "Terminating processes..."
			update.terminate()
			update.join()
			receiving.terminate()
			receiving.join()
			send_message(colored(RED, "{} took the L".format(username)))
			break
		elif message == '\\online':
			print (len(ip_list))
		elif message == '\\commands':
			print "---Chat Bot V2 Commands---"
			for cmd in cmd_list:
				print (cmd)
		elif message == '\\clear':
			clear()
		elif message == '\\status':
			print colored(RED, "Your username is {}".format(username))
			print colored(RED, "You IP address is {}".format(my_ip))
			print colored(RED, "You are on port {}".format(port))
		else:
			message = '<' + username + '> ' + message
			message = colored(GREEN, message)
			send_message(message)


try:
	main()
except Exception as e:
	print (e)
finally:
	print "Closing ports..."
	close()
