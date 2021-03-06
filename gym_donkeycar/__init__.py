# -*- coding: utf-8 -*-

"""Top-level package for OpenAI Gym Environments for Donkey Car."""

__author__ = """Tawn Kramer"""
__email__ = 'tawnkramer@gmail.com'
__version__ = '1.0.14'

from gym.envs.registration import register
from .envs.donkey_env import GeneratedRoadsEnv, WarehouseEnv, AvcSparkfunEnv, GeneratedTrackEnv
#from .envs.vae_env import DonkeyVAEEnv
'''
register(
    id='DonkeyVae-v0',
    entry_point='gym_donkeycar.envs.vae_env:DonkeyVAEEnv',
    max_episode_steps=None,
)
'''

register(
    id='donkey-generated-roads-v0',
    entry_point='gym_donkeycar.envs.donkey_env:GeneratedRoadsEnv',
)

register(
    id='donkey-warehouse-v0',
    entry_point='gym_donkeycar.envs.donkey_env:WarehouseEnv',
)

register(
    id='donkey-avc-sparkfun-v0',
    entry_point='gym_donkeycar.envs.donkey_env:AvcSparkfunEnv',
)

register(
    id='donkey-generated-track-v0',
    entry_point='gym_donkeycar.envs.donkey_env:GeneratedTrackEnv',
)

register(
    id='donkey-ironcar-track-v0',
    entry_point='gym_donkeycar.envs.donkey_env:IroncarTrackEnv',
)

register(
    id='donkey-chicane-track-v0',
    entry_point='gym_donkeycar.envs.donkey_env:ChicaneTrackEnv',
)

register(
    id='donkey-circle-track-v0',
    entry_point='gym_donkeycar.envs.donkey_env:CircleTrackEnv',
)
