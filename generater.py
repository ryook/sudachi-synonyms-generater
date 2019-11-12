import argparse
import csv
import urllib.request


def main(fields):
    with open("synonyms.txt", "r") as f:
        reader = csv.reader(f)
        data = [r for r in reader]

    output_data = []
    synonym_set = []
    for line in data:
        if not line:
            if synonym_set:
                output_data.append(synonym_set)
            synonym_set = []
            continue

        if is_target(fields, line[7]):
            synonym_set.append(line[8])
    return output_data


def fetch_file():
    url = "https://raw.githubusercontent.com/WorksApplications/SudachiDict/develop/src/main/text/synonyms.txt"
    with urllib.request.urlopen(url) as r:
        with open("synonyms.txt", "w") as f:
            f.write(r.read().decode("utf-8"))


def is_target(fields: list, filed_info: str):
    if not fields:
        return True
    for field in fields:
        if field in filed_info:
            return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate synosyms from sudachi")
    parser.add_argument("file_name", type=str, help="output file name")
    parser.add_argument("--fields", type=str, help="targets field information")
    args = parser.parse_args()

    file_name = args.file_name
    fields = args.fields
    if not fields:
        fields = []
    else:
        fields = fields.split(",")

    fetch_file()
    output = main(fields)

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(output)
