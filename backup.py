import json

class BackupCord:
    def __init__(self, account_authorization) -> None:
        self.token: str = account_authorization
        
        print(self.token)
        
    def backup_friends(self) -> bool:
        print("hello world")

if __name__ == "__main__":
    try:
        data = json.load(open("config.json"))
        
        client = BackupCord(account_authorization=data["token"])
        client.backup_friends()
    except:
        exit(code=None)
