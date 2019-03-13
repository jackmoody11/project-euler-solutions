# Call Mondays 0's, Tuesdays 1's, etc. until Sunday (6's)
# The day on January 1, 1901 = 365 - 7 * (365 // 7) = 1 (Tuesday)
# Then, there is a 4 year cycle of [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# times 3 and then for the 4th year, replace 28 with 29
# Make a list of 1's at every first of the month using this cycle
# Then check if the index has a remainder of 

# I didn't want to use the datetime module, because that seemed too easy (see p019.py)
# for a solution using the datetime module

def first_of_month():
    # Get list with 1's at indices where day is first of month
    # Jan. 1, 1901 - Dec. 31, 2000
    normal_helper = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    normal_cycle = [0] * 365
    for i in range(len(normal_helper)):
        normal_cycle[sum(normal_helper[:i])] = 1

    leap_helper = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_cycle = [0] * 365
    for i in range(len(leap_helper)):
        leap_cycle[sum(leap_helper[:i])] = 1
        
    full_cycle = normal_cycle * 3 + leap_cycle * 1
    return full_cycle * 25


def compute():
    is_first = first_of_month()
    count = 0
    for i in range(5, len(is_first), 7):
        if is_first[i]:
            count += 1
    return count

if __name__ == '__main__':
    print(compute())