def solution(bridge_length, weight, truck_weights):
    answer = 0

    on_bridge = []
    finish_cnt = 0
    n = len(truck_weights)

    t = now = 0
    while finish_cnt < n:
        t += 1
        if on_bridge:
            if t - on_bridge[0][1] >= bridge_length:
                temp = on_bridge.pop(0)
                now -= temp[0]
                finish_cnt += 1

            if truck_weights:
                if now + truck_weights[0] <= weight:
                    now += truck_weights[0]
                    on_bridge.append((truck_weights.pop(0), t))
        else:
            on_bridge.append((truck_weights[0], t))
            now += truck_weights.pop(0)
    return t