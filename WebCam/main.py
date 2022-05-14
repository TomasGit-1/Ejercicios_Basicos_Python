# import cv2, importar la librería de openCV
# capture = cv2.VideoCapture(0), crear un objeto capture de VideoCapture(0)
# Tiene como argumento 0 para leer la webCam. También recibe valores como -1, 1, etc si se conecta en otros puertos otras cámaras.
# while (capture.isOpened()):
# capture.isOpened() Devuelve True si la captura de video ya se ha inicializado.
# ret, frame = capture.read(), usa el objeto capture para leer la información de la webCam
# frame información del video frame por frame
# ret valor booleano TRUE si frame es leído correctamente
# if (cv2.waitKey(1) == ord('s')):, sentencia if compara dos valores, si se cumple la condición termina el bucle.
# cv2.waitKey(1), si una tecla es presionada, regresa un valor de acuerdo al código ascii, mientras no se presione una tecla devuelve el valor de -1
# ord('s') la función ord recibe un caracter y devuelve un valor que representa a ese caracter.
# La condición 1 queda de la siguiente manera: (cv2.waitKey(1) == ord('s')) –> 1110011 == 01110011 (Cuando se cuple, sale del bucle)
# capture.release() para liberar la captura
# cv2.destroyAllWindows() cerrar todas las ventanas


import cv2

# capture = cv2.VideoCapture(0)

# while(capture.isOpened()):
#     ret , frame = capture.read()
#     cv2.imshow('webCam' , frame)
#     if(cv2.waitKey(1) == ord('s')):
#         break

capture = cv2.VideoCapture('Street.mp4')
start_point = (200, 205)
end_point = (420, 420)
color = (255, 0, 0)
thickness = 2

while (capture.isOpened()):
    ret, frame = capture.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    image = cv2.rectangle(frame, start_point, end_point, color, thickness)

    if (ret == True):
        cv2.imshow("gato0", image)
        if (cv2.waitKey(30) == ord('s')):
            break
    else:
        break



capture.release()
cv2.destroyAllWindows()
