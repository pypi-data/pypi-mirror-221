# PastebinReaderPy

With this library you can read and run pastes

### Installation

```
pip install PastebinReaderPy
```

### Documentation
(**id** - https://pastebin.com/{**id**})

1. read_paste(paste_id:str) -> str
   - _This function return text of paste_
2. read_var_paste(paste_id:str) -> str
   - _This function return paste's varible_
3. run_paste(paste_id:str) -> None
   - _This function run paste's python code_

### Usage
```

>>> import pastebin as pr
>>> pr.read_paste('uQS3TJgS') # for reading example id = uQS3TJgS
'{\n    "English": "en",\n    "Chinese": "zh",\n    "Ukrainian": "uk",\n    "Polish": "pl"\n}'
>>> pr.read_var_paste('uQS3TJgS')
{'English': 'en', 'Chinese': 'zh', 'Ukrainian': 'uk', 'Polish': 'pl'}
>>> pr.run_paste('tLDZ9p7w') # for running example id = tLDZ9p7w
Hello, World!

```
