from utils import ncr, prod


def compute():
    """
    70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.
    What is the expected number of distinct colours in 20 randomly picked balls?
    Give your answer with nine digits after the decimal point (a.bcdefghij).

    Let X_{i} = 1 if ith color present and 0 if not.
    X = \sum_{i=0}^{6} X_{i}
    E(X) = E(\sum_{i=0}^{6} X_{i})
         = \sum_{i=0}^{6} E(X_{i})
         = 7 * E(X_{0})
         = 7 * (1 - ncr(60, 20) / ncr(70, 20))
    """
    return 7 * (1 - ncr(60, 20) / ncr(70, 20))


if __name__ == "__main__":
    print(compute())
