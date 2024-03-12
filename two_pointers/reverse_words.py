# Created by Adarsh N B at 3/5/2024

# Description:
"""
Given a sentence, reverse the order of its words without affecting the order of letters within a given word

Ex -> input -> Hello World. output -> World Hello
Time complexity - Since the array is traversed twice, the time complexity of this solution is O(n+n)=O(n)
Space complexity - O(n) (usually the two pointers approach uses constant space but since we are storing the reversed
                         string of the input here its O(n))
"""

"""
The logic is to reverse the string (and replace extra spaces between the words. Depends on if the interviewer is asking)
Once the string is reversed, start by having two pointers to the first index i.e, 0. Keep moving the right pointer
until it encounters a space. Extract the word by reversed[left: right-1] and then reverse this string and  
"""

def reverse_words(sentence: str) -> str:
    reversed_str = ""
    left = right = 0

    return reversed_str


if __name__ == "__main__":
    string_to_reverse = ["Hello Friend", "    We love Python",
                         "The quick brown fox jumped over the lazy dog   ",
                         "Hey", "To be or not to be",
                         "AAAAA", "Hello     World"]

    for i in range(len(string_to_reverse)):
        print(i + 1, ".\t Actual string:\t\t" +
              "".join(string_to_reverse[i]), sep='')
        Result = reverse_words(string_to_reverse[i])
        print("\t Reversed string:\t" +
              "".join(Result), sep='')
        print("-" * 100)
