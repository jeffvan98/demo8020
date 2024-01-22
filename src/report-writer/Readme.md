# Report-Writer

## Overview
This project creates a container image that will run notebook.ipynb and export the results to an HTML file.  

## Details
notebook.ipynb contains python code that queries data from an instance of MongoDb and prints it. It uses the following environment variables:

| KEY                           | SAMPLE VALUE                      |
|-------------------------------|-----------------------------------|
| REPORT_WRITER_KEY_VAULT_URL   | https://vault7c02.vault.azure.net |
| REPORT_WRITER_SECRET_NAME     | mongo-connection                  |
| REPORT_WRITER_DATABASE_NAME   | PatientData                       |
| REPORT_WRITER_COLLECTION_NAME | Default                           |

start.sh is the entrypoint for this image.  It runs jupyter, passing in notebook.ipynb as input, and writes a date-time-encoded output file to /app/export.  It also creates a copy of this file, named latest.  Mount an external volume to /app/export in order to preserve this output.

## Build
example: 

```bash
docker build -t report-writer:latest .
docker tag report-writer:latest acr7c02.azurecr.io/report-writer:latest
docker push acr7c02.azurecr.io/report-writer:latest
```