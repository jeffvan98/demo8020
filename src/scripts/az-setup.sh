#! /bin/bash

export RESOURCE_GROUP="2023-12-04-RG-01" # resource group of k8s cluster
export CLUSTER_NAME="aks7c02" # name of k8s cluster
export LOCATION="westus3" # location of k8s cluster
export SUBSCRIPTION="$(az account show --query id --output tsv)" # subscription of k8s cluster
export USER_ASSIGNED_IDENTITY_NAME="oncologysvc" #  name of managed id
export SERVICE_ACCOUNT_NAMESPACE="oncology" # name of service account in k8s
export SERVICE_ACCOUNT_NAME="oncologysvc" # namespace that contains service account
export FEDERATED_IDENTITY_CREDENTIAL_NAME="oncologysvc" # use the same name as user_assigned_identity_name
export KEYVAULT_NAME="vault7c02" # keyvault name
export KEYVAULT_RESOURCE_GROUP="2023-12-04-RG-01" # keyvault resource group

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

echo "ATTENTION - User Assigned Client ID:"
echo $USER_ASSIGNED_CLIENT_ID
read -p "Press enter to continue"

# Grant Key Vault Get Secret Permissions to the Managed ID
az keyvault set-policy \
--name "${KEYVAULT_NAME}" \
--resource-group "${KEYVAULT_RESOURCE_GROUP}" \
--secret-permissions get \
--spn "${USER_ASSIGNED_CLIENT_ID}"