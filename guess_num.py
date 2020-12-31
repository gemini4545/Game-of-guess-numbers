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


prompt_1 = "Input 4 unduplicated numbers:\n\n"
prompt_2 = "Try again:\n\n"
prompt_3 = "Warning! Four numbers are required. Retry:\n"
prompt_4 = "Warning! Unduplicated numbers are requrired. Retry:\n"

# Ask player to input a proper 4-digit number
class InputNum():

    def initial(self):

        list_input = list(int(item) for item in str(input(prompt_1)))
        while len(list_input) != 4:
            list_input = list(int(item) for item in str(input(prompt_3)))
        while len(list_input) != len(set(list_input)):
            list_input = list(int(item) for item in str(input(prompt_4)))
        return list_input

    def other_say(self):

        list_input = list(int(item) for item in str(input(prompt_2)))
        while len(list_input) != 4:
            list_input = list(int(item) for item in str(input(prompt_3)))
        while len(list_input) != len(set(list_input)):
            list_input = list(int(item) for item in str(input(prompt_4)))
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
        print("Congradulation！You found the right number "
              +"{0} in the {1} time!".format(result, counts[count-1]))
    else:
        print("What a pity, you've run out of your limited oppertunities.")


list_create = crt_num()
print(list_create)  # prove
list_temp = InputNum()
list_input = list_temp.initial()

compr_two_lists(list_create, list_input)
