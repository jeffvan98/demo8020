#! /bin/bash

export RESOURCE_GROUP="2023-12-04-RG-01"
export CLUSTER_NAME="aks7c02"
export LOCATION="westus3"
export SUBSCRIPTION="$(az account show --query id --output tsv)"
export USER_ASSIGNED_IDENTITY_NAME="neurologysvc"
export SERVICE_ACCOUNT_NAMESPACE="neurology"
export SERVICE_ACCOUNT_NAME="neurologysvc"
export USER_ASSIGNED_IDENTITY_NAME="neurologysvc"
export FEDERATED_IDENTITY_CREDENTIAL_NAME="neurologysvc"
export KEYVAULT_NAME="vault7c02"

# Create a Managed Identity
az identity create \
--name "${USER_ASSIGNED_IDENTITY_NAME}" \
--resource-group "${RESOURCE_GROUP}" \
--location "${LOCATION}" \
--subscription "${SUBSCRIPTION}"

# Retrieve the OIDC Issuer URL
export AKS_OIDC_ISSUER="$(az aks show \
-n "${CLUSTER_NAME}" \
-g "${RESOURCE_GROUP}" \
--query "oidcIssuerProfile.issuerUrl" \
-otsv)"

# Establish Federated Identity Credential
az identity federated-credential create \
--name ${FEDERATED_IDENTITY_CREDENTIAL_NAME} \
--identity-name "${USER_ASSIGNED_IDENTITY_NAME}" \
--resource-group "${RESOURCE_GROUP}" \
--issuer "${AKS_OIDC_ISSUER}" \
--subject system:serviceaccount:"${SERVICE_ACCOUNT_NAMESPACE}":"${SERVICE_ACCOUNT_NAME}" \
--audience api://AzureADTokenExchange

# Obtain the Client ID for the Managed Identity
export USER_ASSIGNED_CLIENT_ID="$(az identity show \
--resource-group "${RESOURCE_GROUP}" \
--name "${USER_ASSIGNED_IDENTITY_NAME}" \
--query 'clientId' \
-otsv)"

# Grant Key Vault Get Secret Permissions to the Managed ID
az keyvault set-policy \
--name "${KEYVAULT_NAME}" \
--secret-permissions get \
--spn "${USER_ASSIGNED_CLIENT_ID}"