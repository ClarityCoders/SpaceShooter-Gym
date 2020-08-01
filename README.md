<a href="https://www.youtube.com/claritycoders"><img src="https://i.imgur.com/sG7xxyc.png" title="Clarity Coders YouTube" /></a>
# Custom SpaceShooter-Gym
> Custom gym to use with OpenAI algorithms. Showing how you can create more test environments for your custom alorithms.
> Once you get your enviroment setup in the OpenAI Gym format it is super easy to switch between different test algorithms. 

## Setup
- To use stable baselines you will need to install python 3.6 or 3.7
- Then install TensorFlow 1.15.0 ( Install GPU if you have one available or CPU to run on CPU )
```shell
pip install tensorflow==1.15      # CPU
pip install tensorflow-gpu==1.15  # GPU
```
- install OpenAI Gym and stable-baselines
```shell
pip install gym
pip install stable-baselines[mpi]
```
- install the rest of dependencies listed in requirments.txt

## Our Enviroment
- Uses inputs to the nural network (Observations) of pixes in the game include frames from the past. The shape is 252, 84, 1
- This allows our network to see which way enemies are moving to avoid collisions and shoot to score points.
<img src="https://i.imgur.com/OJ5JMUe.jpg" title="source: imgur.com" />
- The enviroment provides a reward to allow the network to learn from it's actions. The reward I chose if fairly simple at the start of the frame the reward is -0.001. This means if the AI just stays alive and never shoots enemies it will have a low reward score. If an enemy is hit the reward is increased by 1. If you touch an enemy the game is over and your reward is -2.
