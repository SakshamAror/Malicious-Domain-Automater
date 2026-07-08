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

It opens tabs for you in headed mode so you can oversee the operation and look at the subject evaluations in real time. It waits for a short period of time (so you can glance at the reports), then pulls the subject data shown on virustotal and outputs it in your terminal.  It also saves screenshots of malicious subjects in /screenshots and saves a logs.txt with the ratings and evaluations of all subjects listed.

There are a few settings you can change to modify the execution. These settings are found at the top of **domain_checker.py**:

#### pause_time
You can modify the time it pauses for before going to the next tab by changing the pause_time variable

```py
pause_time = 1
```

#### timeout
timeout controls how long the task runs before it exits and asks you to decide whether to try again or quit. At this point, you may check your browser to investigate whether the site is down or something else may be causing the issue. If you set the timeout to be too low, normal network noise may cause this too trigger very often, requiring a lot of human intervention.

```py
timeout = 10
```

#### no_parallel
This variable modifies how many tabs open at once in the browser for faster parallel execution

```py
no_parallel = 5
```

#### headless_mode
If headless_mode is set to True, the tabs are run in an headless shell where you can't see the tabs. It is highly recommended to not turn it on because you won't be able to debug when something goes wrong.

```py
headless_mode = False
```

#### default_settings
This sets the viewport and window size of the opened browser to default settings

```py
default_settings = True
```

#### exec_settings
Here you can configure the exact dimensions of the viewport and window for your opened browser. However, first you need to set the screen width and height with your screen's values:

```py
screen_height = 1000
screen_width = 1500
```

Then, you may set the settings for your browser dimension. The first item is the height of the browser, the second is the width, and the last two are the x and y positions of the bottom left point of the browser respectively.

```py
# If any of the positions are a negative number, load in fullscreen
exec_settings = [screen_height, screen_width, 0, 0]
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


## 💭 Subjects.txt and helper script

Your subjects.txt should have one subject per line without any extra characters (trailling spaces will be automatically removed). It should look something like this:

```txt
yahoo.com
google.com
24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c
```

**Note:** You don't need to name it subjects.txt but it must be a .txt file that you pass in as an input to domain_checker.py.

To create this subjects.txt, there is a helper script that parses a csv file.

#### CSV/Excel Parser:
The csv_parser.py script parses a given csv file for subjects from a given column. If you have an excel file, import/download it as a .csv file and input that to the script. The script will save the subjects in subjects.txt.