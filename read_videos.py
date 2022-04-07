'''Código que lê e exibe um vídeo utilizando OpenCV'''

# Biblioteca do OpenCV2
import cv2

# Cria um objeto de captura de vídeo, nesse caso, estamos lendo um vídeo de um arquivo
vid_capture = cv2.VideoCapture("/home/tsuna/Testes_OpenCV/LearningOpenCV/teste.mp4")

# Verifica se o vídeo foi aberto corretamente
if(vid_capture.isOpened() == False):
    print("Deu ruim!")
else:
    # Recolhe a taxa de frames
    fps = int(vid_capture.get(5))
    print("Frame Rate: ", fps, "frames por segundo")

    # Recolhe o número de frames
    frame_count = vid_capture.get(7)
    print("Frame Count: ", frame_count)


while(vid_capture.isOpened()):
    # O método vCapture.read() retorna uma tupla, o primeiro elemento é um booleano e o segundo é um frame
    ret, frame = vid_capture.read()

    #Verifica se o frame está ou não presente e o exibe caso esteja
    if ret == True:
        cv2.imshow("Frame", frame)
        # Espera 20ms entre dois frames consecutivos e quebra o loop se a tecla q for pressionada
        k = cv2.waitKey(20)
        # 113 é um código ASCII para a letra "q"
        if k == 113:   
            break
    else:
        break

# Libera os objetos
vid_capture.release()
cv2.destroyAllWindows()


