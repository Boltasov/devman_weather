# Bitly URL shortener

The script executes two different functions:
* shortens your url and gives a bitlink as an output to terminal
* counts clicks to bitlink (in case if you provided bitlink as an argument)

### How to install

To use se script you need to get Bitly API token. Go [here](https://app.bitly.com/settings/api/), get a bitly account and generate your personal token.

This token you should put to a ```'.env'``` file. Create the file in the directory where ``main.py`` located. Put this to the ``.env`` file:
```
BITLY_TOKEN='Put_here_your_token'
```

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Start script
To execute script use terminal. Execute this command from the project directory:
```
python main.py your_url
```
It supports only full links including ``http:// or https://``.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).