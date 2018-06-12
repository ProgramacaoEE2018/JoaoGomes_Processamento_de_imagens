# JoaoGomes_Processamento_de_imagens

* Projeto: Detectar formas geométricas, e posteriormente avançar em processamento de imagens.

* Motivação: Adquirir conhecimento e prática em processamento de imagem, uma área que me interessa bastante.

* Descrição do conceito: Inicialmente, o objetivo é aprender a detectar formas geométricas utilizando a biblioteca OpenCV do C++. Posteriormente, avançar nos métodos de processamento de imagem, como detecção de cores.

# **Tutorial - Biblioteca gráfica**

O tutorial realizado foi o do Kivy para Python, veja o seguinte link [vídeo do youtube](https://www.youtube.com/watch?v=WiyF3VsL5dY) e outros vídeos do mesmo canal.

O objetivo do tutorial foi criar uma interface de fácil uso, capaz de fornecer o resultado do processamento da imagem.

O resultado pode ser observado nas imagens abaixo:

![alt text](https://github.com/ProgramacaoEE2018/JoaoGomes_Processamento_de_imagens/blob/master/esbocoGUI.PNG)

![alt text](https://github.com/ProgramacaoEE2018/JoaoGomes_Processamento_de_imagens/blob/master/esbocoGUI_2.PNG)

A interface possui um cabeçalho, e um botão. O botão ao receber um clique, fornece a imagem processada.

# **Tutorial - Como rodar o programa**

Primeiramente, é preciso o python instalado no windows, de preferência o Python 3.

Em seguida, vamos instalar as bibliotecas necessárias usando a seguinte sequência se comandos no prompt de comando:

* pip install --upgrade pip setuptools wheel

* pip install "numpy-1.14.2+mkl-cp36-cp36m-win32.whl"

* pip install matplotlib

* pip install "opencv_python-3.4.1+contrib-cp36-cp36m-win32.whl"

* pip install opencv-python (apenas caso a anterior não funcione, mas aconselho a fazer também)

* pip install imutils

* pip install argparse

Agora, coloque o arquivo de imagem que deseja filtrar na mesma pasta em que está o programa de processamento de imagem.

Após isso, com o prompt de comando aberto, acesse a pasta em que estão programa e a imagem a ser filtrada.

Agora, digite: python Processamento de imagem - Formas geometricas.py

E, após aparecer uma mensagem pedindo para digitar 1 caso a cor do plano de fundo da imagem seja preta, e 0 caso seja branco, faça o que se pede.

Agora, digite o arquivo de imagem. Ex de uma imagem que coloquei no repositório: shapes_and_colors.png

O programa irá abrir a interface gráfica, que não está completa devido a conflitos entre a biblioteca kivy e as outras bibliotecas utilizadas, e infelizmente ainda não consegui resolver esse problema.

Por fim, clique no botão do programa, e ele irá mudar a imagem para a imagem processada.

Detalhe, o programa cria um arquivo imagem.png, da imagem processada na mesma pasta do programa.