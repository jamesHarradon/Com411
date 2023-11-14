import json

def read(file_path):
    with open(file_path) as file:
        data = json.load(file)
        location = data["location"]
        population = data["population"]
        print(f"Place Name: {location}")
        print(f"Population Size: {population}")
        for bot in data["bots"]:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")

def run():
    read("futurama.json")

if __name__ == "__main__":
    run()