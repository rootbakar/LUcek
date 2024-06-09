import sys
import argparse
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init()

def ensure_schema(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    return url

def check_url_status(url):
    url = ensure_schema(url)
    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        protocol = 'HTTPS' if response.url.startswith('https://') else 'HTTP'
        if status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'No title found'
        else:
            title = 'N/A'
        if protocol == 'HTTPS':
            url = url.replace('http://', 'https://')
        else:
            url = url.replace('https://', 'http://')
        return url, protocol, status_code, title
    except requests.exceptions.RequestException as e:
        return url, 'N/A', None, str(e)

def colorize_status_code_and_title(status_code, title):
    """Return colored status code and title based on the status code value."""
    if 200 <= status_code < 300:
        colored_status_code = f"{Fore.GREEN}{status_code}{Style.RESET_ALL}"
        colored_title = f"{Fore.GREEN}{title}{Style.RESET_ALL}"
    elif status_code == 404:
        colored_status_code = f"{Fore.RED}{status_code}{Style.RESET_ALL}"
        colored_title = f"{Fore.RED}{title}{Style.RESET_ALL}"
    elif 300 <= status_code < 400:
        colored_status_code = f"{Fore.YELLOW}{status_code}{Style.RESET_ALL}"
        colored_title = f"{Fore.YELLOW}{title}{Style.RESET_ALL}"
    elif status_code == 403:
        colored_status_code = f"{Fore.BLUE}{status_code}{Style.RESET_ALL}"
        colored_title = f"{Fore.BLUE}{title}{Style.RESET_ALL}"
    elif 500 <= status_code < 600:
        colored_status_code = f"{Fore.MAGENTA}{status_code}{Style.RESET_ALL}"
        colored_title = f"{Fore.MAGENTA}{title}{Style.RESET_ALL}"
    else:
        colored_status_code = f"{status_code}"
        colored_title = f"{title}"
    return colored_status_code, colored_title

def main():
    parser = argparse.ArgumentParser(description="Alive URL Check v1")
    parser.add_argument("-ms", "--filter-status", type=str, help="Filter by status code(s), e.g., -ms 200 or -ms 200,302,404")
    parser.add_argument("-t", "--max-threads", type=int, default=50, help="Max threads to use (default: 50)")
    parser.add_argument("-o", "--output-file", type=str, default="results.txt", help="Output file name (default: results.txt)")
    parser.add_argument("-f", "--input-file", type=str, help="Input file name")

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    max_threads = args.max_threads
    filter_status = [int(code) for code in args.filter_status.split(',')] if args.filter_status else None

    # Display figlet
    figlet_text = pyfiglet.figlet_format("RB - LUCEK")
    print(figlet_text)
    print("Alive URL Check v1\n")

    urls = []

    if input_file:
        with open(input_file, 'r') as file:
            urls = [url.strip() for url in file.readlines()]
    elif not sys.stdin.isatty():
        urls = [url.strip() for url in sys.stdin.readlines()]
    else:
        print("No input URLs provided.")
        return

    results = []

    start_time = time.time()  # Start timer

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for result in executor.map(check_url_status, urls):
            if result is not None:
                url, protocol, status_code, title = result
                if status_code is not None and (filter_status is None or status_code in filter_status):
                    colored_status_code, colored_title = colorize_status_code_and_title(status_code, title)
                    result = f'[{colored_status_code}] {url} [{colored_title}]'
                    results.append(result)
                    print(result)  # Print the result to see the progress

    end_time = time.time()  # End timer
    total_time = end_time - start_time  # Calculate total time

    with open(output_file, 'w') as file:
        for result in results:
            # Remove color codes for writing to the file
            clean_result = result.replace(Fore.GREEN, '').replace(Fore.RED, '').replace(Fore.YELLOW, '').replace(Fore.BLUE, '').replace(Fore.MAGENTA, '').replace(Style.RESET_ALL, '')
            file.write(clean_result + '\n')

    print(f'\nResults saved to {Fore.GREEN}{output_file}{Style.RESET_ALL}')
    print(f'Total time taken: {total_time:.2f} seconds')

if __name__ == '__main__':
    main()