class Solution:
    def findRadius(self, houses,heaters):
        houses.sort()
        heaters.sort()
        heat_l = heat_r = -10**9
        min_rad = 0
        heat_it = iter(heaters)
        for house in houses:
            if house > heat_r:
                for cur_heat in heat_it:
                    if cur_heat < house:
                        heat_l = cur_heat
                        heat_r = cur_heat
                    else:
                        heat_l = heat_r
                        heat_r = cur_heat
                        break
            
            min_rad = max(min_rad, min(abs(house - heat_l), 
                                       abs(house - heat_r)))
        return min_rad


if __name__ == '__main__':
    houses,heaters = [1,2,3,4],[1,4]
    s = Solution()
    print s.findRadius(houses,heaters)
