# This solution would not have been possible without https://blog.dreamshire.com/project-euler-54-solution/
# It took a while for me to fully understand what was happening, but I have worked through it and made
# comments to try and clarify what is happening in this concise and powerful code piece

from collections import Counter

hands = (line.split() for line in open('p054.txt'))

# Convert cards to numbers
# T, J, Q, K, A = 10, 11, 12, 13, 14
VALUES = {r: i for i, r in enumerate('23456789TJQKA', 2)}
STRAIGHTS = [(v, v-1, v-2, v-3, v-4)
             for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
# high card, one pair, two pair, three of a kind, straight, flush, full house, four of a kind
RANKS = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1),
         (3, 1, 1), (), (), (3, 2), (4, 1)]


def hand_rank(hand):
    """
    Count number of each card
    Ex: ['8C', 'TS', 'KC', '9H', '4S']  =>
    [(1, 13), (1, 10), (1, 9), (1, 8), (1, 4)]  =>
    [(1, 1, 1, 1, 1), (13, 10, 9, 8, 4)]
    """
    score_zip = zip(*sorted(((v, VALUES[k]) for
                             k, v in Counter(x[0] for x in hand).items()), reverse=True))
    score = list(score_zip)
    score[0] = RANKS.index(score[0])

    if len(set(card[1] for card in hand)) == 1:
        score[0] = 5  # flush

    if score[1] in STRAIGHTS:
        if score[0] == 5:
            score[0] = 8 
        else:
            score[0] = 4
    return score


def compute():
    """
    Since tuples can be compared, royal flushes will have a score > straight flush
    Ex: [8, (9, 8, 7, 6, 5)] < [8, (14, 13, 12, 11, 10)]
    """
    return sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands)


if __name__ == "__main__":
    print(compute())
