from gym.envs.registration import register

register(
    id="gym_rlcc/rlcc-v0",
    entry_point="gym_rlcc.envs:RlccEnv",
)

register(
    id="gym_rlcc/rlcc-v1",
    entry_point="gym_rlcc.envs:RlccEnvMulti",
)
