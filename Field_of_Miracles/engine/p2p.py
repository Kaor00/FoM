from qq.data.questions import data
from qq.data.frases import frases
from qq.data.dict_name import dn
from qq.engine.names import get_names
from qq.engine.leksic import lsc
from qq.engine.game2 import fn
from random import choice

q = choice(data)
query = q[0]
answer = q[1]
world = [f"_" for _ in range(len(answer))]

def play():
    end = False
    names = get_names()
    print(f"{frases.get(4)}\n"
          f"{query} - {lsc(len(answer))}")
    arr = names
    double = []
    while not end:
        if len(arr) == 0:
            arr = double
            double = []
        cur = arr.pop(0)
        double.append(cur)
        if not dn.get(cur): dn[cur] = {"score": 0}
        [total, w] = fn(cur, answer, world)
        match total:
            case "change":
                print(f"{frases.get(12)}")
            case "end":
                print(f"{frases.get(13)}")
                print(w)
                print(f"{cur} {frases.get(14)}")
                end = True
            case "fall":
                print(f"Игрок {cur} {frases.get(15)}")
                double.pop(-1)
        if len(arr)==0 and len(double)==0:
            print(f"{frases.get(16)}")
            end = True
    print(f"{frases.get(17)}")
    return