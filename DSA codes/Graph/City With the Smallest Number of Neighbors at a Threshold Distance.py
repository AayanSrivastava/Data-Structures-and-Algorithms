class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        dist=[[float('inf') for i in range(n)] for j in range(n)]
        for city1,city2,wt in edges:
            dist[city1][city2]=wt
            dist[city2][city1]=wt
        for i in range(n):
            dist[i][i]=0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]==float('inf') or dist[k][j]==float('inf'):
                        continue
                    dist[i][j]=min(dist[i][j],(dist[i][k]+dist[k][j]))
        
        citycnt=n
        cityNo=-1
        for city in range(n):
            cnt=0
            for adjcity in range(n):
                if dist[city][adjcity]<=distanceThreshold:
                    cnt+=1
            if cnt<=citycnt:
                citycnt=cnt
                cityNo=city
        return cityNo