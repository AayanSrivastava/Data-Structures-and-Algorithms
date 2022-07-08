class Solution:
    def final(self,digits,output,index,ans,mapp):
        if index>=len(digits):
            ans.append(output)
            return
        
        di=digits[index]
        value=mapp[di]
        
        for i in range(len(value)):
            output+=(value[i])
            self.final(digits,output,index+1,ans,mapp)
            output=output[:-1]
            
        
    def letterCombinations(self, digits):
        ans=[]
        if len(digits)==0:
            return ans
        output=""
        index=0
        mapp={'0':"",
              '1':"",
              '2':"abc",
              '3':"def",
              '4':"ghi",
              "5":"jkl",
              '6':"mno",
              '7':"pqrs",
              '8':"tuv",
              '9':"wxyz"}
        self.final(digits,output,index,ans,mapp)
        return ans
l=Solution()
s="23"
print(l.letterCombinations(s))




# typing on keypad

# def phone(s,mapp):
#     a=""
#     l=1
#     for i in range(0,len(s),l+2):
        # print(i)
#         l=s.count(s[i])
#         a+=mapp[s[i]][l-1]
#     return a

# s="222333777"  #output= "cfr"
# mapp={'0':"",
#       '1':"",
#       '2':"abc",
#       '3':"def",
#       '4':"ghi",
#       "5":"jkl",
#       '6':"mno",
#       '7':"pqrs",
#       '8':"tuv",
#       '9':"wxyz"}

# print(phone(s,mapp))