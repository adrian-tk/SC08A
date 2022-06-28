# SC08A
Tools for working with SC08A servo driver.

Up to 8 servo are connected to SC08A driver.
SC08A driver is connected via uart with Raspberry pi.
Raspberry pi get data thru socket using servo.py app.
pc send data to raspberry pi thru socket with client.py app.

PC (client) ->{socket}-> Rpi (server) ->{uart}-> SC08A ->{impulses}-> servo.

for error:
ModuleNotFoundError: No module named 'tkinter'
try install python3-tk or python3-tkinter or something similar
