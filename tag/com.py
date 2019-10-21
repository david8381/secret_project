import ipscanner as ip
import multiprocessing as mp
import sys, socket

host = ""
port = 1024
buf = 1024
UDPSock = none

def close():
    try:
        UDPSock.close()
    except:
        print "Something went wrong with closing the socket."


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

setup_sock()

def send_message(ip, msg):
    UDPSock.sendto(msg, (ip, port))


def update_ips():
        global ip_list
        ip_list = ipscanner.map_network()
        for x, ip in enumerate(ip_list):
                if ip == my_ip:
                        del ip_list[x]

