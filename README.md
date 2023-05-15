# Ponderada 2 | movimentação do TurtleBot no Gazebo

O controle de movimento do robô no ROS2 é feito por meio de mensagens de Twist que passam velocidades lineares e angulares. Porém, como o robô não é omnidirecional e só pode se movimentar para frente e para trás, além de rotacionar ao redor de seu eixo z, é necessário descobrir o vetor relativo entre a posição atual do robô e a posição desejada para que ele possa se movimentar para um ponto específico.

Para isso, é necessário realizar a transformação de bases de coordenadas para converter as coordenadas relativas do robô em relação ao seu próprio sistema de coordenadas para as coordenadas absolutas do mundo.

Para realizar essa transformação, é necessário conhecer a posição e rotação do robô em relação ao mundo, o que pode ser obtido por meio de um subscriber do nó no ROS2. A partir disso, é possível calcular a rotação total necessária para que o robô se vire no sentido do vetor relativo entre a posição atual e a posição desejada e, em seguida, a translação necessária para que o robô possa se mover em direção ao ponto de inspeção desejado. Essas informações são enviadas à simulação através do publicador do nó em questão.

Assim, a utilização da transformação de bases de coordenadas, é possível programar o robô para ir a um ponto específico em um ambiente complexo. Além disso, com a adição de uma lógica de filas no programa, podemos programar rotas completas de forma eficiente e automatizada.

A rota configurada para este entregável foi uma espiral com início na origem do mundo.

<img src="/src/route.png">

Demo: https://www.youtube.com/watch?v=C1FmhUciqL0