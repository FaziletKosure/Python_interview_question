
def snakefill(n):
    return len(bin(n**2))-3


snakefill(3)  # 3

snakefill(6)  # 5

snakefill(24)  # 9



def snakefill2(n):
    return floor(log2(n*n))

