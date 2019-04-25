def thompson():
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv('Routing_table_optimised.csv')

    # Implementing Thompson Sampling
    import random
    N = 10000
    d = 10
    router_selected = []
    numbers_of_rewards_1 = [0] * d
    numbers_of_rewards_0 = [0] * d
    total_reward = 0
    for n in range(0, N):
        router = 0
        max_random = 0
        for i in range(0, d):
            random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
            if random_beta > max_random:
                max_random = random_beta
                router = i
        router_selected.append(router)
        reward = dataset.values[n, router]
        if reward == 1:
            numbers_of_rewards_1[router] = numbers_of_rewards_1[router] + 1
        else:
            numbers_of_rewards_0[router] = numbers_of_rewards_0[router] + 1
        total_reward = total_reward + reward

    # Visualising the results - Histogram
    plt.hist(router_selected)
    plt.title('Histogram of routers selections')
    plt.xlabel('routers')
    plt.ylabel('Number of times each router was selected')
    plt.show()

if __name__ == '__main__':
    thompson();