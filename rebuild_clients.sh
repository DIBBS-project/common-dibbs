#!/usr/bin/env bash

SWAGGER_CODE_GEN_PATH=$(which swagger-codegen)

if [ "${SWAGGER_CODE_GEN_PATH}" == "" ]; then
    echo "Could not find the 'swagger-codegen' tool."
    echo "  => Please go to https://github.com/swagger-api/swagger-codegen to find how to install it!"
    echo ""
    echo "  PSST: on MacOS, run 'brew install swagger-codegen' to install swagger-codegen"

    exit 1
fi


###########################################################
# Generate the client for Appliance Registry
###########################################################

CLIENT_NAME="ar_client"
swagger-codegen generate -i swagger/${CLIENT_NAME}/swagger.yaml -l python -o /tmp/test/${CLIENT_NAME}/
if [ -d /tmp/test/${CLIENT_NAME}/swagger_client ]; then
    # Erase old version of the client
    rm -rf common_dibbs/clients/${CLIENT_NAME}
    # Copy the new version of the client to the clients package
    cp -r /tmp/test/${CLIENT_NAME}/swagger_client common_dibbs/clients/${CLIENT_NAME}
else
    echo "Could not find the folder generated for ${CLIENT_NAME}, aborting :("
    exit 1
fi


###########################################################
# Generate the client for Central Authentication System
###########################################################

CLIENT_NAME="cas_client"
swagger-codegen generate -i swagger/${CLIENT_NAME}/swagger.yaml -l python -o /tmp/test/${CLIENT_NAME}/
if [ -d /tmp/test/${CLIENT_NAME}/swagger_client ]; then
    # Erase old version of the client
    rm -rf common_dibbs/clients/${CLIENT_NAME}
    # Copy the new version of the client to the clients package
    cp -r /tmp/test/${CLIENT_NAME}/swagger_client common_dibbs/clients/${CLIENT_NAME}
else
    echo "Could not find the folder generated for ${CLIENT_NAME}, aborting :("
    exit 1
fi


###########################################################
# Generate the client for Operation Management
###########################################################

CLIENT_NAME="om_client"
swagger-codegen generate -i swagger/${CLIENT_NAME}/swagger.yaml -l python -o /tmp/test/${CLIENT_NAME}/
if [ -d /tmp/test/${CLIENT_NAME}/swagger_client ]; then
    # Erase old version of the client
    rm -rf common_dibbs/clients/${CLIENT_NAME}
    # Copy the new version of the client to the clients package
    cp -r /tmp/test/${CLIENT_NAME}/swagger_client common_dibbs/clients/${CLIENT_NAME}
else
    echo "Could not find the folder generated for ${CLIENT_NAME}, aborting :("
    exit 1
fi


###########################################################
# Generate the client for Operation Management Agent
###########################################################

CLIENT_NAME="oma_client"
swagger-codegen generate -i swagger/${CLIENT_NAME}/swagger.yaml -l python -o /tmp/test/${CLIENT_NAME}/
if [ -d /tmp/test/${CLIENT_NAME}/swagger_client ]; then
    # Erase old version of the client
    rm -rf common_dibbs/clients/${CLIENT_NAME}
    # Copy the new version of the client to the clients package
    cp -r /tmp/test/${CLIENT_NAME}/swagger_client common_dibbs/clients/${CLIENT_NAME}
else
    echo "Could not find the folder generated for ${CLIENT_NAME}, aborting :("
    exit 1
fi


###########################################################
# Generate the client for Operation Registry
###########################################################

CLIENT_NAME="or_client"
swagger-codegen generate -i swagger/${CLIENT_NAME}/swagger.yaml -l python -o /tmp/test/${CLIENT_NAME}/
if [ -d /tmp/test/${CLIENT_NAME}/swagger_client ]; then
    # Erase old version of the client
    rm -rf common_dibbs/clients/${CLIENT_NAME}
    # Copy the new version of the client to the clients package
    cp -r /tmp/test/${CLIENT_NAME}/swagger_client common_dibbs/clients/${CLIENT_NAME}
else
    echo "Could not find the folder generated for ${CLIENT_NAME}, aborting :("
    exit 1
fi


###########################################################
# Generate the client for Resource Manager
###########################################################

CLIENT_NAME="rm_client"
swagger-codegen generate -i swagger/${CLIENT_NAME}/swagger.yaml -l python -o /tmp/test/${CLIENT_NAME}/
if [ -d /tmp/test/${CLIENT_NAME}/swagger_client ]; then
    # Erase old version of the client
    rm -rf common_dibbs/clients/${CLIENT_NAME}
    # Copy the new version of the client to the clients package
    cp -r /tmp/test/${CLIENT_NAME}/swagger_client common_dibbs/clients/${CLIENT_NAME}
else
    echo "Could not find the folder generated for ${CLIENT_NAME}, aborting :("
    exit 1
fi


###########################################################
# Generate the client for Resource Manager Agent
###########################################################

CLIENT_NAME="rma_client"
swagger-codegen generate -i swagger/${CLIENT_NAME}/swagger.yaml -l python -o /tmp/test/${CLIENT_NAME}/
if [ -d /tmp/test/${CLIENT_NAME}/swagger_client ]; then
    # Erase old version of the client
    rm -rf common_dibbs/clients/${CLIENT_NAME}
    # Copy the new version of the client to the clients package
    cp -r /tmp/test/${CLIENT_NAME}/swagger_client common_dibbs/clients/${CLIENT_NAME}
    # The following line is for compatibility
    cp -r /tmp/test/${CLIENT_NAME}/swagger_client common_dibbs/clients/rpa_client
else
    echo "Could not find the folder generated for ${CLIENT_NAME}, aborting :("
    exit 1
fi


exit 0