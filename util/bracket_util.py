def check_bracket_str(bracket_str):
    if bracket_str and len(bracket_str) > 0:

        list_index_bracket_right_t = list()
        list_index_bracket_left_t = list()

        list_index_bracket_left_f = list()
        list_index_bracket_right_f = list()

        ret_data_bracket_right = list()
        ret_data_bracket_left = list()

        info_result_bracket_right = dict()
        info_result_bracket_left = dict()

        flag = 0
        for i in range(len(bracket_str)):
            j = i + 1
            if bracket_str[i] == "(":
                while j < len(bracket_str):
                    flag = 0
                    if j not in list_index_bracket_right_t:
                        if bracket_str[j] == ")":
                            list_index_bracket_right_t.append(j)
                            list_index_bracket_left_t.append(i)
                            flag = 1
                            break
                    j += 1
            elif bracket_str[i] == ")":
                if i not in list_index_bracket_right_t:
                    list_index_bracket_right_f.append(i)
                flag = 1

            if flag == 0:
                list_index_bracket_left_f.append(i)

        if len(list_index_bracket_left_f) == 0 and len(list_index_bracket_right_f) == 0:
            print("True")
        else:
            print("False")

            if len(list_index_bracket_right_f) > 0:
                last_index = len(list_index_bracket_right_f) - 1
                for i in range(len(list_index_bracket_right_f)):
                    index = last_index - list_index_bracket_right_f[i]
                    info_result_bracket_right['('] = index
                    ret_data_bracket_right.append(info_result_bracket_right.copy())

            if len(list_index_bracket_left_f) > 0:
                for i in range(len(list_index_bracket_left_f)):
                    index = list_index_bracket_left_f[i] + 1
                    info_result_bracket_left[')'] = index
                    ret_data_bracket_left.append(info_result_bracket_left.copy())

            print("Right:")
            print(ret_data_bracket_right)
            print("--------------")
            print("Left:")
            print(ret_data_bracket_left)

            return ret_data_bracket_right, ret_data_bracket_left

    return ("brackets is not correct. Please inout againt. EX:(())))")
