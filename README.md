# autogen
testing [autogen](https://github.com/microsoft/autogen)

## env
python version 3.11.4


## how to run
The only one requirement is an OpenAI API key.  

001 is to write FizzBuzz code in python and run the generated code.  
```zsh
cd 001 && pip install -r requirements.txt
```

```zsh
cp .env.sample .env
```

Put the OpenAI API key into `.env` file.

```zsh
python app.py
```
