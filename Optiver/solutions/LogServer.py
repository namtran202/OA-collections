from collections import deque


class LogServer:
    def __init__(self, m):
        self.m = m
        self.logs = deque()

    def recordLog(self, logId, timestamp):
        self.logs.append((logId, timestamp))
        one_hour_timestamp = self.logs[-1][1] - 3600
        while self.logs[0][1] <= one_hour_timestamp:
            self.logs.popleft()

    def getLogs(self):
        max_logs = min(len(self.logs), self.m)
        one_hour_logs = []
        while max_logs > 0:
            log = self.logs[-max_logs]
            one_hour_logs.append(str(log[0]))
            max_logs -= 1
        return ",".join(one_hour_logs)

    def getLogCount(self):
        return len(self.logs)


server = LogServer(2)
server.recordLog(1, 0)
server.recordLog(7, 600)
server.recordLog(3, 1200)
server.recordLog(5, 1800)
print(server.getLogs())
print(server.getLogCount())
server.recordLog(2, 2400)
print(server.getLogs())
print(server.getLogCount())

print("-------")
server2 = LogServer(100)
server2.recordLog(1, 0)
server2.recordLog(2, 300)
print(server2.getLogs())
print(server2.getLogCount())
server2.recordLog(3, 1200)
server2.recordLog(1, 1800)
print(server2.getLogs())
print(server2.getLogCount())
server2.recordLog(4, 3900)
print(server2.getLogs())
