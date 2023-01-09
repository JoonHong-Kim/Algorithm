# https://school.programmers.co.kr/learn/courses/30/lessons/17683
from datetime import datetime


def solution(m, musicinfos):
    candidates = []
    sharp_dict = {"C#": "1", "D#": "2", "F#": "3", "G#": "4", "A#": "5"}

    for key in sharp_dict.keys():
        m = m.replace(key, sharp_dict[key])
    for music in musicinfos:
        start, end, title, pitchs = music.split(",")
        for key in sharp_dict.keys():
            pitchs = pitchs.replace(key, sharp_dict[key])
        start = datetime.strptime(start, "%H:%M")
        end = datetime.strptime(end, "%H:%M")
        total_time = int((end - start).total_seconds() / 60)

        if total_time <= len(pitchs):
            pitchs = pitchs[:total_time]
        else:
            quotient = int(total_time // len(pitchs))
            remainder = total_time % len(pitchs)
            pitchs *= quotient
            pitchs = pitchs + pitchs[:remainder]

        if m in pitchs:
            candidates.append((total_time, title))

    candidates.sort(key=lambda x: -x[0])
    return candidates[0][1] if candidates else "(None)"
