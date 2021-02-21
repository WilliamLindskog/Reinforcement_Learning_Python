def learn():
    for t in range(nbr_steps):
        data = runner.run()
        agent.train(data)