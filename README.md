Project: Microbits by Peter Hammar

This is a program that collects data with microbits and creates a suitable web-based interface that displays your room and the sensors
in 2D as well as the data collected.

Softwares needed:

Python

SQL

an IDE (I used VSCode for this program)

Libraries needed:

flask

serial.tools.list_ports

mysql.connector

serial

You can install these libraries using pip with the following command in the command line:
pip install package-name

Setting up:

1. Connect a microbit to the USB-port on your computer. 
2. Go to the folder called 'hexfiles'
3. Drag 'receiver.hex' to your microbit-folder, like you would with any USB-connected device.
4. Wait until the file transfer is complete. 
5. Remember which microbit you used for the receiver-file.
6. Disconnect the microbit from the USB-port
7. Connect another microbit to the USB-port
8. In the 'hexfiles'-folder drag senderA.hex to your microbit-folder
9. Wait until the file transfer is complete.
10. Disconnect the microbit from the USB-port
11. Repeat steps 7-10 for however many microbits you have. Use senderB.hex for the second one, senderC.hex for the third one etc.
12. Finally, connect the first microbit to the USB-port, the one that contains the receiver.hex-file and keep it plugged in.


Running the program:
1. In the terminal, be in the /FlaskApp directory
2. Type main.py
The microbits containing the 'sender.hex'-files will transmit radio signals to the microbit connected to the USB-port
3. Type in http://127.0.0.1:5000/ in your web-browser and you should see the interface



