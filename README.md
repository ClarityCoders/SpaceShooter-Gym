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
- install rest of dependencies listed in requirments.txt
