class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {
             ")": "(", "}": "{", "]": "["
        }
        stack = []
        for p in s:
            if p in p_dict:
                if not stack: 
                    return False
                if p_dict[p] != stack.pop():
                    return False
            else:
                 stack.append(p)
               
        return not len(stack) 
