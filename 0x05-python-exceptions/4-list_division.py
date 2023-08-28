#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    flag = 0

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            flag = 1
        except ZeroDivisionError:
            print("division by 0")
            flag = 1
        except (TypeError, ValueError):
            print("wrong type")
            flag = 1
        finally:
            if (flag):
                newlist.append(0)
                flag = 0
            else:
                newlist.append(result)
    return newlist
