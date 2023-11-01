# autogen
testing [autogen](https://github.com/microsoft/autogen)

## env
python version: 3.11.4  

## install packages
```zsh
pip install -r requirements.txt
```

## how to run 001
The only one requirement is an OpenAI API key.  

001 is to write FizzBuzz code in python and run the generated code.  
```zsh
cd 001
```

```zsh
cp .env.sample .env
```

Put the OpenAI API key into `.env` file.

```zsh
python app.py
```

medium
https://koji-kanao.medium.com/fizzbuzz-with-autogen-fb1a234f6588

## how to run 002
Install [LM Studio](https://lmstudio.ai/) and download a model.  
After downloading the model, start local server.  

```zsh
cd 002 && python app.py
```


