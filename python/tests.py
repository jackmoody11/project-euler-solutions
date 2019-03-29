import importlib, time


filename = "../answers.txt"

with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    ANSWERS = {int(line.split(". ")[0]): int(line.split(". ")[1]) for line in lines}

def main():
	total_time = 0.0  # In seconds
	for (prob, expected) in sorted(ANSWERS.items()):
		module = importlib.import_module("p{:03d}".format(prob))
		starttime = time.time()
		actual = int(module.compute())  # Must return an int
		elapsedtime = time.time() - starttime
		total_time += elapsedtime
		print("Problem {:03d}: {:7d} ms{}".format(
			prob, int(round(elapsedtime * 1000)),
			"" if actual == expected else "    *** FAIL ***"))
	print("Total computation time: {} ms".format(int(round(total_time * 1000))))
	print("{} problems solved".format(len(ANSWERS)))


if __name__ == "__main__":
    main()
