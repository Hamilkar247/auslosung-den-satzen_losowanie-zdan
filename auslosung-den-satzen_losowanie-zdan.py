import logging
import argparse
import random

def def_params():
    parser = argparse.ArgumentParser(
            description="""
            Program do losowania zdan z dostepnych w pliku auslosung_den_satze.txt
            Uwaga - kolejne zdania wpisuj z odstepem pustej linii
            """
    )
    parser.add_argument(
        "-l", "--loghami", action='store_true', help="set debug")
    parser.add_argument(
        "-d", "--datei", default="auslosung_den_satze.txt", help="plik z którego pobieramy sentencje do losowania")
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG, force=True)
        print("args:" + str(args))
    return args

def auslosung_den_satzen(name_datei):
    with open(name_datei) as nd:
        inhalt = nd.read()
    tafel=[]
    for satze in inhalt.split('\n\n'):
        tafel.append(satze)
    #auslosung
    while True:
        anzahl_den_satzen = len(tafel)
        if anzahl_den_satzen == 0:
            break
        ziehl=random.randint(0, anzahl_den_satzen-1)
        print(tafel[ziehl])
        del tafel[ziehl]

def main():
    args=def_params()
    name_datei=args.datei
    auslosung_den_satzen(name_datei)

if __name__ == "__main__":
    main()
