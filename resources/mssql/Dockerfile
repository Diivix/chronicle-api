FROM mcr.microsoft.com/mssql/server:2019-latest

USER root

RUN apt-get update
RUN apt-get install -y \
    curl \
    gnupg-agent

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

#Ubuntu 20.04
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list


RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17 \
    mssql-tools

ENV PATH /opt/mssql-tools/bin:$PATH

USER mssql