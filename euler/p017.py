letters = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
           6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
           16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
           30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
           90: "ninety", 100: "onehundred", 1000: "onethousand"}


def count_letters(n):
        # Catch 1-20, multiples of 10 up to 100 and 1000
    if n in letters.keys():
        return letters[n]
    # Catch numbers not caught up to 100
    elif 20 < n < 100:
        tens = n // 10
        ones = n - tens * 10
        return letters[tens * 10] + letters[ones]
    # Catch 200, 300, ..., 900
    elif n % 100 == 0:
        hundreds = n // 100
        return letters[hundreds] + "hundred"
    # Catch 110, 120, .., 990
    elif n % 10 == 0:
        hundreds = n // 100
        tens = n // 10 - hundreds * 10
        return letters[hundreds] + "hundred" + "and" + letters[tens * 10]
    # Catch 111-119, 211-219, ...
    elif n % 100 < 20:
        hundreds = n // 100
        rest = n - hundreds * 100
        return letters[hundreds] + "hundred" + "and" + letters[rest]
    # Catch 121-129, 131-139, ..., 991-999
    else:
        hundreds = n // 100
        tens = n // 10 - hundreds * 10
        ones = n - hundreds * 100 - tens * 10
        if tens == 0:
            return letters[hundreds] + "hundred" + "and" + letters[ones]
        else:
            return letters[hundreds] + "hundred" + "and" + letters[tens * 10] + letters[ones]


letter_count = 0
for i in range(1, 1001):
    letter_count += len(count_letters(i))

print(letter_count)
