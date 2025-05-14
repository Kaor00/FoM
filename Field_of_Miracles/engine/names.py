from qq.data.frases import frases

def get_names():
    return [input(frases.get(3)) for _ in range(3)]

def get_name():
    return input(frases.get(3))