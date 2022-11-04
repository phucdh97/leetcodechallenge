from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        dic = defaultdict(list)
        for path in paths:
            line = list(map(str, path.split()))
            length = len(line)
            directoryPath = line[0]
            for i in range(1, length):
                file = line[i]
                full_length = len(file)

                index = -1
                for i in range(full_length):
                    cur_char = file[i]
                    if cur_char == '(':
                        index = i
                        break
                
                file_name = file[:i]
                file_content = file[i+1:full_length-1]
                full_path = directoryPath + '/' + file_name
                dic[file_content].append(full_path)
        
        ans = []
        for value in dic.values():
            if len(value) > 1:
                ans.append(value)

        # print("dic:", dic)
        # print("ans:", ans)
        return ans
                




sol = Solution()
sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"])

#[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]