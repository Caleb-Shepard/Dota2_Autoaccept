# Alexa_Auto_Accept_Dota2
Welcome to *Alexa Auto-Accept Dota2*, this is a new skill for Alexa that allows her to be interacted with via voice commands to accept or decline a que pop-up for Dota 2. <br />

# Installation

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

# Prerequisites
Amazon's [Alexa](https://www.amazon.com/b/?ie=UTF8&node=9818047011&tag=mh0b-20&hvadid=77721756043382&hvqmt=e&hvbmt=be&hvdev=c&ref=pd_sl_iwlt1gvek_e) <br />
2 GB RAM <br />
30 MB  

# Voice Commands
"Alexa, accept que." <br />
"Alexa, decline que."


# Donations
Help support future releases of *Alexa Auto-Accept Dota2* <br />
[Paypal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&token=-wONNamGPhHApp9KQZNCSqdIwCCSm3WLA9NjDXQpHAuNpTFeHe4VU0s9Rma)

# Version 0.4.0 - Beta
Initial Release - 10/07/2017 <br />
Current Release - 10/08/2017

# Authors
[Caleb Shepard](https://github.com/Caleb-Shepard) <br />
[Andy Shepard](https://github.com/Andrew-Shepard) <br />
[Derek Donahue](https://www.facebook.com/derek.donahue.94) <br />
[Tiger Sachse](https://github.com/tgsachse)

# License
MIT License
