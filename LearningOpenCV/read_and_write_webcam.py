'''Código que lê e exibe a transmissão de vídeo de uma webcam utilizando OpenCV'''

#Biblioteca do OpenCV2
import cv2

# Cria um objeto de captura de vídeo, nesse caso, estamos conectados à webcam
vid_capture = cv2.VideoCapture(0)

# Verifica se o vídeo foi aberto corretamente
if(vid_capture.isOpened() == False):
    print("Deu ruim!")
else:

    # Obtém a informação das dimensões do frame utilizando o método get()
    frame_width = int(vid_capture.get(3))
    frame_height = int(vid_capture.get(4))
    frame_size = (frame_width,frame_height)
    fps = 20
    # Inicializa o objeto de criação de vídeo
    output = cv2.VideoWriter('/home/tsuna/Testes_OpenCV/LearningOpenCV/video_criado.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps, frame_size)


    while(vid_capture.isOpened()):
        # O método vCapture.read() retorna uma tupla, o primeiro elemento é um booleano e o segundo é um frame
        ret, frame = vid_capture.read()
        if ret == True:
            # Passa o frame para os arquivos de saída
            output.write(frame)
        else:
            print("Deu ruim!")
            break

# Libera os objetos
vid_capture.release()
cv2.destroyAllWindows()


