class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3: return False

        def check(num_1, num_2, remaining):
            if max(len(num_1), len(num_2)) > len(remaining):
                return False
            if (num_1[0] == '0' and len(num_1) != 1 or num_2[0] == '0' and len(num_2) != 1):
                return False
            
            total = int(num_1) + int(num_2)
            total = str(total)

            if len(remaining) < len(total):
                return False

            if total == remaining[0: len(total)]:
                if len(total) == len(remaining):
                    return True
                num_1 = num_2
                num_2 = total
                return check(num_1, num_2, remaining[len(total):])
            return False

        left = 0
        for mid in range(left+1, len(num)):
            for right in range(mid+1, len(num)):
                num_1 = num[left: mid]
                num_2 = num[mid: right]
                remaining = num[right:]

                if check(num_1, num_2, remaining):
                    return True
                
        return False

