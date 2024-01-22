FROM quay.io/jupyter/docker-stacks-foundation:python-3.11

ENV REPORT_WRITER_KEY_VAULT_URL=https://vault7c02.vault.azure.net
ENV REPORT_WRITER_SECRET_NAME=mongo-connection
ENV REPORT_WRITER_DATABASE_NAME=PatientData
ENV REPORT_WRITER_COLLECTION_NAME=Default

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN mkdir export

ENTRYPOINT [ "/app/start.sh" ]