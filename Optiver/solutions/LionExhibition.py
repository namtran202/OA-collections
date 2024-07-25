import heapq
from collections import defaultdict


class LionCompetition:
    def __init__(self, lions, schedule):
        self.our_lions = {}  # To store our lions' heights by their names
        self.schedule = {}  # To store entry and exit times by lion names
        for lion in lions:
            name, height = lion[0], lion[1]
            self.our_lions[name] = height

        for entry in schedule:
            name, enter_time, exit_time = entry[0], entry[1], entry[2]
            self.schedule[name] = (enter_time, exit_time)

        self.in_room_lions = defaultdict(int)  # A dictionary to track counts of lions in the room by height
        self.our_lions_in_room = set()  # A set to track our lions in the room
        self.max_heap = []  # A max-heap (implemented as a min-heap with negative heights)

    def lion_entered(self, current_time, height):
        # This will be used for external lions
        self.in_room_lions[height] += 1
        heapq.heappush(self.max_heap, -height)  # Push the negative height to simulate a max-heap

    def lion_left(self, current_time, height):
        # Decrease the count of lions with the given height
        self.in_room_lions[height] -= 1
        if self.in_room_lions[height] == 0:
            del self.in_room_lions[height]

        # We need to maintain the max-heap to reflect the current maximum lion height
        # Lazy removal: just mark it as invalid and clean up during inspection
        while self.max_heap and -self.max_heap[0] not in self.in_room_lions:
            heapq.heappop(self.max_heap)

    def get_biggest_lions(self, current_time):
        if self.max_heap:
            max_competing_height = -self.max_heap[0]
        else:
            max_competing_height = 0

        biggest_lions = [name for name in self.our_lions_in_room if self.our_lions[name] >= max_competing_height]
        return sorted(biggest_lions)


sol = LionCompetition([("marry", 300), ("rob", 250)], [("marry", 10, 15), ("rob", 13, 20)])
sol.lion_entered(8, 200)
sol.lion_entered(10, 310)
sol.lion_entered(10, 300)

sol.lion_entered(13, 250)
sol.lion_left(13, 310)
print(sol.get_biggest_lions(11))
print(sol.in_room_lions)
print(sol.our_lions_in_room)
print(sol.max_heap)
print(sol.get_biggest_lions(13))
# sol.lion_left(15, 300)
# print(sol.get_biggest_lions(16))
# sol.lion_left(16, 310)
# sol.lion_left(20, 310)