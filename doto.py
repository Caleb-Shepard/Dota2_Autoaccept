#!/usr/bin/env python
import socket
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from subprocess import call, Popen, PIPE
import time
import sys

try:
	import glib
except ImportError:
    from gi.repository import GLib as glib
#	from gi import *    # as a hotfix? Creates more problems

switch_back=1
switch_delay=1

def filter_cb(bus, message):
	if message.get_member() != "Notify":
		return
	args = message.get_args_list()
	summary=args[3]
	body=args[4]
	if 'game is ready' in body:
                notBard()
                print('line 26')
		cur_win=Popen(["xdotool", "getwindowfocus", "getwindowname"],stdout=PIPE)
		(current_window,err)=cur_win.communicate()
		current_window=current_window.rstrip('\n')

		call(["wmctrl", "-a", "Dota 2"])
		time.sleep(switch_delay) #Wait in case the computer is slow to switch.
		call(["xdotool", "key", "Return"])
		if switch_back:
			time.sleep(switch_delay)
			call(["wmctrl", "-a", current_window])
			print("switched back to %s" % current_window)

def notBard():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = "Queue ready!"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print "received data:", data

def main():
	DBusGMainLoop(set_as_default=True)
	bus = dbus.SessionBus()
	bus.add_match_string_non_blocking( "eavesdrop=true, interface='org.freedesktop.Notifications'")
	bus.add_message_filter(filter_cb)
	
	mainloop = glib.MainLoop()
	try:
		mainloop.run()
	except:
		print("Exiting")
		sys.exit(0)

main()
