from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends

# Recupera el token
securityBearer = HTTPBearer()

@app.get('/')
def root(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    token = credential.credentials
    if token = "12treS":
        return{"auth": True}
    else
        return{"auth": False}
    