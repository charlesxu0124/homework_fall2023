# python cs285/scripts/run_hw3_sac.py -cfg experiments/sac/sanity_invertedpendulum_reinforce.yaml --seed 1
# python cs285/scripts/run_hw3_sac.py -cfg experiments/sac/sanity_invertedpendulum_reparametrize.yaml --seed 1

python cs285/scripts/run_hw3_sac.py -cfg experiments/sac/halfcheetah_reinforce1.yaml --seed 1 &
python cs285/scripts/run_hw3_sac.py -cfg experiments/sac/halfcheetah_reinforce10.yaml --seed 1