import heapq
from collections import defaultdict


class LionCompetition:
    def __init__(self, lions, schedule):
        self.our_lions = {}  # To store our lions' heights by their names
        self.schedule = {}  # To store entry and exit times by lion names
        for lion in lions:
            name, height = lion['name'], lion['height']
            self.our_lions[name] = height

        for entry in schedule:
            name, enter_time, exit_time = entry['name'], entry['enterTime'], entry['exitTime']
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

    def run_schedule(self, events):
        for event in events:
            current_time = event['time']
            action = event['action']
            if action == 'enter':
                height = event['height']
                self.lion_entered(current_time, height)
            elif action == 'exit':
                height = event['height']
                self.lion_left(current_time, height)
            elif action == 'inspect':
                print(current_time, self.get_biggest_lions(current_time))
            elif action == 'start':
                for name, (enter_time, exit_time) in self.schedule.items():
                    if enter_time <= current_time:
                        self.in_room_lions[self.our_lions[name]] += 1
                        self.our_lions_in_room.add(name)
                        heapq.heappush(self.max_heap, -self.our_lions[name])
                    if exit_time <= current_time:
                        self.our_lions_in_room.remove(name)
                        self.lion_left(current_time, self.our_lions[name])


# Example usage
lions = [
    {"name": "marry", "height": 300},
    {"name": "rob", "height": 250}
]

schedule = [
    {"name": "marry", "enterTime": 10, "exitTime": 15},
    {"name": "rob", "enterTime": 13, "exitTime": 20}
]

events = [
    {"time": 8, "action": "enter", "height": 200},
    {"time": 10, "action": "enter", "height": 310},
    {"time": 10, "action": "enter", "height": 300},
    {"time": 11, "action": "inspect"},
    {"time": 13, "action": "enter", "height": 256},
    {"time": 13, "action": "exit", "height": 310},
    {"time": 13, "action": "inspect"},
    {"time": 15, "action": "exit", "height": 300},
    {"time": 16, "action": "inspect"},
    {"time": 16, "action": "exit", "height": 200},
    {"time": 20, "action": "exit", "height": 250},
    {"time": 21, "action": "end"}
]

lc = LionCompetition(lions, schedule)
lc.run_schedule(events)
