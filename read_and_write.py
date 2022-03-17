#Biblioteca do OpenCV2
import cv2

#Lê e armazena uma mesma imagem em trẽs diferentes flags
img_color = cv2.imread("/home/tsuna/Downloads/16030.jpg", cv2.IMREAD_COLOR)
img_grayscale = cv2.imread("/home/tsuna/Downloads/16030.jpg",cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread("/home/tsuna/Downloads/16030.jpg",cv2.IMREAD_UNCHANGED)

#Exibe as três imagens criadas anteriormente
cv2.imshow('color image',img_color) 
cv2.imshow('grayscale image',img_grayscale)
cv2.imshow('unchanged image',img_unchanged)

#Espera indefinidamente até a inserção de uma tecla de fechamento
cv2.waitKey(0) 

#"Destroi" todas as janelas criadas
cv2.destroyAllwindows()

