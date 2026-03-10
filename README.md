<h1>🛜Chat de Redes IFSC 2026</h1>
<img src="imagens/imagem.png" height="350">
<h3>Com base nos conceitos apresentados nas aulas (materia de Redes- IFSC) e utilizando a linguagem de programação de sua 
preferência crie uma aplicação de bate papo (chat) contemplando os seguintes requisitos técnicos: </h3></br>
• deve ter interface gráfica (GUI – Graphical User Interface); </br>
• somente uma aplicação será desenvolvida, sendo esta capaz de enviar e receber mensagens; </br>
◦ obs.: para o envio e recebimento de mensagens de forma simultânea, a mesma porta de comunicação
pode ser utilizada, porém o envio e recebimento devem ser tratados em threads distintas; </br>
• a comunicação entre os nós comunicantes deve ser realizada obrigatoriamente via multicast; </br>
◦ obs.: o padrão multicast exige a utilização do protocolo UDP; </br>
• a interface gráfica deve permitir ao usuário: </br>
◦ definir o seu nome de usuário; </br>
◦ definir o grupo multicast ao qual a aplicação irá entrar; </br>
◦ definir a porta de comunicação; </br>
◦ entrar e sair de diferentes grupos sem o fechamento da aplicação; </br>
▪ obs: a aplicação irá se comunicar (entrar) com apenas 1 grupo por vez; </br>
• o payload (carga útil) da mensagem deve estar no formato JSON (codificação UTF-8) e seguir
rigorosamente o seguinte layout: </br>
</br>
{ </br>
"date":"date_value", </br>
"time":"time_value", </br>
"username":"username_value", </br>
"message":"message_value"</br> 
} </br>
<h3>Onde:</h3>
date_value é a data (dd/mm/aaaa) de envio da mensagem (obtida no nó origem); </br>
time_value é a hora (hh:mm:ss) de envio da mensagem (obtida no nó origem); </br>
username_value é o nome do usuário que enviou a mensagem; </br>
message_value é a mensagem em si;
