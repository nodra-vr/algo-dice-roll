from pyteal import *

def contract():
    return Int(1)

if __name__ == "__main__":
    print(compileTeal(contract(), Mode.Application, version=5))