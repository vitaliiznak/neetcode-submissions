class Solution:
    def isValid(self, s: str) -> bool:
        open_p = ["(", "{", "["]
        p_dict = {
            "(" : ")", "{" : "}", "[" : "]",
             ")": "(", "}": "{", "]": "["
        }
        stack = []
        for p in s:
            if p in open_p:
                stack.append(p)
            else:
                if not stack: 
                    return False
                if p_dict[p] != stack.pop():
                    return False
        return not len(stack) 
