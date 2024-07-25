from collections import defaultdict
from heapq import heappush, heappop


class LionExhibition:
    def __init__(self, lions, schedule):
        # Map of our lions' names to their sizes
        self.my_lions = {lion: size for lion, size in lions}
        # Set of our lions that are present at any given time
        self.my_lions_present = set()

        # Ignore map to keep track of our lions entering and leaving
        self.ignore_map = defaultdict(int)

        # Other lions that are present (max heap by size)
        self.max_height = []
        # Lions that have left but are still in the heap (lazy deletion)
        self.other_lions_left = defaultdict(int)

        # Schedule sorted by time of arrival/leaving
        self.schedule = []
        for name, arrival, departure in schedule:
            self.schedule.append((arrival, name, 'arrive'))
            self.schedule.append((departure, name, 'depart'))
            self.ignore_map[(self.my_lions[name], arrival, 'arrive')] += 1
            self.ignore_map[(self.my_lions[name], departure, 'depart')] += 1

        self.schedule.sort(key=lambda event: event[0])
        # Schedule index
        self.schedule_index = 0

    def lion_entered(self, time, height):
        key = (height, time, 'arrive')
        if self.ignore_map[key] > 0:
            self.ignore_map[key] -= 1
        else:
            heappush(self.max_height, -height)

    def lion_left(self, time, height):
        key = (height, time, 'depart')
        if self.ignore_map[key] > 0:
            self.ignore_map[key] -= 1
        else:
            self.other_lions_left[height] += 1

    def get_biggest_lions(self, time):
        # Flush our lions to the ones currently in the room based on time
        while self.schedule_index < len(self.schedule) and self.schedule[self.schedule_index][0] <= time:
            event_time, name, event_type = self.schedule[self.schedule_index]
            if event_type == 'arrive':
                self.my_lions_present.add((name, self.my_lions[name]))
            else:
                self.my_lions_present.remove((name, self.my_lions[name]))
            self.schedule_index += 1

        # Flush the heap of other lions to find the tallest and still present
        while self.max_height:
            tallest = -self.max_height[0]
            if self.other_lions_left[tallest] > 0:
                heappop(self.max_height)
                self.other_lions_left[tallest] -= 1
            else:
                break

        tallest = -self.max_height[0] if self.max_height else 0
        candidates = [name for name, height in self.my_lions_present if height >= tallest]
        candidates.sort()
        return candidates


sol = LionExhibition([("marry", 300), ("rob", 250)], [("marry", 10, 15), ("rob", 13, 20)])
sol.lion_entered(8, 200)
sol.lion_entered(10, 310)
sol.lion_entered(10, 300)
print(sol.get_biggest_lions(11))
sol.lion_entered(13, 250)
sol.lion_left(13, 310)
print(sol.get_biggest_lions(13))
sol.lion_left(15, 300)
print(sol.get_biggest_lions(16))
sol.lion_left(16, 310)
sol.lion_left(20, 310)