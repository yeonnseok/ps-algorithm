def solution(participant, completion):
    dicts = {}
    # 참가자 명단을 사전으로 저장한다.
    # 키는 이름, 밸류는 등장횟수
    for part in participant:
        if part not in dicts:
            dicts[part] = 1
        else:
            dicts[part] += 1

    # 완료된 명단을 참가자 사전에서 1명이면 지우고
    # 2명이면 밸류에서 1을 뺀다.
    # 최종적으로 남아있는 한명이 정답이다.
    for comp in completion:
        if comp in dicts:
            if dicts[comp] == 1:
                del dicts[comp]
            else:
                dicts[comp] -= 1

    return list(dicts.keys())[0]

