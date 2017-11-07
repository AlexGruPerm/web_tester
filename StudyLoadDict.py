
dict_test_results = None
results_text_file = None

def get_pair(line):
    key, sep, value = line.strip().partition(" ")
    return int(key), value

with open("test_result.txt") as fd:
    dict_test_results = dict(get_pair(line) for line in fd)

