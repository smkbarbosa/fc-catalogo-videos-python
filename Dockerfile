FROM python:3.10.2-slim

# usuário padrão para o container
# echo $UID no terminal --> colocar o mesmo UID da sua maquina para manter a compatibilidade entre os arquivos
# padrão 1000

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

CMD [ "tail", "-f", "/dev/null" ]