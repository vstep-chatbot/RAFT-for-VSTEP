import random
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(description='Train test split')
    parser.add_argument('--input', '-i', type=str, help='Input file', required=True)
    parser.add_argument('--ratio', '-r', type=float, help='Train ratio', default=0.85)
    args = parser.parse_args()
    return args


def run(input, ratio):
    with open(input, "r") as f:
        lines = f.readlines()
        random.shuffle(lines)
        split = int(len(lines) * ratio)
        train = lines[:split]
        test = lines[split:]
        base, ext = os.path.splitext(input)
        with open(base + "-train" + ext, "w") as f:
            f.writelines(train)
        with open(base + "-test" + ext, "w") as f:
            f.writelines(test)

if __name__ == "__main__":
    args = get_args()
    run(args.input, args.ratio)
