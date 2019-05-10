def experiment(num_runs, model_factory, df):
    rewards = np.ndarray((len(df), num_runs))
    
    for run in range(num_runs):
        model = model_factory(len(df.columns)-1)
        for ix, row in df.iterrows():
            arm = model.pull()
            rewards[ix, run] = row[arm+1]
            model.feedback(arm, row[arm+1])

    c = 1 - rewards.cumsum(0) / df.values[:, 1:].max(1).cumsum(0).reshape(-1, 1)

    data=np.vstack((df.timestamp.values, c.mean(1), c.std(1))).transpose()
    return pd.DataFrame(data=data, columns=('timestamp', 'regret_mean', 'regret_std'))







from bandits import Bandit, experiment, NUM_RUNS

class EpsilonGreedy(Bandit):
    def __init__(self, n_arms, epsilon=.1):
        Bandit.__init__(self, n_arms)
        self.epsilon = epsilon
        self.reward_sum_per_arm = np.zeros(n_arms)
        self.actions_per_arm = np.zeros(n_arms)

    def pull(self):
        unpulled_arms = [_ for _ in range(self.n_arms) if self.actions_per_arm[_] < 1]
        if len(unpulled_arms):
            return np.random.choice(unpulled_arms)
        if np.random.random() < self.epsilon:
            arm = np.random.choice(np.arange(self.n_arms))
            return arm
        arms_weights = self.reward_sum_per_arm / self.actions_per_arm
        return np.argmax(arms_weights)

    def feedback(self, arm, reward):
        self.actions_per_arm[arm] += 1
        self.reward_sum_per_arm[arm] += reward
