import httpx 

from helpers.files import create_dir, create_file

httpx_client: object = httpx.Client()
base_url: str = "https://discord.com/api/v9"

def get_friends(authorization_token: str) -> bool:
    create_dir("backup");create_file("friends")
    
    headers = {
        "Authorization": authorization_token, 
        "Content-Type": "application/json"
    }
    request: object = httpx_client.get(f"{base_url}/users/@me/relationships", headers=headers)
    
    if request.status_code == 200:
        for user in request.json():
            if str(user["type"]) == "1":
                user_id: int = user["user"]["id"]
                user_username: str = user["user"]["username"]
                user_discriminator: int = user["user"]["discriminator"]
                
                print(user_id, user_username, user_discriminator)
                
            else:
                pass
    else:
        return False