# JoaoGomes_Processamento_de_imagens

# Descri��o do conceito, com fun��o e motiva��o

* Projeto: Detectar formas geom�tricas, e posteriormente avan�ar em processamento de imagens.

* Motiva��o: Adquirir conhecimento e pr�tica em processamento de imagem, uma �rea que me interessa bastante.

* Descri��o do conceito: Inicialmente, o objetivo � aprender a detectar formas geom�tricas utilizando a biblioteca OpenCV do C++. Posteriormente, avan�ar nos m�todos de processamento de imagem, como detec��o de cores.

# Fluxograma

![alt text](https://github.com/ProgramacaoEE2018/JoaoGomes_Processamento_de_imagens/blob/master/Fluxograma.PNG)

# Diagrama de Classes

![alt text](https://github.com/ProgramacaoEE2018/JoaoGomes_Processamento_de_imagens/blob/master/Diagrama%20de%20Classes.PNG)

# **Tutorial - Biblioteca gr�fica**

O tutorial realizado foi o do Kivy para Python, veja o seguinte link [v�deo do youtube](https://www.youtube.com/watch?v=WiyF3VsL5dY) e outros v�deos do mesmo canal.

O objetivo do tutorial foi criar uma interface de f�cil uso, capaz de fornecer o resultado do processamento da imagem.

O resultado pode ser observado nas imagens abaixo:

![alt text](https://github.com/ProgramacaoEE2018/JoaoGomes_Processamento_de_imagens/blob/master/esbocoGUI.PNG)

![alt text](https://github.com/ProgramacaoEE2018/JoaoGomes_Processamento_de_imagens/blob/master/esbocoGUI_2.PNG)

A interface possui um cabe�alho, e um bot�o. O bot�o ao receber um clique, fornece a imagem processada.

# **Tutorial - Como rodar o programa**

Primeiramente, � preciso o python instalado no windows, de prefer�ncia o Python 3.

Em seguida, vamos instalar as bibliotecas necess�rias usando a seguinte sequ�ncia se comandos no prompt de comando:

* pip install --upgrade pip setuptools wheel

* pip install "numpy-1.14.2+mkl-cp36-cp36m-win32.whl"

* pip install matplotlib

* pip install "opencv_python-3.4.1+contrib-cp36-cp36m-win32.whl"

* pip install opencv-python (apenas caso a anterior n�o funcione, mas aconselho a fazer tamb�m)

* pip install imutils

* pip install argparse

Agora, coloque o arquivo de imagem que deseja filtrar na mesma pasta em que est� o programa de processamento de imagem.

Ap�s isso, com o prompt de comando aberto, acesse a pasta em que est�o programa e a imagem a ser filtrada.

Agora, digite: python Processamento de imagem - Formas geometricas.py

E, ap�s aparecer uma mensagem pedindo para digitar 1 caso a cor do plano de fundo da imagem seja preta, e 0 caso seja branco, fa�a o que se pede.

Agora, digite o arquivo de imagem. Ex de uma imagem que coloquei no reposit�rio: shapes_and_colors.png

O programa ir� abrir a interface gr�fica, que n�o est� completa devido a conflitos entre a biblioteca kivy e as outras bibliotecas utilizadas, e infelizmente ainda n�o consegui resolver esse problema.

Por fim, clique no bot�o do programa, e ele ir� mudar a imagem para a imagem processada.

Detalhe, o programa cria um arquivo imagem.png, da imagem processada na mesma pasta do programa.

# Funcionamento do programa final

Basicamente, ele necessita de duas entradas, o indicativo da cor do plano de fundo da imagem e o nome do arquivo de imagem a ser utilizada, respectivamente.

Uma janela ser� aberta, com a imagem que deseja processar, e ao clicar no bot�o, a imagem ser� trocada pela nova imagem processada. Al�m disso, ser� criado um arquivo da nova imagem na pasta do programa.