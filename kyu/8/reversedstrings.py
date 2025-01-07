# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'
#  my solution:
def solution(string):
    word = list(string)
    word.reverse()
    return "".join(word)
