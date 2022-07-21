# Exercise 3

**Get PKCE code verifier and challenge**

```bash
./setup.sh
python3 refresh-token-exercise/main.py

# Sample output
# Generated code_challange is QyrQK9Y22UUOztGbJUdJLiJfleHbM3bRWt-IqKC4o54
# Generated code_verifier is Cr89gTYTGKapdv_NhonDNFpZR9Mn9QmlNyUxvFcntIXYXNXxcW8ODl2YRbi2Tmm3ElcZcmEVNwTBUUOeVD_DBXVpnBo3oaGz6-cT-09gJHApysgn6hW-IL8DQMfMezi3

```

**Sample Authorization request**

_Note offline_access is not in list of scopes_

```
    https://dev-xxxxxx.okta.com/oauth2/default/v1/authorize?
      response_type=code&
      scope=offline_access+{YOUR_SCOPE}&
      client_id={YOUR_CLIENT_ID}&
      state={RANDOM_STRING}&
      redirect_uri=https://example-app.com/redirect&
      code_challenge={YOUR_CODE_CHALLENGE}&
      code_challenge_method=S256
```

**Sample cURL request to get access token**

```bash
    curl -X POST https://dev-xxxxxx.okta.com/oauth2/default/v1/token \
      -d grant_type=authorization_code \
      -d redirect_uri=https://example-app.com/redirect \
      -d client_id={YOUR_CLIENT_ID} \
      -d code_verifier={YOUR_CODE_VERIFIER} \
      -d code={YOUR_AUTHORIZATION_CODE}
```

**Sample cURL request to get access token using refresh token**

```bash
    curl -X POST https://dev-xxxxxx.okta.com/oauth2/default/v1/token \
      -d grant_type=refresh_token \
      -d client_id={YOUR_CLIENT_ID} \
      -d refresh_token={YOUR_REFRESH_TOKEN}
```
