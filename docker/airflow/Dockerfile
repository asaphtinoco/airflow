#definindo a imagem de base - start point 
FROM spark-base:latest
LABEL maintainer = 'Asaph Tinoco'

#Definindo as variaveis que serão usadas para a instalação da imagem no container
ARG AIRFLOW_VERSION=1.10.12
ARG AIRFLOW_HOME=/usr/local/home
ARG APACHE_INSTALL=apache-airflow[crypto,celery,postgres,hive,jdbc,mysql,ssh,docker,hdfs,redis,webhdfs]

#Comando export no linux para declaracao da variavel home
ENV AIRFLOW_HOME=${AIRFLOW_HOME}


RUN apt-get update -y && \
    apt-get upgrade -yqq && \
    apt-get install -yqq --no-install-recommends \
    python3-dev \
    wget \
    libczmq-dev \
    curl \
    libssl-dev \
    git \
    inetutils-telnet \
    bind9utils freetds-dev \
    libkrb5-dev \
    libsasl2-dev \
    libffi-dev libpq-dev \
    freetds-bin build-essential \
    default-libmysqlclient-dev \
    apt-utils \
    rsync \
    zip \
    unzip \
    gcc \
    vim \
    netcat \
    && apt-get autoremove -yqq --purge && apt-get clean

#copiando as bibliotecas do python que eventualmente serão utilizadas para dentro do container
COPY ./requirements-python3.7.txt /requirements-python3.7.txt

# instalando pip  
# criando user aiflow:
    # useradd -ms /bin/bash --> colocando bin/bash como login shell da conta
    # -d ${AIRFLOW_HOME} airflow --> setando a pasta do novo user
    # airflow --> nome do user
    # -G sudo --> dando acesso de admin ao user
# instalando pip com as bibliotecas anexas no arquivo externo
RUN pip install --upgrade "pip==20.2.4" && \
    useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow && \
    pip install $APACHE_INSTALL==${AIRFLOW_VERSION} --constraint /requirements-python3.7.txt

# chown -R --> mudar o dono da pasta / -R recursivamente, ou seja, todos os arquivos que vem embaixo dessa pasta tambem mudarao de dono 
RUN chown -R airflow: ${AIRFLOW_HOME}

# Copy the entrypoint.sh from host to container (at path AIRFLOW_HOME)
COPY ./start-airflow.sh ./start-airflow.sh

# Set the entrypoint.sh file to be executable
RUN chmod +x ./start-airflow.sh

# Set the username to use
USER airflow

# Create the folder dags inside $AIRFLOW_HOME
RUN mkdir -p ${AIRFLOW_HOME}/dags

# Expose ports (just to indicate that this container needs to map port)
EXPOSE 8080

# Execute start-airflow.sh
CMD [ "./start-airflow.sh" ]