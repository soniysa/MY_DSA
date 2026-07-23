class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        ans = 0
        l = 0
        r = 0
        char_map = {}
        while (r < len(s)):
            ch = s[r]
            char_map[ch] = char_map.get(ch, 0)+1

            max_length =  max(max_length, char_map[ch])

            while(r-l+1)-max_length > k:
                ch1 = s[l]
                char_map[ch1] -= 1

                current_max = 0
                for key in char_map:
                    current_max = max(current_max, char_map[key])

                max_length = current_max
                l+=1
            
            if (r - l + 1) - max_length <= k:
                ans = max(ans, r-l+1)
            r+=1

        return ans