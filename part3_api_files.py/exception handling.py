import requests

# ===================== Part A: Guarded Calculator =====================
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print("=== Part A: Safe Divide ===")
print(f"safe_divide(10, 2)  -> {safe_divide(10, 2)}")
print(f"safe_divide(10, 0)  -> {safe_divide(10, 0)}")
print(f"safe_divide('ten', 2) -> {safe_divide('ten', 2)}")
print()

# ===================== Part B: Guarded File Reader =====================
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print("=== Part B: Safe File Reader ===")
print("Testing with 'python_notes.txt' (should exist):")
read_file_safe("python_notes.txt")
print("Testing with 'ghost_file.txt' (should fail):")
read_file_safe("ghost_file.txt")
print()

# ===================== Part C: Robust API Calls =====================
def fetch_products_with_exception_handling():
    url = "https://dummyjson.com/products?limit=20"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raises HTTPError for 4xx/5xx
        data = response.json()
        print("Successfully fetched 20 products.")
        # Optionally print first product title as demonstration
        print(f"First product: {data['products'][0]['title']}")
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"Unexpected error: {e}")

print("=== Part C: Robust API Call ===")
fetch_products_with_exception_handling()
print()

# ===================== Part D: Input Validation Loop =====================
def product_lookup_loop():
    while True:
        user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Validate integer and range
        try:
            product_id = int(user_input)
            if not (1 <= product_id <= 100):
                print("Warning: Product ID must be between 1 and 100. Please try again.")
                continue
        except ValueError:
            print("Warning: Please enter a valid integer or 'quit'.")
            continue
        
        # Make the API request with error handling
        url = f"https://dummyjson.com/products/{product_id}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 404:
                print("Product not found.")
            elif response.status_code == 200:
                product = response.json()
                print(f"Title: {product['title']}, Price: ${product['price']}")
            else:
                print(f"Unexpected status code: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print("Connection failed. Please check your internet.")
        except requests.exceptions.Timeout:
            print("Request timed out. Try again later.")
        except Exception as e:
            print(f"Unexpected error: {e}")

print("=== Part D: Product Lookup Loop ===")
product_lookup_loop()