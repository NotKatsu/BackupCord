import os 

def create_dir(folder_name: str) -> bool: 
    if os.path.exists(f"./{folder_name}"):
        return False
    else:
        try:
            os.mkdir(f"./{folder_name}")
            return True
        except:
            return False
        
def create_file(dir_name: str, file_name: str) -> bool: 
    if os.path.exists(f"./{dir_name}"):
        with open(f"./{dir_name}/{file_name}.txt", 'w') as f:
            f.close()
            return True
    else:
        return False
