def uni_total(s):
    return 0 if s == '' else sum([ord(x) for x in s])


# After submitting to evaluate solution, realized didn't need the if else in return.
# First experience with ASCII and glad to have found ord and char functions