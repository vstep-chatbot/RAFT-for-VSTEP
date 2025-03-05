import json
import argparse
import re

def get_args():
    parser = argparse.ArgumentParser(description='Format finetune data')
    parser.add_argument('--input', '-i', type=str, help='Input file')
    parser.add_argument('--output', '-o', type=str, help='Output file')
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    if (args.input is None) or (args.output is None) or (args.input == args.output):
        print('Invalid input/output')
        return
    with open(args.input, 'r') as f:
        lines = f.readlines()
    with open(args.output, 'w') as f:
        for line in lines:
            data = json.loads(line)
            try:              
                data['messages'][1]['content'] = re.sub(r'<DOCUMENT>.+?</DOCUMENT>(\n)+', '', data['messages'][1]['content'])
                data['messages'][2]['content'] = re.search(r'<ANSWER>:\s(.+)', data['messages'][2]['content']).group(1)
            except Exception as e:
                print('Error processing line', e)
                print(data['messages'])
                return
            f.write(json.dumps(data, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    main()