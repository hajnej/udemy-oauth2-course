# Exercise 3

**Get PKCE code verifier and challenge**

```bash
./setup.sh
python3 oauth-spa-exercise/main.py

# Sample output
# Generated code_challange is QyrQK9Y22UUOztGbJUdJLiJfleHbM3bRWt-IqKC4o54
# Generated code_verifier is Cr89gTYTGKapdv_NhonDNFpZR9Mn9QmlNyUxvFcntIXYXNXxcW8ODl2YRbi2Tmm3ElcZcmEVNwTBUUOeVD_DBXVpnBo3oaGz6-cT-09gJHApysgn6hW-IL8DQMfMezi3

```

**Sample Authorization request**

```
    https://dev-xxxxxx.okta.com/oauth2/default/v1/authorize?
      response_type=code&
      scope={YOUR_SCOPE}&
      client_id={YOUR_CLIENT_ID}&
      state={RANDOM_STRING}&
      redirect_uri=https://example-app.com/redirect&
      code_challenge={YOUR_CODE_CHALLENGE}&
      code_challenge_method=S256
```

**Sample cURL request to get access tokon**

```bash
    curl -X POST https://dev-xxxxxx.okta.com/oauth2/default/v1/token \
      -d grant_type=authorization_code \
      -d redirect_uri=https://example-app.com/redirect \
      -d client_id={YOUR_CLIENT_ID} \
      -d code_verifier={YOUR_CODE_VERIFIER} \
      -d code={YOUR_AUTHORIZATION_CODE}
```
