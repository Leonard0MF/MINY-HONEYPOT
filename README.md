# MINY-HONEYPOT
meus projetos 

 Mini Honeypot

Esse é um projeto simples que eu fiz pra começar a entender melhor como funciona a parte de escuta de conexões e captura de dados em redes. 
É tipo um honeypot básico feito em Python, que registra IP, porta e o que for enviado pra ele.

É bem simples, mas funcional.


 O que ele faz

- Escuta conexões na porta 8080
- Registra o IP de quem tentou se conectar
- Guarda o texto enviado no log
- Funciona com telnet ou até navegadores (se mudar a porta pra 80)
- Cria os logs em uma pastinha automática


 Por que eu fiz isso?

Tô estudando cibersegurança e queria colocar a mão no código. Sempre vi sobre honeypots, mas nunca tinha feito um. 
Esse projeto é meu jeito de começar a explorar o lado da coleta de informações (passiva, no caso).


 Como rodar

1. Tenha Python instalado (usei a versão 3.14)
2. Clona o repositório:
   ```bash
   git clone https://github.com/Leonard0MF/MINY-HONEYPOT
   cd MINY-HONEYPOT

Isso aqui é só pra estudo. Não use isso exposto na internet sem proteção, e sempre com responsabilidade.

Feito por mim
Leonardo — 17 anos, estudando programação e cibersegurança.