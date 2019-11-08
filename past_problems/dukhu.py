def solution(total_ticket, logs):
    answer = []
    server_stack = []
    start = 9*3600
    end = 10*3600

    for i in range(len(logs)):
        id, action, time_log = logs[i].split()
        hh, mm, ss = list(map(int, time_log.split(":")))
        time = hh*3600 + mm*60 + ss  # 접속시간을 초로 다 변경
        if start <= time < end and total_ticket > 0:
            if action == 'request':
                if not server_stack:
                    server_stack.append((id, time))
                elif time - server_stack[-1][1] >= 60:
                    temp = server_stack.pop()
                    answer.insert(0, temp[0])
                    server_stack.append((id, time))
                    total_ticket -= 1
            else: # action == 'leave' 이면 티케팅 실패했다는 의미
                if server_stack[-1][0] == id:
                    server_stack.pop()

    if server_stack:
        if end - server_stack[-1][1] >= 60:
            answer.insert(0, server_stack[-1][0])

    return answer


total_ticket = 2000
logs = [
    "mini request 09:00:00",
    "woni request 09:12:29",
    "brown request 09:23:11",
    "brown leave 09:23:44",
    "jason request 09:33:51",
    "jun request 09:33:56",
    "cu request 09:34:02",
    "mi request 09:34:51",
    "choi request 09:58:00"
]

print(solution(total_ticket, logs))





