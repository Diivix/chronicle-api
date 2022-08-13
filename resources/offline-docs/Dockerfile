FROM squidfunk/mkdocs-material

RUN pip install mdx-include && \
    pip install mkdocs-markdownextradata-plugin

WORKDIR /repos
RUN git clone https://github.com/tiangolo/sqlmodel.git
RUN git clone https://github.com/tiangolo/fastapi.git

WORKDIR /root
COPY ./docs/offline/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

EXPOSE 8010
EXPOSE 8020

ENTRYPOINT [ "/root/entrypoint.sh" ]