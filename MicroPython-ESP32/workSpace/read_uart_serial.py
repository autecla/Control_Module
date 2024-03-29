#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Receive from UART_serial
#   Sketch/program to read data from RFID_Module by UART_serial using micropython
#   Tip: To test this program, you can use an arduino and the program found in "Arduino/test_serial_arduino" or "Arduino/little_test_serial_arduino"
#   ESP32 Port:
#      Pin_RX = 16
#      Pin_TX = 17
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************

from machine import UART

urt = UART(2, 9600)
urt.init(9600, bits=8, parity=None, stop=1, tx=17, rx=16)

while True:
    if (urt.any()):
        dados = urt.readline()
        print('Dado:', dados)
