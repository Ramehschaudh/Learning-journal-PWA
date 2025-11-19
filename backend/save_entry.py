import json
from datetime import datetime

JSON_FILE = 'reflections.json'

def main():
    print("\n--- Add Reflection via Python ---")
    reflection_text = input("Type your reflection: ")
    
    new_entry = {
        "id": int(datetime.now().timestamp() * 1000),  # Match JS Date.now()
        "date": datetime.now().isoformat(),  # Match JS toISOString()
        "text": reflection_text
    }
    
    try:
        with open(JSON_FILE, 'r') as file:
            reflections = json.load(file)
    except FileNotFoundError:
        reflections = []
    
    reflections.append(new_entry)
    
    with open(JSON_FILE, 'w') as file:
        json.dump(reflections, file, indent=4)
    
    print(" Reflection saved to JSON file!")

if __name__ == "__main__":
    main()