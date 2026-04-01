import requests

# ----------------------------------------------
# Step 1: Fetch 20 products and display in a table
# ----------------------------------------------
print("=== Step 1: Fetching 20 products ===")
url_20 = "https://dummyjson.com/products?limit=20"
response = requests.get(url_20)
response.raise_for_status()          # Stop if an error occurs
data = response.json()
products = data["products"]

# Print table header
print("\nID  | Title                          | Category      | Price    | Rating")
print("----|--------------------------------|---------------|----------|-------")

for p in products:
    # Format each field to align nicely
    title = p["title"][:30].ljust(30)
    category = p["category"][:15].ljust(15)
    price = f"${p['price']:.2f}".rjust(8)
    rating = f"{p['rating']:.2f}".rjust(6)
    print(f"{p['id']:3} | {title} | {category} | {price} | {rating}")

# ----------------------------------------------
# Step 2: Filter rating >= 4.5, sort by price descending
# ----------------------------------------------
filtered = [p for p in products if p["rating"] >= 4.5]
sorted_filtered = sorted(filtered, key=lambda x: x["price"], reverse=True)

print("\n=== Step 2: Products with rating ≥ 4.5 (sorted by price descending) ===")
print("ID  | Title                          | Category      | Price    | Rating")
print("----|--------------------------------|---------------|----------|-------")

for p in sorted_filtered:
    title = p["title"][:30].ljust(30)
    category = p["category"][:15].ljust(15)
    price = f"${p['price']:.2f}".rjust(8)
    rating = f"{p['rating']:.2f}".rjust(6)
    print(f"{p['id']:3} | {title} | {category} | {price} | {rating}")

# ----------------------------------------------
# Step 3: Fetch laptops category
# ----------------------------------------------
print("\n=== Step 3: Laptops category products ===")
url_laptops = "https://dummyjson.com/products/category/laptops"
response = requests.get(url_laptops)
response.raise_for_status()
laptops = response.json()["products"]

print("Name                               | Price")
print("-----------------------------------|----------")

for lap in laptops:
    name = lap["title"][:35].ljust(35)
    price = f"${lap['price']:.2f}".rjust(9)
    print(f"{name} | {price}")

# ----------------------------------------------
# Step 4: POST request (simulated)
# ----------------------------------------------
print("\n=== Step 4: Sending POST request to add a product ===")
post_url = "https://dummyjson.com/products/add"
payload = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}
response = requests.post(post_url, json=payload)
response.raise_for_status()
post_response = response.json()

print("Response from server:")
print(post_response)
