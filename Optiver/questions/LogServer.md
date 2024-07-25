# Problem Statement
Complete the following functions
• recordLog(LogId, timestamp): Records a new log entry.
• Each log is represented as an object with a logId and timestamp. The logid is an identifier for each log and the timestamp is an integer in seconds representing when the log was sent.
• Ignore logs with timestamps earlier than the latest log received
• The log ID is not guaranteed to be unique - the same log ID can be used for different logs.
• getLogs): Returns a comma separated string of the latest m logids from the last hour in the order they were received.
• Return a string of the form "logld1,logld2, logld3, logld4" where logld4 is the most recently received log and logid1 is the earliest log received < 1 hour before logld4's timestamp
• getLogCount (): Returns the total number of logs received < 1 hour from the most recently stored log timestamp. In the event more than m logs have been received still return the full count of logs
Input Format
The first line contains a single integer, m denoting the maximum number of logs getLogs) should return.
The second line contains a single integer, q denoting the number of queries. Each of the next q lines contains a query in one of the following formats:
• "RECORD logld timestamp" - This query represents a call to recordLog (logId,
timestamp）.
• "GET_LOGS" - This query represents a call to getLogs ().
• "COUNT" - This query represents a call to getLogCount ().

Constraints:
•1 m 1800
• 1≤45 1846
• LogId is an integer
• timestamp is an integer representing a timestamp in seconds
Output Format:
For each 'GET_LOGS' and 'COUNT' query, print the result
of getLogs () or getLogCount) on a new line. For 'GET_LOGS' queries, print a comma-separated string of log IDs. For 'COUNT' queries, print an integer.

Sample Input
100
1Đ
RECORD 1 0
RECORD 2 300
GET_LOGS
COUNT
RECORD 3 1200
RECORD 1 1800
GET_LOGS
COUNT
RECORD 4 3900
GET_LOGS
Sample Output
1,2
2
1,2,3,1
4
3,1,4

Explanation
1. RECORD 1 0: The log with ID 1 at timestamp 0 is recorded.
2. RECORD 2 300: The log with ID 2 at timestamp 300 is recorded.
3. GET_LOGS: At this point, we have two logs recorded. The function returns 1, 2 which are the IDs of the logs received so far in the order they were received.
4. COUNT: This returns the total number of logs in the last hour. At this time, we have two logs from the last hour, so it returns 2.
5. RECORD 3 1200: The log with ID 3 at timestamp 1200 is recorded.
6. RECORD 1 1800: Another log with ID 1 (logs can have the same ID) at timestamp 1800 is recorded.
7. GET_LOGS: At this point, four logs have been recorded within the last hour, so it returns 1,2,3,1 - the IDs of all the logs in the order they were received.
8. COUNT: This returns the total number of logs in the last hour. We have four logs from the last hour, so it returns 4.
9. RECORD 4 3900: The log with ID 4 at timestamp 3900 is recorded.
10. GET_LOGS: At this point, the logs with ID 1 at timestamp o and ID 2 at timestamp 300 are more than an hour old, so they are not included. The function returns 3,1,4 - the IDs of the logs from the past hour in the order they were received.