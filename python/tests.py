import importlib, time
import doctest
import sys

filename = "../answers.txt"

with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    ANSWERS = {int(line.split(". ")[0]): int(line.split(". ")[1]) for line in lines}

def test(prob, expected):
	try:
		module = importlib.import_module("p{:03d}".format(prob))
	except ModuleNotFoundError:
		raise ModuleNotFoundError("It looks like you haven't solved #{prob} yet".format(prob=prob))
	start = time.time()
	actual = int(module.compute())  # Must return an int
	elapsed = time.time() - start
	print("Problem {:03d}: {:7d} ms{}".format(
		prob, int(round(elapsed * 1000)),
		"" if actual == expected else "    *** FAIL ***"))

def main(doctests=False):
	start = time.time()  # In seconds
	if len(sys.argv) > 1:
		for prob in list(map(int, sys.argv[1:])):
			try:
				test(prob, ANSWERS[prob])
			except KeyError:
				raise KeyError("It looks like you haven't added #{prob} to answers.txt yet".format(prob=prob))
		num_probs = len(sys.argv[1:])
	else:
		for (prob, expected) in sorted(ANSWERS.items()):
			test(prob, expected)
		num_probs = len(ANSWERS)
	total_time = time.time() - start
	print("Total computation time: {} ms".format(int(round(total_time * 1000))))
	print("{} problems solved".format(num_probs))

	if doctests:
		doctesting()

def doctesting():
	import utils
	doctest.testmod(utils)
	return 0


if __name__ == "__main__":
    main()
