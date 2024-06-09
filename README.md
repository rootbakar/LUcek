# Features

  <img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/15e999f3-fd36-47b3-b117-af044a50b1e2">


  * check status code
  * check web title
  * print url with status code
  * print url only
  * print url with title
  * print url with status code and title

# LUcek
`LUcek` is toolkit for checks the status of URLs to see if they are alive or not.

# Installation Instructions
`LUcek` requires python3.8 and pip3.8 to install successfully. Run the following command to get the repo: 

* Clone the LUcek repo
```bash
git clone https://github.com/rootbakar/LUcek.git
```
* Change directory to LUcek
```bash
cd LUcek
```
* Install requirement.sh
```bash
bash requirement.sh
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
echo "progress28.com" | lucek
```
<img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/6623a780-b106-4bf4-aece-b0212e1ccdb0">


* Multiple Target with subfinder
```bash
subfinder -d progress28.com | lucek
```
<img width="1440" alt="Screenshot 2024-06-09 at 16 11 36" src="https://github.com/rootbakar/LUcek/assets/43517550/3849742b-67ed-4f32-8259-96a8503c9a87">


* Multiple Target with file
```bash
cat subs.txt | lucek
```
<img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/fd641a2b-8b70-41fa-bf5a-d21f73c34108">


* Multiple Target with assetfinder
```bash
assetfinder -subs-only progress28.com | lucek
```
<img width="1440" alt="Screenshot 2024-06-09 at 16 14 43" src="https://github.com/rootbakar/LUcek/assets/43517550/a2137890-8682-4868-a2e8-8046ebca1837">

# Acknowledgement
This tools inspired by [httpx](https://github.com/projectdiscovery/httpx) and [httprobe](https://github.com/tomnomnom/httprobe)

