# Features

<img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/00a9d268-2086-4cf7-b778-144633d89093">

  * check status code
  * check web title
  * print url with status code
  * print url only
  * print url with title
  * print url with status code and title

# LUcek
`LUcek` is toolkit for checks the status of URLs to see if they are alive or not.

# Installation Instructions
`LUcek` requires python3.12 and pip3.12 to install successfully. Run the following command to get the repo: 

* Clone the LUcek repo
```bash
git clone https://github.com/rootbakar/LUcek.git
```
* Change directory to LUcek
```bash
cd LUcek
```
* Install requirement.sh (For Linux)
```bash
bash requirement.sh
```

* Install requirement.sh (For Mac)
```bash
bash requirement-mac.sh
```

# Usage
```bash
lucek -h
```
This will display help for the tool. Here are all the switches it supports.

```
Usage:
  lucek [options]

Options:
  -h, --help            show this help message and exit
  -ms FILTER_STATUS, --filter-status FILTER_STATUS
                        Filter by status code(s), e.g., -ms 200 or -ms
                        200,302,404
  -t MAX_THREADS, --max-threads MAX_THREADS
                        Max threads to use (default: 50)
  -f INPUT_FILE, --input-file INPUT_FILE
                        Input file name
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output file name (default: results.txt) with
                        full output
  -os OUTPUT_STATUS, --output-status OUTPUT_STATUS
                        Output file name (default: results.txt) with
                        only status code and URL
  -ot OUTPUT_TITLE, --output-title OUTPUT_TITLE
                        Output file name (default: results.txt) with
                        only URL and title
  -ou OUTPUT_URL, --output-url OUTPUT_URL
                        Output file name (default: results.txt) with
                        only URL
  --version             Display the current version of LUcek
```

# Running lucek
* Single target
```bash
echo "hackerone.com" | lucek
```
<img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/d7a5774b-524b-4837-b73a-3176b87f1c7d">



* Multiple Target with subfinder
```bash
subfinder -d hackerone.com -silent | lucek
```
<img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/48c690f4-97fa-4112-a69c-13c79ffab364">



* Multiple Target with file
```bash
cat subs.txt | lucek
```
<img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/f07505cd-c46e-47e1-b92a-211522ba1f3f">



* Multiple Target with assetfinder
```bash
assetfinder -subs-only hackerone.com | lucek
```
<img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/df3e756b-f6c9-4793-ac47-1148a56b82f1">


* Other command
```bash
assetfinder -subs-only hackerone.com | lucek -ms 200
```

```bash
subfinder -d hackerone.com -silent | lucek -ms 200,301,403
```

```bash
subfinder -d hackerone.com -silent | lucek -o all.txt
```

```bash
subfinder -d hackerone.com -silent | lucek -os only-status-code.txt
```

```bash
subfinder -d hackerone.com -silent | lucek -ot only-title.txt
```

```bash
subfinder -d hackerone.com -silent | lucek -ou only-url.txt
```

# Acknowledgement
This tools inspired by [httpx](https://github.com/projectdiscovery/httpx) and [httprobe](https://github.com/tomnomnom/httprobe)

