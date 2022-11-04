class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        # equalityDict = defaultdict(set)
        equalityDict = {}
        for equation in equations:
            a = equation[0]
            b = equation[3]
            operator = equation[1]
            if operator == '=':
                if a == b:
                    # a == b not need to handle
                    continue
                if a not in equalityDict and b not in equalityDict:
                    equalityDict[a] = set(b)
                    equalityDict[b] = set(a)
                else:
                    existed_a = a in equalityDict
                    existed_b = b in equalityDict 
                    # some case b was added to dict[a] by 1st loop
                    # so we define variable to keeptrack
                    if existed_a and b in equalityDict[a]:
                        # a and b were in dict and a == b -> skip
                        continue
                    
                    if existed_a:
                        if b not in equalityDict:
                            equalityDict[b] = set(a)
                        for val in equalityDict[a]:
                            if val != b:
                                equalityDict[val].add(b)
                            for val2 in equalityDict[b]:
                                if val2 != val:
                                    equalityDict[val].add(val2)
                            equalityDict[b].add(val)
                            
                        equalityDict[a].add(b)
                    if existed_b:
                        if a not in equalityDict:
                            equalityDict[a] = set(b)
                        for val in equalityDict[b]:
                            if val != a:
                                equalityDict[val].add(a)
                            for val2 in equalityDict[a]:
                                if val2 != val:
                                    equalityDict[val].add(val2)
                            equalityDict[a].add(val)
                        equalityDict[b].add(a)
            # print(equalityDict)
            # print("/n")
                          
        # print(equalityDict)
        
        for equation in equations:
            a = equation[0]
            b = equation[3]
            operator = equation[1]
            if operator == '!':
                if a == b:
                    return False
                if a in equalityDict:
                    if b in equalityDict[a]:
                        return False
        return True
                
                
sol = Solution()
sol.equationsPossible(["f==a","a==b","f!=e","a==c","b==e","c==f"])