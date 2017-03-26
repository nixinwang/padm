import time
import os
import multiprocessing
import argparse

"""I would like this script to allow user specify which command to run
   on multiple cores. User can also specify how many cores to be used.
   It will show how long it takes to finish that command on multi-cores."""

def run_cmd(cmd):
    os.system(cmd)

parser = argparse.ArgumentParser()
parser.add_argument('--cmd')
parser.add_argument('--num', type=int)

args = parser.parse_args()

# we are going to create args.num processes to run args.cmd command
pool = multiprocessing.Pool(processes=args.num)

start_time = time.time()

iteration = [args.cmd for i in range(args.num)]
result = pool.map(run_cmd, iteration)

end_time = time.time()
work_time = end_time - start_time

print(f'spent {str(work_time)}')

