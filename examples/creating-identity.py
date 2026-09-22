from bedrock_agentcore.services.identity import IdentityClient

identity_client= IdentityClient("us-east-1")

apikey_provider= identity_client.create_api_key_credential_provider({
    "name": "another-service-name",
    "apiKey": "your-api-key"
})
