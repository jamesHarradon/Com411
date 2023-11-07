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

#run_task2()


def observed_items2():
    observations = []
    while len(observations) < 5:
        observation = input("Please enter an observation:")
        observations.append(observation)
    return observations

# below is how to do a do while loop in python
def remove_observations(list_of_obs):
    while True:
        decision = input("Do you wish to remove an observation (yes/no) ?")
        if decision == "no":
            break
        obs = input("Please type the name of the observation you wish to remove: ")
        list_of_obs.remove(obs)
        print("Done!")

def run_task3():
    obs = observed_items2()
    remove_observations(obs)
    sorted(obs)
    obs_set = set()
    for value in obs:
        obs_set.add((value, obs.count(value)))
    for value in obs_set:
        print(f"{value[0]}")


run_task3()









