import requests

class GAuthPython:
    global server_url
    global open_url

    server_url = "https://server.gauth.co.kr"
    open_url = "https://open.gauth.co.kr/user"
    
    def ㅊ(email: str, password:str) -> str :
        URL = server_url + "/oauth/code"
        response = requests.post(URL, json={"email":email, "password" : password})
        return response.content
        
    def token_issuance(code : str, clientId: str, clientSecret: str, redirectUri: str) -> str :
        URL = "https://server.gauth.co.kr/oauth/token"
        response = requests.post(URL, json={"code" : code,
                                            "clientId": clientId,
                                            "clientSecret": clientSecret,
                                            "redirectUri" : redirectUri})
        return response.content
    
    def token_reissuance(refreshToken : str) -> str:
        URL = "https://server.gauth.co.kr/oauth/token"
        response = requests.patch(URL, headers={"refreshToken" : "Bearer" + refreshToken})

        return response.content
    
    def user_info(refreshToken : str) -> str:
        URL = "https://open.gauth.co.kr/user"
        response = requests.get(URL, headers={"Authorization": "Bearer" + refreshToken})

        return response.content