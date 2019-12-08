class longestCommonPref(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        strs.sort(key=len)
        A = (strs)[0]
        res=''
        for i in range(len(A)):
            is_found = True
            for j in strs[1:]:
                if A[i] != j[i]:
                    is_found = False
                    return res
            if is_found:
                res += A[i]
        return res   


