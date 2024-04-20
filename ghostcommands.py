import sys
import random
import time
import subprocess

def execute_command(args):
    # Random chance to introduce a fake error or delay
    if random.randint(0, 4) == 0:  # 20% chance for anomalies
        if random.choice([True, False]):
            # Introduce a fake error message
            print("bash: {}: command not found".format(args[0]))
        else:
            # Introduce a delay
            time.sleep(random.uniform(1, 3))
            # Then execute the command normally
            subprocess.run(args)
    else:
        # Execute the command normally
        subprocess.run(args)

if __name__ == "__main__":
    execute_command(sys.argv[1:])
