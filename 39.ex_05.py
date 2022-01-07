# ---------------------Exercise------------------

# create lenth() functicon

# len()
# lenth()


def lenth(par):
    lenth = 0
    for i in par:
        lenth += 1
    return lenth

name = ["Dot","Code","Name","Password"]
print(lenth(name))
print(len(name))