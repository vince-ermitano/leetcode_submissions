class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p, s) for p, s in zip(position, speed)]
        pos_speed.sort(reverse=True)
        stack = []

        for pos, speed in pos_speed:
            stack.append((target - pos) / speed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)