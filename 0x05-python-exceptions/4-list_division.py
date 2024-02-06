#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            dr = my_list_1[i] / my_list_2[i]
        except IndexError:
            dr = 0
            print("out of range")
        except ZeroDivisionError:
            dr = 0
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
            dr = 0
        finally:
            result.append(dr)
        return result
