# hackrf

## Its the easy way

###  How to run Hack RF?
You need to install many driwers that wosnt work OR you can run Pentoo live CD with all software - but it is not so easy too. Because if you want to work with hack rf try first to get the easy way with live cd:

1) install gnu radio companion
  ```apt install gnuradio```

a) get a 64 version of pentoo or x64 virtual box + x64 penotoo because x86 can not work) 

(https://pentoo.ch/isos/daily-autobuilds/Pentoo_Full_amd64_hardened/)

b) run virtual box as ```sudo``` if you use virtual box

c) connect virtual box usb (devices->USB->GreatScottGadgetsHackRFOne)

d) check ```hackrf_info```

e) run: ```gnuradio-companion```

f) and the most useful - add to osmocom source to Devica arguments this line "soapy=0,driver=hackrf"
