import json

# Load data from file
with open('ukol-3.json', encoding='utf-8') as f:
    data = json.load(f)

# Create new dictionary with pass/fail information
result = {}
for name, score in data.items():
    if score >= 60:
        result[name] = "Pass"
    else:
        result[name] = "Fail"

# Save result to file
with open('prospech.json', mode='w', encoding='utf-8') as soubor:
    json.dump(result, soubor, ensure_ascii=False)