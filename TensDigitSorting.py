'''
Given an array A of N integers. Sort the array in increasing order of the value at the tens place digit of every number.

If a number has no tens digit, we can assume value to be 0.If 2 numbers have same tens digit, in that case number with max value will come firstSolution should be based on comparator.

Input 1:
A = [15, 11, 7, 19]

Input 2:
A = [2, 24, 22, 19]

Output 1:
[7, 19, 15, 11]

Output 2:
[2, 19, 24, 22]
'''
def tensDigit(tens):
    tens //= 10
    return tens % 10

def tenDigitSorting(array):
    array.sort(key=lambda x: (tensDigit(x), -x))
    return array

array = list(map(int, input().strip().split()))
print(tenDigitSorting(array))


# remember
'''

key=lambda x: (tensDigit(x), -x): The lambda function here takes each element x from the array and returns a tuple of two values:

 tensDigit(x): The first element of the tuple is the tens digit of the number x, obtained by calling the tensDigit function with x as the argument.

 -x: The second element of the tuple is the negation of the number x. By using -x, we effectively sort the elements in descending order of their original values. For example, if x is 10, -x will be -10; if x is 5, -x will be -5.

example array is [42, 19, 73, 58, 35, 90, 25].

For each element x in the array, we calculate the tuple (tensDigit(x), -x). For example:

For x = 42, tensDigit(x) = 4 and -x = -42, so the tuple is (4, -42).
For x = 19, tensDigit(x) = 1 and -x = -19, so the tuple is (1, -19).
And so on for the rest of the elements.

The list is then sorted based on the tuples. The primary sorting is done based on the first element of the tuple, i.e., the tens digit. So, elements with the same tens digit will be grouped together. Since Python's sorting is stable (i.e., elements that compare equal will remain in their original order), elements with the same tens digit will still maintain their original order in the secondary sorting.

For elements with the same tens digit, the secondary sorting comes into play, which is based on the second element of the tuple, i.e., -x. Sorting by -x in essence means sorting the elements in descending order of their original values.
'''






