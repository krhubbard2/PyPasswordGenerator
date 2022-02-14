# PyPasswordGenerator
Unique Password Generator with a GUI

## Setup
You will need Python3 and PyQt5 installed on your machine.
Clone this repository to wherever you'd like.
```bash
git clone "https://github.com/krhubbard2/PyPasswordGenerator"
```

## Running
```bash
cd PyPasswordGenerator
python3 pypasswordgenerator.py
```

## Usage
Set what limitations you want on your password (lowercase, uppercase, symbols) and set desired password length. Then click generate.


## Future implementations
### Copy Button
Automatically copy password to clipboard.
### Gaurantee at least one symbol, uppercase, or lowercase letter (depending on selection)
Currently it is possible for a password to be generated without the selected options, if length is filled with other selected options.
### Increase symbol reaccurance
Currently password is generated from 10 symbols -- being that there is 26 (52 if including uppercase) letters, there is much higher probability of getting all letters
### Force at least one selection
Currently users can unselect all boxes, a password of 0 characters.
