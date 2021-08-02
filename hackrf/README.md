# hackrf

## Its the easy way

###  How to run Hack RF with gnuradio?

1) install gnu radio companion by:


a)```apt install gnuradio```

b)Install with PyBOMBS from https://github.com/gnuradio/gnuradio

``` 
sudo -H pip3 install PyBOMBS
pybombs auto-config
pybombs recipes add-defaults
pybombs prefix init ~/gnuradio -R gnuradio-default
```
If you have libvolk error
```
/gnuradio/src/libvolk/include/volk/volk_common.h:153:24: error: ‘isinf’ was not declared in this scope
```
And set isinf to 0


c) get a 64 version of pentoo or x64 virtual box + x64 penotoo because x86 will not work. Run virtual box as ```sudo``` if you use virtual box
(https://pentoo.ch/isos/daily-autobuilds/Pentoo_Full_amd64_hardened/)




2) Run: ```gnuradio-companion```

a) connect virtual box usb (devices->USB->GreatScottGadgetsHackRFOne)

b) check ```hackrf_info```

c) and the most useful - add to osmocom source to Devica arguments this line ``` "soapy=0,driver=hackrf"  ```


