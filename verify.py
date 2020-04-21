# The cdc code of each letter is given in the problem
cdc = {'A':23, 'B': 47, 'I':397, 'L':507, 'O':581, 'P':635, 'R':687, 'U':763, 'Y':901, '0':405, '1':73}

# This function generates any possible combination of letters from the list
your_list = 'ABILOPRUY01'   # character list
complete_list = []
for current in range(3):    # 3 character long password
    a = [i for i in your_list]
    for y in range(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list + a

# Generate cdc co of the text
def generate_cdc(text):
    i = 0;
    for letter in text:
        i = ((((i + cdc[letter]) * 521) % 10000) + 450) % 967
    return i

# loop for every possible password combination from the list generated earlier
for pwd in complete_list:
    if (generate_cdc(pwd+"PAYBOB100") == 481 and generate_cdc(pwd+"BILLBOB1000") == 827 and\
        generate_cdc(pwd+"PAYROB1000") == 301):
        print("Key found: ",pwd)
        break
