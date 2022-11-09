class Solution:
    def dfs(self,row,col,delrow,delcol,inicolor,newColor,ans,image):
        ans[row][col]=newColor
        n=len(image)
        m=len(image[0])
        for i in range(4):
            nrow=row+delrow[i]
            ncol=col+delcol[i]
            if (nrow>=0 and nrow<n and ncol>=0 and ncol<m and image[nrow][ncol]==inicolor and ans[nrow][ncol]!=newColor):
                self.dfs(nrow,ncol,delrow,delcol,inicolor,newColor,ans,image)
                
            
    def floodFill(self, image, sr, sc, newColor):
        ans=image
        inicolor=image[sr][sc]
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        self.dfs(sr,sc,delrow,delcol,inicolor,newColor,ans,image)
        return ans
    
