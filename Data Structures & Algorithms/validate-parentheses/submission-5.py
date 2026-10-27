class Solution:
    def isValid(self, s: str) -> bool:
        stac = []
        for char in s:

            if char =='(' or  char =='{' or  char =='[':
                stac.append( char )
            
            if  char ==')':
                if stac and stac[-1]=='(':
                    stac.pop()
                else:
                    return False
            elif  char =='}':
                if stac and stac[-1]=='{':
                    stac.pop()
                else:
                    return False
            elif  char ==']':
                if stac and stac[-1]=='[':
                    stac.pop()
                else:
                    return False
        if stac :
            return False
        else:
            return True
        