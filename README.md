# SC08A
Tools for working with SC08A servo driver.

Up to 8 servo are connected to SC08A driver.
SC08A driver is connected via uart with Raspberry pi.
Raspberry pi get data thru socket using servo.py app.
pc send data to raspberry pi thru socket with two ways: website and client.py app.

web browser -> Django with htmx on apache2 ->{socket}-> Rpi (server) ->{uart}-> SC08A ->{impulses}-> servo.
PC (client) ->{socket}-> Rpi (server) ->{uart}-> SC08A ->{impulses}-> servo.

for error:
ModuleNotFoundError: No module named 'tkinter'
try install python3-tk or python3-tkinter or something similar
