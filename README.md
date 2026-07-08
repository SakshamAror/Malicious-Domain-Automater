## 🌟 Highlights

- This script makes it easier for you to check subjects for malicious intent through [VirusTotal](https://www.virustotal.com)
- It opens and closes tabs for you automatically so you can focus on analyzing the subjects rather than typing them in
- Suports parallel execution for speed
- It is a tool for your task, not a web scraping replacement


## 🚀 Usage
Run this command with a subjects.txt which should be a txt file of your subjects, one per line.

```py
>>> python domain_checker.py subjects.txt
Initializing with these subjects:
['amazon.com', 'yahoo.com', 'google.com']
Launching with default viewport ...
--- Safe Subject: amazon.com
Evaluation: No security vendors flagged this IP address as malicious
Rating: 0/91
-------- Perhaps Suspicious Subject: yahoo.com
Evaluation: At least 10 detected files embedding this domain
Rating: 0/91
-------- Perhaps Suspicious Subject: google.com
Evaluation: At least 8 detected files embedding this domain
Rating: 0/91
(Screenshots saved in /screenshots)
Suspicious Subjects: 0
[]
```


## ⬇️ Installation & Setup

### Download playwright
To run this script you either need to globally install the [playwright](https://playwright.dev/python/) python package or create a virtual environment to download the playwright package in. If you decide to download it globally, skip the first 2 steps:

Create virtual environment

```zsh
>>> python -m venv .venv
```

Activate virtual environment

```zsh
source .venv/bin/activate
```

Download playwright 
```zsh
pip install playwright
```

### Setup browser configuration

You have two options to set up the browser the script opens the tabs in. Either you link your own locally installed browser or download [playwright's supported browser binaries](https://playwright.dev/python/docs/browsers) to run on.

#### Option 1: Link your own chromium based browser
For playwright and this script to work properly, it is recommended to use chromium as your locally installed browser agent for this task. However, it should work fine with Google Chrome. Find the path to your Chrome executable file and put it in quotes in the chromium_path field found at the top of the domain_checker.py script in the SETTINGS section.

```py
chromium_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

Your path would look something like this on a MacOS device.

#### Option 2: Use playwright's supported browser binaries
The script defaults to this option if your chromium path doesn't point to a chromium executable. To download the chromium browser for playwright, enter this command in your terminal:

```zsh
playwright install --with-deps chromium
```


## 💭 Helper files

To produce your subjects.txt which should look something like this:

```txt
yahoo.com
google.com
24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c
```

**Note:** You don't need to name it subjects.txt but it must be a .txt file that you pass in as an input to domain_checker.py.

To create this subjects.txt, there are some helper scripts that parse some basic formats to extract subjects:

#### CSV/Excel Parser:
The csv_parser.py script 