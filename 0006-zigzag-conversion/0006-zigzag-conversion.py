class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = ""
        if numRows == 1 or numRows >=  len(s):
            return s

        for i in range(0,numRows):
            idx = i
            niche = (numRows-i-1)*2
            ooper = 2 * i
            flag = False

            while(idx < len(s)):
                output += s[idx]
                if i==0:
                    idx += niche
                elif i==numRows-1:
                    idx += ooper
                else:
                    if flag == False:
                        idx += niche
                    else:
                        idx += ooper
                    

                    flag = not flag

        return output
                
        

            