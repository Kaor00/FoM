from qq.data.frases import frases as _f
from qq.data.dict_name import dn
from qq.data.drum import drum
from qq.bot.logic import lgk
from random import choice, randint


def fn(cur, answer, world):
    score = dn[cur]["score"]
    try:
        while True:
            print(f"\n{world}\n")
            if cur.startswith("_"): print(cur)
            action = "1" if cur.startswith("_") else input(f"{cur}, {_f.get(5)}")
            match action:
                case "1":
                    tt = 0
                    print(_f.get(6))
                    t = choice(drum)
                    if type(t) == int:
                        tt = t
                        print(f"{t} {_f.get(7)}")
                    if t == "x2":
                        print(f"{_f.get(8)}")
                        score *= 2
                        dn[cur] = {"score": score}
                    if t == "0":
                        print(f"{_f.get(9)}")
                        score = 0
                        dn[cur] = {"score": 0}
                    if t == '>>':
                        print(f"{_f.get(10)}")
                        return ["change", world]
                    if t == "prise":
                        print(f"{_f.get(11)}")
                    if t == "+":
                        while True:
                            print(world)
                            print(f"Сектор плюс на барабане\n")
                            ind = str(randint(1, len(answer))) if cur.startswith("_") else input(f"Какую букву открыть: ")
                            if ind.isdigit() and int(ind) <= len(answer):
                                ind = int(ind) - 1
                                world[ind] = answer[ind]
                                c = answer.count(world[ind])
                                if c > 1:
                                    print(f"Таких букв в слове {c}")
                                    for k, v in enumerate(answer):
                                        if v == world[ind]:
                                            world[k] = v
                                print(f"\n{world}\n")
                                break
                            else:
                                print("Будьте внимательнее! Буквы под таким номером нет")
                    print(f'У вас {score} очков')
                    word = lgk(world) if cur.startswith("_") else input("Ваша буква: ").lower()
                    if cur.startswith("_"): print(f"Ваша буква: {word}")
                    c = answer.count(word)
                    if c == 1:
                        print("Есть такая буква!")
                        ind = answer.index(word)
                        world[ind] = word
                        score += tt
                        dn[cur] = {"score": score}
                    if c > 1:
                        print(f"Таких букв в слове {c}")
                        for k, v in enumerate(answer):
                            if v == word:
                                world[k] = word
                                score += tt
                                dn[cur] = {"score": score}
                    if c == 0:
                        print("такой буквы здесь нет")
                        return ["change", world]
                case "2":
                    y = input(f"Напоминаю, что если вы назовете слово не верно, то вы проиграете\n"
                              f"Назовите слово целиком: ")
                    if y.lower() == answer:
                        world = [i for i in y.lower()]
                        print(f"Вы отгадали слово!!!\n{world}")
                        return ["end", world]
                    else:
                        print("Это не верный ответ. Вы проиграли")
                        return ["fall", world]
                case _:
                    print('Не говорите ерунды')
            if answer == "".join(world):
                print(f"Вы отгадали слово!!!\n{world}")
                return ["end", world]
    except KeyboardInterrupt:
        print("Игра прекращена")
