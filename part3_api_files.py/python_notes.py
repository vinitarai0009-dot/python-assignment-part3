# ==================== Part A — Write ====================
# Write initial five lines (write mode)
with open("python_notes.txt", "w", encoding="utf-8") as f:
    f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    f.write("Topic 2: Lists are ordered and mutable.\n")
    f.write("Topic 3: Dictionaries store key-value pairs.\n")
    f.write("Topic 4: Loops automate repetitive tasks.\n")
    f.write("Topic 5: Exception handling prevents crashes.\n")
print("File written successfully.")

# Append two more lines (append mode)
with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions help organize reusable code.\n")
    f.write("Topic 7: Modules allow you to import external libraries.\n")
print("Lines appended.")

# ==================== Part B — Read ====================
# Read all lines
with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Print numbered lines (strip newline)
print("\n--- File Contents ---")
for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.rstrip('\n')}")

# Count and print total lines
print(f"\nTotal number of lines: {len(lines)}")

# Keyword search (case‑insensitive)
keyword = input("\nEnter a keyword to search for: ").lower()
matches = [line.rstrip('\n') for line in lines if keyword in line.lower()]

if matches:
    print(f"\nLines containing '{keyword}':")
    for match in matches:
        print(match)
else:
    print(f"\nNo lines contain the keyword '{keyword}'.")