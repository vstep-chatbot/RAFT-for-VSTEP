import json
import random

INPUT = "dist/gen1/chat.jsonl"


def run(input=INPUT, ratio=0.85):
    with open(input, "r") as f:
        lines = f.readlines()
        random.shuffle(lines)
        split = int(len(lines) * ratio)
        train = lines[:split]
        test = lines[split:]
        with open("train.jsonl", "w") as f:
            f.writelines(train)
        with open("test.jsonl", "w") as f:
            f.writelines(test)


def convert_ini(input="dist/gen1/train_test/test_sgu.ini"):
    with open(input, "r") as f:
        lines = f.readlines()
        with open("test_sgu.json", "w") as f:
            for line in lines:
                f.write(json.dumps({"question": line.strip()}, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    # run()
    convert_ini()
