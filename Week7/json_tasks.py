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


def read_task2(file_path):
    print("Reading...")
    with open(file_path) as file:
        data = json.load(file)
    print("Done!")
    return data

def save(file_path, data):
    print("Exporting...")
    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)
    print("Done!")

def run_task2():
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)

run_task2()