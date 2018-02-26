#!/usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 3456))

mySocket.listen(5)

sumandos = 0

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict")
        print(peticion)

        try:
            numero = peticion.split()[1][1:]
            print (numero)

            if numero == "favicon.ico":
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "Continue\r\n", 'utf-8'))
                recvSocket.close()
                continue
            print('Answering back...')

            if (sumandos == 0):
                sumandos = numero
                resultado = "Has introducido el siguiente nr.: " + str(sumandos) + " ///Por favor, introduce un segundo nr.: "
            else:
                sumando2 = numero
                suma = int(sumandos) + int(sumando2)
                resultado = "El primer nr. introducido ha sido: " + str(sumandos) + " ///El segundo nr. introducido ha sido: " + str(sumando2) + " ///La suma de ambos es: " + str(suma)
                sumandos = 0

            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>" + resultado + "</h1></body></html>" +
                            "\r\n", 'utf-8'))
            recvSocket.close()
        except ValueError:
            resultado = resultado = "Se ha introducido un: " + str(sumandos) + " ///Se ha introducido un: " + str(sumando2) + " ///ERROR, el sumador funciona solo con numeros"
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>" + resultado + "</h1></body></html>" +
                            "\r\n", 'utf-8'))
            recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
mySocket.close()
