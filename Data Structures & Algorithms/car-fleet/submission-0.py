class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position,speed),reverse=True)
        fleets = 0
        max_time = 0.0
        for pos,sp in pairs:
            time=(target-pos)/sp
            if time > max_time:
                fleets += 1
                max_time = time
            # else: merges into the fleet ahead, no new fleet

        return fleets