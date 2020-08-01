# Test run of our enviroment by simply picking a random action.
from SpaceENV import SpaceENV
from PIL import Image
import random
import csv

env = SpaceENV()
obs = env.reset()
env.render()

# Gets total number of actions available
action_length = env.action_space.n

# Test for 200 episodes
episodes = 1000
i = 1

scores = []

while i <= episodes:
    action = random.randint(0, action_length - 1)
    obs, reward, done, info = env.step(action)

    # Save our observation as an image
    im = Image.fromarray(obs[:, :, 0] * 255)
    im = im.convert("L")
    im.save("algo-view.jpeg")   

    env.render()

    if done:
        print(f"Episode {i}: {info['score']}")
        scores.append(info['score'])
        env.reset()
        i += 1

print(f"\n-------\nEpisodes: {episodes}\nAverage: {sum(scores)/len(scores)}\nMax: {max(scores)}\nMin: {min(scores)}\n-------")

# Create a csv of scores
with open("scores.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(scores)
