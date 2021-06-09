# APRS Call
 Simple application that creates a JS8Call ready string to send to the APRS network.
 
 ![Alt text](pic.PNG?raw=true "Title")

There are already a few applications for this purpose minaly:
https://github.com/m0iax/js8call_aprsmessaging_interface

What I wanted to provide however, was a more simple approach.
Instead of having more dependancies and relying on JS8Call not breaking the apllication between updates, I've broke the ocnnection between the two.
The user just needs to copy the text from APRSCall into JS8Call and hit send.

What can it send?
SMS, EMAIL, GRID, and Direct APRS Message.

How to run:
Simply install python, and run the application with "python main.py" in either windows or linux.

If you are on windows, installing python isn't even nessisary as I've provided a binary in the "dist" folder.
This is to make things as easy as possible.
