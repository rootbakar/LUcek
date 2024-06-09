# Features

  {screenshot}

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
<img width="1440" alt="image" src="https://github.com/rootbakar/LUcek/assets/43517550/5f2ca1d2-5bdf-42eb-a29f-4ec8503aee85">

* Multiple Target with subfinder
  
* Multiple Target with file
  
* Multiple Target with assetfinder
