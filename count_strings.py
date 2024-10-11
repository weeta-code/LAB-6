# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu
# Spire IDs : 34569497

def count_strings(lst: list, n: int):
    count = 0
    for strings in lst:
        if n <= len(strings):
            count += 1
    return count

