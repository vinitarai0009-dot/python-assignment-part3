import requests
from datetime import datetime

def log_error(context, error_type, details):
    """
    Write a timestamped error entry to error_log.txt.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] ERROR in {context}: {error_type} — {details}\n"
    with open("error_log.txt", "a", encoding="utf-8") as f:
        f.write(log_line)

# ========== 1. Trigger a ConnectionError ==========
print("Triggering a ConnectionError...")
unreachable_url = "https://this-host-does-not-exist-xyz.com/api"
try:
    requests.get(unreachable_url, timeout=3)
except requests.exceptions.ConnectionError as e:
    log_error("fetch_products", "ConnectionError", str(e))
    print("Logged ConnectionError.")

# ========== 2. Trigger an HTTP error (404) ==========
print("Triggering an HTTP 404 error...")
product_id = 999
url = f"https://dummyjson.com/products/{product_id}"
try:
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        log_error("lookup_product", f"HTTPError — {response.status_code}", 
                  f"{response.status_code} Not Found for product ID {product_id}")
        print("Logged HTTP 404 error.")
except Exception as e:
    # In case of any other network error, also log it
    log_error("lookup_product", type(e).__name__, str(e))

# ========== 3. Read and print the log file ==========
print("\n--- Contents of error_log.txt ---")
try:
    with open("error_log.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No log file found.")