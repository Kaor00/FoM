from qq.data.frases import frases as d
from qq.engine.p2p import play
from qq.engine.p2b import pwb

if __name__ == "__main__":
    try:
        print(d.get(1))
        start = input(d.get(2))
        match start:
            case "1":
                print("<<<<< Игра с другими игроками >>>>>")
                play()
            case "2":
                print("<<<<< В разработке >>>>>")
                pwb()
            case _:
                print("<<<<< Вы покинули игру >>>>>")
    except Exception as e:
        print(e)
