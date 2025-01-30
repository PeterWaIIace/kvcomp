import json
import argparse
from termcolor import colored

def load_file(path):
    with open(path, "r") as f:
        return json.load(f)

def kvcomp(j1,j2):
    only_in_j1 = dict()
    diff_j1_j2 = dict()
    only_in_j2 = dict()

    for key, value in j1.items():
        if key in j2:
            if j2[key] != j1[key]:
                diff_j1_j2[key] = j2[key]
                j2.pop(key)
        else:
            only_in_j1[key] = j1[key]

    only_in_j2 = j2
    return (only_in_j1,diff_j1_j2,only_in_j2)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process two JSON files.")
    parser.add_argument('file1', type=str, help="Path to the first JSON file")
    parser.add_argument('file2', type=str, help="Path to the second JSON file")

    args = parser.parse_args()

    j1 = load_file(args.file1)
    j2 = load_file(args.file2)

    only_in_j1,diff_j1_j2,only_in_j2 = kvcomp(j1,j2)

    print("Unique first JSON file content:")
    print(colored(json.dumps(only_in_j1, indent=4), 'green'))
    print("\nDifferent values between JSON files:")
    print(colored(json.dumps(diff_j1_j2, indent=4), 'yellow'))
    print("\nUnique second JSON file content:")
    print(colored(json.dumps(only_in_j2, indent=4), 'red'))