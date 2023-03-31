import json

from helpers.friends import get_friends

class BackupCord:
    def __init__(self, account_authorization) -> None:
        self.token: str = account_authorization
                
    def backup_friends(self) -> bool:
        return get_friends(self.token)

if __name__ == "__main__":
    try:
        data = json.load(open("config.json"))
        
        client = BackupCord(account_authorization=data["token"])
        client.backup_friends()
    except:
        exit(code=None)
