import ipscanner as ip
import multiprocessing as mp
import sys, socket

def close():
    try:
        UDPSock.close()
    except:
        print "Something went wrong with closing the socket."
        
