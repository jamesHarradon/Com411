def observed():
    # below is a set
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations

def run_task1():
    print(observed())


run_task1()



def observed_items():
    observations = []
    while len(observations) < 7:
        observation = input("Please enter an observation:")
        observations.append(observation)
    return observations


def run_task2():
    print("Counting observations...")
    obs_list = observed_items()
    obs_set = set()
    for value in obs_list:
        obs_set.add((value, obs_list.count(value)))
    print(obs_set)

run_task2()