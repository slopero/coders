from config import PATH_LIT, PATH_SCI
from services.calculate import calculate


def main():
    print("Художественный текст")
    print("------------------")
    calculate(PATH_LIT)
    print("\n\n")
    print("Научный текст")
    print("------------------")
    calculate(PATH_SCI)
if __name__ == "__main__":
    main()