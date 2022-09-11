class SumNumb():

    def __init__(self, list):
        self.list = list

    def sum_from_list(self):
        answer = 0
        for numb in self.list:
            answer += int(numb)
        return answer