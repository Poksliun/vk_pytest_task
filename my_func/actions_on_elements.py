import math
class ActionsOnElements():
    def sum_from_list(self, list):
        answer = 0
        for numb in list:
            answer += int(numb)
        return answer

    def division_elements(self, list, numb):
        final_list = []
        for element in list:
            new_element = element / numb
            final_list.append(new_element)

        return final_list

    def exp_and_sqrt(self, numb):
        sqare = numb ** 2
        sqrt = math.sqrt(sqare)

        return sqrt


