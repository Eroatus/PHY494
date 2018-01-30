# Marco's Test Program

# Set the state of the program to 'not done' to indicate that the
# code hasn't completed its primary purpose.
done = False

# Initially, no loop iterations have occurred and the list of
# multiples is empty.
iteration = 0
multiplicity_list = []

# Extend the program's purpose by allowing the user to choose which
# value is the base in the multiplicity list.
base = int(input("Choose a base: "))

# The program will continue to loop and conduct calculations so
# long as it is 'not done'.
while not done:
    # Each loop increments the iteration that is underway and the
    # list is updated with an additional multiple of the base.
    iteration += 1
    multiplicity_list.append(base * iteration)

    # The first iteration places the base value into the list, which
    # would provide a trivial solution. As such, this portion is only
    # executed for subsequent iterations.
    if(iteration > 1):
        # Whenever the base value is repeated, the difference in the
        # lastest multiple and the base should end in a 0. In other
        # words, the difference should be a multiple of 10.
        difference = multiplicity_list[iteration - 1] - \
                     multiplicity_list[0]

        # In the case the difference IS a multiple of 10, then the
        # program has found the desired value and is now 'done'.
        if(difference % 10 == 0):
            done = True

# The results are printed.
print("Multiple with first base value repetition:", iteration)
