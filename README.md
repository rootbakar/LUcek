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

Alive URL Check v1

# optional arguments:
  -h, --help            show this help message and exit
  
  -ms FILTER_STATUS, --filter-status FILTER_STATUS
  
                        Filter by status code(s), e.g., -ms 200 or -ms 200,302,404
                        
  -t MAX_THREADS, --max-threads MAX_THREADS
  
                        Max threads to use (default: 50)
                        
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
  
                        Output file name (default: results.txt)
                        
  -f INPUT_FILE, --input-file INPUT_FILE
  
                        Input file name
