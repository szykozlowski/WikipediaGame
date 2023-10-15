# WikipediaGame

## Installation

(these instructions are for GnuLinux/Macos)

Prerequisites: Python

```
git clone https://github.com/alexhkurz/WikipediaGame.git
cd WikipediaGame/server
source setup.sh
```

Starting the server:

```
python server.py
```

(For development one may want to use `watchmedo auto-restart -d . -p '*.py' -- python server.py`.)

Go to [`localhost:5000`](http://127.0.0.1:5000/).

## Branches

- `version1` computes the shortest path betwen two wikipedia pages
- `version2` (=`main`) additionally displays all pages visited during the computation
- `dev` is an unfinished attempt at outputting the pages being visited in real time



