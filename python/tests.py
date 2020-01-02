import importlib
import time
import doctest
import sys
import argparse


filename = "../answers.txt"

with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    ANSWERS = {int(line.split(". ")[0]):
               line.split(". ")[1] for line in lines}


def test(prob, expected):
    try:
        module = importlib.import_module("p{:03d}".format(prob))
    except ImportError:

        raise ImportError(
            "It looks like you haven't solved #{prob} yet".format(prob=prob))
    start = time.time()
    actual = int(module.compute())  # Must return an int
    elapsed = int((time.time() - start) * 1000)
    print("Problem {:03d}: {:7d} ms".format(
        prob, elapsed),
        "" if actual == expected else "    *** FAIL ***")
    return elapsed


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', type=int, nargs='*')
    parser.add_argument('-g', '--graph', action='store_true',
                        help='graph execution time for selected problems')
    parser.add_argument('--doctest', action='store_true',
                                            help='run doctests on utils')
    args = parser.parse_args()
    return args


def main(doctests=False):
    args = get_args()
    results = dict()
    if len(args.numbers) > 0:
        for prob in args.numbers:
            try:
                results[prob] = test(prob, ANSWERS[prob])
            except KeyError:
                raise KeyError(
                    "It looks like you haven't added #{prob} to answers.txt yet".format(prob=prob))
        num_probs = len(args.numbers)
        prob_names = ", ".join(map(str, args.numbers))
    else:
        for (prob, expected) in sorted(ANSWERS.items()):
            results[prob] = test(prob, expected)
        num_probs = len(ANSWERS)
        prob_names = "(all)"
    total_time = sum(results.values())
    print("Total computation time: {} secs".format(total_time / 1000))
    print("{} problems solved".format(num_probs))
    if args.doctest:
        doctesting()
    if args.graph:
        graph(results, prob_names)


def doctesting():
    import utils
    doctest.testmod(utils, verbose=True)
    return 0


def graph(data, probs):
    import matplotlib.pyplot as plt
    from matplotlib import rc

    rc('text', usetex=True)
    plt.bar(data.keys(), data.values())
    plt.title(
        'Execution Time (secs) for Project Euler Problems {0}'.format(probs))
    plt.xlabel('Project Euler Problem Number')
    plt.ylabel('Execution Time (ms)')
    plt.show()


if __name__ == "__main__":
    main()
