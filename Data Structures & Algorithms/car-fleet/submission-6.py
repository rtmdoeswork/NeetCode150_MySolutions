class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 1
        time_to_reach = 0
        paired_list = []

        if len(position) < 2:
            return 1

        for i in range(len(position)):
            paired_list.append((position[i], speed[i]))

        paired_list.sort(key=lambda x: x[0], reverse=True)
        max_time = (target - paired_list[0][0]) / paired_list[0][1]
        for i in range(1, len(paired_list)):
            time_to_reach = (target - paired_list[i][0]) / paired_list[i][1]
            if max_time < time_to_reach:
                fleet += 1
                max_time = time_to_reach
            else:
                pass

        return fleet