# Dota2_Autoaccept

Requires wmctrl xdotool python-dbus and inotify-send (this is required for dota to send a desktop notification)


For Debian based distros:
sudo apt-get install wmctrl xdotool python-dbus inotify-send

For Mac OS and OSX
```
# requires homebrew, install python-dbus
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
brew install dbus-glib
pip install dbus-python
pip install gi
```

For python3 you also need python3-gi
