#!/bin/bash

#SBATCH --partition=gpu_a100          # Partition name
#SBATCH --gres=gpu:1                  # Number of GPUs to allocate
#SBATCH --cpus-per-task=9            # Number of CPU cores per task
#SBATCH --gpus=1                      # This line is sometimes optional/redundant depending on your system
#SBATCH --job-name=adv_bias       # Job name (customize)
#SBATCH --ntasks=1                    # Number of tasks
#SBATCH --time=02:00:00               # Time limit hh:mm:ss
#SBATCH --output=work/tiny_adv_bias_%A.out      # Standard output (%A expands to job ID)

### --- MODULE SETUP / ENVIRONMENT ---
module purge
module load 2023
# If your cluster requires loading an Apptainer module explicitly,
# for example: module load Apptainer/1.1.7 (adjust version as needed)
# module load Apptainer/<VERSION>

### --- APPTAINER RUN ---
# This command runs the container with GPU support (--nv) 
# and binds your local directories to the container's /local/ paths.
#
# The --pwd /local/work sets the container’s working directory to /local/work.

apptainer run --nv \
  --pwd /local/work \
  -B $(pwd)/data:/local/data \
  -B $(pwd)/cache:/local/cache \
  -B $(pwd)/work:/local/work \
  -B $(pwd)/src:/local/src \
  -B $(pwd)/scripts:/local/scripts \
  -B $(pwd)/configs:/local/configs \
  ./refact-multiarch-latest.sif \
  python /local/scripts/get_circuit.py --config_path ../configs/llama3_config_tiny_adv_bias.py

