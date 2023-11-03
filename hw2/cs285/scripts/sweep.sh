# for LAMBDA in 0 0.95 0.98 0.99 1; do
#     inner_pids=()  # Use an array to collect PIDs of inner loop processes


#     for seed in $(seq 1 3); do

#         python cs285/scripts/run_hw2.py --env_name InvertedPendulum-v4 -n 100 \
#         --exp_name pendulum_b2000_bgs10 \
#         -rtg --use_baseline -na \
#         --batch_size 2000 \
#         --seed $seed \
#         --gae_lambda $LAMBDA \
#         -bgs 10 &

#         inner_pids+=($!)  # Collect the PID of the last backgrounded process
#     done

#     # Wait for all inner loop processes to complete before moving to next LAMBDA
#     for pid in "${inner_pids[@]}"; do
#         wait $pid
#     done
# done

for seed in $(seq 1 5);
do
    python cs285/scripts/run_hw2.py \
    --env_name InvertedPendulum-v4 \
    -n 100 --exp_name pendulum_b2000_bgs10 \
    -rtg --use_baseline -na \
    --batch_size 2000 --seed 2 \
    --gae_lambda 0.98 -bgs 10 
done