import random

change = True # Set whether or not the guess is changed after an incorrect door is revealed.
tests = 100000 # Set the number of tests, the more tests the more accurate the result.

class Solution:
    def __init__(self, x):
        self.correct = 0
        i = 0

        while i < x:
            answer = random.randint(1, 3)
            door = random.randint(1, 3)
            guess = random.randint(1, 3)
            switch = 0

            # Remove door that isn't the answer or the current guess.
            while door == answer or door == guess:
                door = random.randint(1, 3) # Randomly generates a number between 1 and 3, necessary in case the answer and guess are the same (should be the same ~11.11% of the time).

            # Change current guess to door that hasn't been removed IF the 'change' boolean is set to True (should be ~66.66% if True, ~33.33% if False).
            if change:
                while switch < 4:
                    if switch == 0 or guess == switch or door == switch:
                        switch += 1
                    else:
                        if switch == answer:
                            self.correct += 1
                        break
            else:
                if guess == answer:
                    self.correct += 1

            i += 1

monty_hall = Solution(tests)

print(str(round(monty_hall.correct / tests * 100, 2)) + '%')
input()

# https://en.wikipedia.org/wiki/Monty_Hall_problem
