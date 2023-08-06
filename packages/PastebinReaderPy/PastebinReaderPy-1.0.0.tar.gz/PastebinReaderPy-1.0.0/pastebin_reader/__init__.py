from requests import get

def read_paste(paste_id:str):
    text = get(f"https://pastebin.com/raw/{paste_id}").text
    text = text.replace("\r", "") # clear text
    return text

def read_var_paste(paste_id:str):
    text = read_paste(paste_id)
    text = text.replace("\n", "").replace("\t", "").replace("\r", "").replace("    ", "") # clear text
    exec(f"globals()['res'] = {text}")
    return res

def run_paste(paste_id:str):
    exec(read_paste(paste_id))
