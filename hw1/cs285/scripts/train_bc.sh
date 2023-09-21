
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper-v4 \
--exp_name bc_hopper \
--n_iter 1 \
--expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 \
--train_batch_size 1024 \
--learning_rate 1e-5 \
--num_agent_train_steps_per_iter 100000 \
--eval_batch_size 10000 
