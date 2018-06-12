#Dependencias de bibliotecas:
#vamos baixar as bibliotecas
#abra o prompt de comando do windows
#digite os seguintes passos
#pip install --upgrade pip setuptools wheel
#pip install "numpy‑1.14.2+mkl‑cp36‑cp36m‑win32.whl"
#pip install matplotlib
#pip install "opencv_python‑3.4.1+contrib‑cp36‑cp36m‑win32.whl"
#pip install opencv-python
#pip install imutils

#pip install argparse

#digite: python nome_do_programa.py
#o programa vai pedir para digitar 1 se o plano de fundo for preto
#e 0 se nao for preto
#digite: nome_da_imagem.png ou .jpg ou
#outra terminação


from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
import cv2
import argparse
import imutils

class ShapeDetector:
        def __init__(self):
                pass

        def detect(self, c):
                # inicialize o nome da forma e aproxime o contorno
                shape = "nao identificado"
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.04 * peri, True)

                # se é um triangulo, terá 3 vértices
                if len(approx) == 3:
                        shape = "triangulo"

                # se é um quadrado ou retângulo, terá 4 vértices
                elif len(approx) == 4:
                        # compute the bounding box of the contour and use the
                        # bounding box to compute the aspect ratio
                        (x, y, w, h) = cv2.boundingRect(approx)
                        ar = w / float(h)

                        # um quadrado tem um 'aspect ratio' aproximadamente
                        # igual a 1, caso contrário, será um retângulo
                        shape = "quadrado" if ar >= 0.95 and ar <= 1.05 else "retangulo"

                # se é um pentágono, terá 5 vértices
                elif len(approx) == 5:
                        shape = "pentagono"

                # Vamos assumir que acima de 5 vértices, será um círculo
                else:
                        shape = "circulo"

                # retorna o nome da forma geométrica
                return shape

# Vamos analisar se o plano é preto ou branco
# Infelizmente, o programa só detecta corretamente as formas
# com um fundo nessas cores
k = int(input("Se o plano de fundo da imagem for preto, digite 1. Digite 0 caso contrário: "))
# carregue a imagem, e mude seu tamanho para um fator menor
# para que as formas sejam aproximadas com mais precisão
im = input("Digite o nome da imagem com sua terminação: ")
if im != None:
        image = cv2.imread(im)
        resized = imutils.resize(image, width=300)
        ratio = image.shape[0] / float(resized.shape[0])
        # converta a imagem para uma escala de cinza, e borre-a levemente com o 'blur'
        # use o threshold na imagem
        # os parâmetros usados, são específicos e foram encontrados na internet
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        if k == 1:
            thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
        else:
            thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)[1]


        # encontre os contornos na iamgem resultante e inicialize o
        # detector de formas geométricas
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        sd = ShapeDetector()

        # loop pelos contornos
        for c in cnts:
                # calcule o centro do contorno, e então detecte o nome da
                # forma usando apenas o contorno
                M = cv2.moments(c)
                cX = int((M["m10"] / M["m00"]) * ratio)
                cY = int((M["m01"] / M["m00"]) * ratio)
                shape = sd.detect(c)

                # multiplique o contorno (x, y)-coordenadas pelo resize ratio,
                # então desenhe os contornos e o nome da forma da imagem
                c = c.astype("float")
                c *= ratio
                c = c.astype("int")
                cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 255, 255), 2)

                # opções para teste
                #cv2.imshow("Image", image)
                #cv2.imshow("gray", gray)
                #cv2.imshow("blur", blurred)
                #cv2.imshow("thresh", thresh)

        #crie o arquivo de imagem, da imagem processada
        cv2.imwrite('image.png', image)

#parte gráfica do programa:       
class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text = 'Clique aqui', font_size = 30, size_hint = (1, .2), on_release = self.incrementar)
        label = Label(text = 'Processar a imagem', font_size = 30, size_hint = (1, .2))
        self.image = Image(source = im)

        box.add_widget(label)
        box.add_widget(button)
        box.add_widget(self.image)
        return box

    def incrementar(self,button):
        self.image.source = 'image.png'

#Executar a interface gráfica        
Test().run()
