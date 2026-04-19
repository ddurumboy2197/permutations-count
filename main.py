import itertools

def permutatsiya_soni(string):
    return len(set(itertools.permutations(string)))

string = input("Kiriting: ")
print(permutatsiya_soni(string))
