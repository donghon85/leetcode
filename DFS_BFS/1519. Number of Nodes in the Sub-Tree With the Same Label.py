class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        path={}
        for s,e in edges:
            if e not in path:
                path[e]=[s]
            else:
                path[e].append(s)
            if s not in path:
                path[s]=[e]
            else:
                path[s].append(e)

        labelCt = {}
        for i in labels:
            if i not in labelCt:
                labelCt[i]=1
            else:
                labelCt[i]+=1
        print(path)
        print(labelCt)

        ans=[0]*n
        def fun(node=0,par=None):
            prev=labelCt[labels[node]]
            labelCt[labels[node]] += 1
            for child in path[node]:
                if child != par: 
                    fun(child, node)

            ans[node] = labelCt[labels[node]] - prev
        fun()
        return ans