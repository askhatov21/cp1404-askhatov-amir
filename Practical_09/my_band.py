from band import Band
from musician import Musician
from guitar import Guitar

def main():
    band = Band("Extreme")
    band.add(Musician("Nuno Bettencourt"))
    band.add(Musician("Gary Cherone"))
    band.add(Musician("Pat Badger"))
    band.add(Musician("Kevin Figueiredo"))

    band.musicians[0].add(Guitar("Washburn N4", 1990, 2499.95))
    band.musicians[0].add(Guitar("Takamine acoustic", 1986, 1200.00))
    band.musicians[2].add(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))

    print("band (str)")
    print(band)
    print("band.play()")
    band.play()

if __name__ == "__main__":
    main()
