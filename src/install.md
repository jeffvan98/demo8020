# Installation Steps 

1. Prerequisites

- ingress-nginx and oauth2-proxy must be installed (including supporting Entra Application) and configured before installing this application.
- key-vault - the demo requires an instance of key vault
- storage account - both the report-writer and dashboard-web-application write and read from a blob storage container
- report-writer application:
   - this part of the application is designed to perform a simple query against a mongo database.  
   - you will require a mongo database (or compatible) that the report-writer can query
   - In order to do this, it needs a mongo connection string.  
   - The connection string should be stored as a secret in Key Vault and called "mongo-connection"
- dashbord-web-application:
   - This is a web UI built with the assumption that it will be protected under the combination of ingress-nginx and oauth2-proxy.
   - When deployed, it should appear in the following structure:

      ```
      ROOT \
         - auth-neurology <- oauth2-proxy deployed here
         - neurology <- dashboard-web-application deployed here
      ```

2. Create a kubernetes namespace for the deployment

```bash
kubectl create namespace <NAMESPACE>
```

3. Update and run scripts/az-setup.sh

This will create the application's Managed Identity and Federated Credential and grant them permission to Key Vault

```bash
./scripts/az-setup.sh
```

4. Update demo8020/values.yaml and install the helm chart

This will create all the application artifacts in Kubernetes.

```bash
helm install demo8020 demo8020 -n <NAMESPACE>
```

## Notes

- The report-writer is configured to run once per day at midnight.  You can run it on demand using the following technique:

```bash
kubectl create job --from=cronjob/report-writer <NEW-JOB-NAME> -n <NAMESPACE>
```