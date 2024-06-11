#!/usr/bin/env python3

import sys
import argparse
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time
from colorama import Fore, Style, init
import pyfiglet
import re
import os
from tqdm import tqdm

# Initialize colorama
init()

def ensure_schema(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    return url

def is_html(content):
    """Check if the content contains basic HTML tags."""
    return bool(re.search(r'<html.*?>.*?</html>', content, re.DOTALL | re.IGNORECASE))

def check_url_status(url):
    url = ensure_schema(url)
    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        protocol = 'HTTPS' if response.url.startswith('https://') else 'HTTP'
        if status_code == 200 and is_html(response.text):
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
        return url, 'N/A', None, 'Failed to open page'

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

def format_result(output_type, colored_status_code, url, colored_title):
    """Format the result based on the specified output type."""
    if output_type == '-o':
        return f'[{colored_status_code}] {url} [{colored_title}]'
    elif output_type == '-os':
        return f'[{colored_status_code}] {url}'
    elif output_type == '-ot':
        return f'{url} [{colored_title}]'
    elif output_type == '-ou':
        return f'{url}'
    else:
        return f'[{colored_status_code}] {url} [{colored_title}]'

def update_script():
    script_path = "/usr/local/bin/lucek"
    print(f"{Fore.BLUE}Updating LUcek script at {script_path}...{Style.RESET_ALL}")
    try:
        url = "https://raw.githubusercontent.com/rootbakar/LUcek/main/lucek.py"

        response = requests.get(url)
        if response.status_code == 200:
            with open(script_path, "wb") as file:
                file.write(response.content)

            # Ensure the new script is executable
            os.chmod(script_path, 0o755)
            os.system("python3.12 -m pip install tqdm")
            print(f"{Fore.GREEN}Update completed successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Failed to fetch the latest script from GitHub. Status code: {response.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Failed to update script: {e}{Style.RESET_ALL}")

def get_github_script():
    try:
        url = "https://raw.githubusercontent.com/rootbakar/LUcek/main/lucek.py"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"{Fore.RED}Failed to fetch the latest script from GitHub. Status code: {response.status_code}{Style.RESET_ALL}")
        return None
    except Exception as e:
        print(f"{Fore.RED}Failed to fetch latest version: {e}{Style.RESET_ALL}")
        return None

def check_version_status():
    github_script = get_github_script()
    if github_script:
        local_script_path = "/usr/local/bin/lucek"
        try:
            with open(local_script_path, "r") as file:
                local_script = file.read()
            if local_script == github_script:
                return f"{Fore.BLUE}latest{Style.RESET_ALL}"
            else:
                return f"{Fore.RED}outdated{Style.RESET_ALL}"
        except Exception as e:
            print(f"{Fore.RED}Failed to read local script: {e}{Style.RESET_ALL}")
            return f"{Fore.RED}unknown{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}unknown{Style.RESET_ALL}"

def main():
    parser = argparse.ArgumentParser(description="alive URL check by rootbakar")
    parser.add_argument("-ms", "--filter-status", type=str, help="Filter by status code(s), e.g., -ms 200 or -ms 200,302,404")
    parser.add_argument("-t", "--max-threads", type=int, default=50, help="Max threads to use (default: 50)")
    parser.add_argument("-f", "--input-file", type=str, help="Input file name")
    parser.add_argument("-o", "--output-file", type=str, help="Output file name (default: results.txt) with full output")
    parser.add_argument("-os", "--output-status", type=str, help="Output file name (default: results.txt) with only status code and URL")
    parser.add_argument("-ot", "--output-title", type=str, help="Output file name (default: results.txt) with only URL and title")
    parser.add_argument("-ou", "--output-url", type=str, help="Output file name (default: results.txt) with only URL")
    parser.add_argument("--version", action="store_true", help="Display the current version of LUcek")
    parser.add_argument("--update", action="store_true", help="Update the LUcek script to the latest version")

    args = parser.parse_args()

    if args.update:
        update_script()
        return

    version_status = check_version_status()

    # Display figlet
    figlet_text = pyfiglet.figlet_format("RB - LUcek")
    print(figlet_text)
    print("alive URL check by rootbakar\n")
    print(f"[{Fore.BLUE}INF{Style.RESET_ALL}] Current LUcek version v1.0.3 [{version_status}]\n")

    input_file = args.input_file
    output_file = args.output_file or args.output_status or args.output_title or args.output_url or "results.txt"
    max_threads = args.max_threads
    filter_status = [int(code) for code in args.filter_status.split(',')] if args.filter_status else None
    output_type = '-o' if args.output_file else '-os' if args.output_status else '-ot' if args.output_title else '-ou' if args.output_url else '-o'

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
                    if title and "Failed to open page" not in title and title != "52 Mercusuar - Situs Tidak Ditemukan" and title != "Mercusuar - Situs Tidak Ditemukan":
                        colored_status_code, colored_title = colorize_status_code_and_title(status_code, title)
                        formatted_result = format_result(output_type, colored_status_code, url, colored_title)
                        results.append(formatted_result)
                        print(formatted_result)  # Print the result to see the progress

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
