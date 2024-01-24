# Installation Steps 

1. Create a kubernetes namespace for the deployment

```bash
kubectl create namespace <NAMESPACE>
```

2. Update and run scripts/az-setup.sh

This will create the application's Managed Identity and Federated Credential and grant them permission to Key Vault

```bash
./scripts/az-setup.sh
```

3. Update demo8020/values.yaml and install the helm chart

This will create all the application artifacts in Kubernetes.

```bash
helm install demo8020 demo8020 -n <NAMESPACE>
```

## Notes

- Prerequisites:

   - ingress-nginx and oauth2-proxy must be installed (including supporting Entra Application) and configured before installing this application.

   - report-writer is designed to perform a simple query against a mongo database.  In order to do this, it needs a mongo connection string.  This connection string should be stored as a secret in Key Vault and called "mongo-connection"

   - both report-writer and the dashboard-web-application are designed to read and write to an Azure Storage Account Blob Container.  A storage account and blob container are required.

- The dashboard-web-application is a web UI built with the assumption that it will be protected under the combination of ingress-nginx and oauth2-proxy.  When deployed, it should appear in the following structure:

```
ROOT \
   - auth-neurology <- oauth2-proxy deployed here
   - neurology <- dashboard-web-application deployed here
```

- The report-writer is configured to run once per day at midnight.  You can run it on demand using the following technique:

```bash
kubectl create job --from=cronjob/report-writer <NEW-JOB-NAME> -n <NAMESPACE>
```