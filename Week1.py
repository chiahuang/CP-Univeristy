##Challenge 1 - Deleting duplicates from a sorted array
#O(n) time complexity / O(n) space complexity
def duplicate(nums):
    result = set()
    for element in nums:
        result.add(element)

    return len(result)

#O(n) time complexity / O(1) space complexity
def duplicate2(nums):
    size = len(nums)
    index = 0
    count = 0
    for index in range(size - 1):
        if nums[index] == nums[index + 1]:
            count += 1

    return len(nums) - count

def test_duplicate():
    print("Testing Challenge 1 - Deleting duplicates from a sorted array")
    print("Input - [2,3,5,5,7,11,11,11,11,13]")
    assert duplicate([2,3,5,5,7,11,11,11,11,13]) == 6, "Result is True"
    print("Input - [2,3,5,5,7,11,11,11,13]")
    assert duplicate2([2,3,5,5,7,11,11,11,11,13]) == 6, "Result is True"
    print("End of Challenge 1\n")

##Challenge 2 - Enumerate all primes <= n
##def enumerate_prime(num):
##    answer = []
##    for index in range(2,num):
##        if index % 
##
##    return answer




##Challenge 3 - Spiral Order

def spiral_order(matrix):
    print(matrix)
    layer = len(matrix) // 2
    print(layer)
    answer = []
    for i in range(layer + 1):
        for j in range(len(matrix[i])):
            print(matrix[i][j])
            
        

def test_spiral_order():
    print("Testing Challenge 3 - Spiral Order")
    assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]), "Result: [1,2,3,6,9,8,7,4,5]"
    print("End of Challenge 3")
##Challenge 4 - Palindrome detection
'''
"A man, a plan, a canal: Panama" is a palindrome and should return true
"race a car" is not a palindrome and should return false
'''
#O(n) time complexity / O(1) space complexity
def is_palindrome(string):
    if string is None:
        return False
    
    list_of_strings = string.split()
    sentence = ''.join(list_of_strings)
    sentence_free = ''.join(e.lower() for e in sentence if e.isalpha())
    size = len(sentence_free)
    for index in range(size//2): # Divide by half to compare char by char or Do not divid and it will check all chars
        if sentence_free[index] != sentence_free[size - 1 - index]:
            return False

    return True

def test_is_palindrome():
    print("Testing Challenge 4 - Palindrome detection")
    print("Input - None")
    assert is_palindrome(None) == False, "Result is False"
    print("Input - race car")
    assert is_palindrome("race car"), "Result is True"
    print("Input - race a car")
    assert is_palindrome("race a car") == False, "Result is False"
    print("Input - A man, a plan, a canal: Panama")
    assert is_palindrome("A man, a plan, a canal: Panama"), "Result is True"
    print("End of Challenge 4\n")
    
##Challenge 5 - Longest Palindromic Substring

    
##Challenge 6 - Longest Common Prefix




if __name__ == "__main__":
    test_duplicate()
    test_spiral_order()
    #print(enumerate_prime(8))
    test_is_palindrome()
