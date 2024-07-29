import json



# To store the high score

def open_highscore():
    filename = "number.json"
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            return data["number"]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    
  


def get_highscore(number):
    filename = "number.json"
    data = {"number": number}
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
