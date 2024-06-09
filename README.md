# lucek
This script checks the status of URLs to see if they are alive or not.

# usage
lucek.py [-h] [-ms FILTER_STATUS] [-t MAX_THREADS] [-o OUTPUT_FILE] [-f INPUT_FILE]

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
