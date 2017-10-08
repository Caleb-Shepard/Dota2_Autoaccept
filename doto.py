#!/usr/bin/env python
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
