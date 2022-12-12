class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
            answer = []
            i = 1
            while i <= n:
                if i % 15 == 0:
                    answer.append("FizzBuzz")
                elif i % 3 == 0:
                    answer.append("Fizz")
                elif i % 5 == 0:
                     answer.append("Buzz")
                else:
                     answer.append(str(i))
                i += 1
            return answer
