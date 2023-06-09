# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        next_letter = letters[0]

        for letter in letters:
            if ord(letter) > ord(target):
                next_letter = letter
                break

        return next_letter
