class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans={}
        for i in cpdomains:
            cos=i.split(" ")
            count=cos[0]
            name=cos[1].split(".")
            name=name[::-1]
            st=""
            for i in name:
                if st=="":
                    st=i
                else:
                    st=i+"."+st
                if st not in ans:
                    ans[st]=0
                ans[st]+=int(count)
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]