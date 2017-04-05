import os
import argparse
import time
import signal
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--cmd')
parser.add_argument('--num')
args = parser.parse_args()

curr_dir = os.path.dirname(os.path.abspath(__file__))
pare_dir = os.path.dirname(curr_dir)

cmd = f"python {os.path.join(curr_dir, 'run_task_multi_core.py')} --cmd '{args.cmd}' --num {args.num}"

def signal_handler(signal, frame):
    print('You pressed CTRL+C')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    start = time.time()
    os.system(cmd)
    stop = time.time()
    print(f"Used Time: {stop-start}")


