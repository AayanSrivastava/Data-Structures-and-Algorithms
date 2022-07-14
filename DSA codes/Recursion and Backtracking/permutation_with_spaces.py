class l:
    def solve(self,n,ip,op,l):

        if len(op)==0:
            l.append(ip)
            return
        if len(op)==n:
            self.solve(n,ip+op[0],op[1:],l)
        else:
            self.solve(n,ip+' '+op[0],op[1:],l)
            self.solve(n,ip+op[0],op[1:],l)
            
    def permutation (self, S):
        # code here
        
        n=len(S)
        l=[]
        self.solve(n,'',S,l)
        return l

l1=l()
s="ABC"
print(l1.permutation(s))