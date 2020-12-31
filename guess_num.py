import random


# Create a radom 4-digit number automatically
def crt_num():
    list_create = []
    list_range = list(range(9))
    for i in range(4):
        temp = random.choice(list_range)
        list_create.append(temp)
        list_range.remove(temp)

    return list_create


# Ask player to input a proper 4-digit number
class InputNum():

    def initial(self):

        list_input = list(int(item) for item in
            str(input('Input 4 unduplicated numbers:\n\n')))
        while len(list_input) != 4:
            list_input = list(int(item) for item in str(input
                ('Warning! A 4-digit number is needed, retry:\n')))
        while len(list_input) != len(set(list_input)):
            list_input = list(int(item) for item in str(input
                ("warning! Non-repeating digitals are needed, retry:\n")))

        return list_input

    def other_say(self):

        list_input = list(int(item) for item in
                 str(input('Try agian:\n\n')))
        while len(list_input) != 4:
            list_input = list(int(item) for item in str(input
                 ('Warning! A 4-digit number is needed, retry:\n')))
        while len(list_input) != len(set(list_input)):
            list_input = list(int(item) for item in str(input
                 ("warning! Non-repeating digitals are needed, retry:\n")))

        return list_input


# Compare the 2 lists within limited times:
def compr_two_lists(list1, list2):
    count = 1

    while list1 != list2 and count < 10:
        count_A, count_B = 0,0

        for item1 in list1:
            for item2 in list2:
                if item1 == item2:
                    count_B += 1

        for i in range(4):
            if list1[i] == list2[i]:
                count_A += 1
                if count_B > 0:
                    count_B -= 1

        print("{0}A{1}B ---> {2} times left."
              .format(count_A, count_B, 10-count), end = " ")
        list2 = list_temp.other_say()
        #list(int(item) for item in str(input('try again:\n')))
        count += 1

    result = ''.join(str(j) for j in list1)

    if list1 == list2:
        counts = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th']
        print("Congradulation, you found the right number "
              +"{0} in the {1} time!".format(result, counts[count-1]))
    else:
        print("Pity, you've run out of your limited times.")


list_create = crt_num()
print(list_create)  # prove
list_temp = InputNum()
list_input = list_temp.initial()

compr_two_lists(list_create, list_input)
