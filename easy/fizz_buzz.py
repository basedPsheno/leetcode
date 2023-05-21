# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        third = fifth = 0
        for i in range(1, n + 1):
            third += 1
            fifth += 1
            if third == 3 and fifth == 5:
                answer.append("FizzBuzz")
                third = fifth = 0
            elif third == 3:
                answer.append("Fizz")
                third = 0
            elif fifth == 5:
                answer.append("Buzz")
                fifth = 0
            else:
                answer.append(f"{i}")
        return answer
