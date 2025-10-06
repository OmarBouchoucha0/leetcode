def lengthOfLongestSubstring(s: str) -> int:
   if len(s) <= 1:
        return len(s)
   sub_s = ""
   max_len =  0
   for char in s:
        if char not in sub_s:
            sub_s += char
            print(sub_s)
        else:
            if len(sub_s) > max_len:
                max_len = len(sub_s)
            pos = sub_s.find(char)
            sub_s = sub_s[pos+1:] 
            sub_s += char
   if len(sub_s) > max_len:
        max_len = len(sub_s)
   return max_len
