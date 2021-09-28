class DVD:    
    def __init__(self, name, releaseYear, director):
        self.name = name
        self.releaseYear = str(releaseYear)
        self.director = director
    
    def __str__(self):
        try:
            return (self.name + ", directed by " + self.director + 
                    ", released in " + self.releaseYear)
        except Exception:
            pass
        
if __name__ == "__main__":
    dvdCollection = [None]*15
    # Firstly, we need to actually create a DVD object for The Avengers.
    avengersDVD = DVD("The Avengers", 2012, "Joss Whedon")

    # Next, we'll put it into the 8th place of the Array. Remember, because we
    # started numbering from 0, the index we want is 7.
    dvdCollection[7] = avengersDVD

    incrediblesDVD = DVD("The Incredibles", 2004, "Brad Bird");
    findingDoryDVD = DVD("Finding Dory", 2016, "Andrew Stanton");
    lionKingDVD = DVD("The Lion King", 2019, "Jon Favreau");
    
    # Put "The Incredibles" into the 4th place: index 3.
    dvdCollection[3] = incrediblesDVD;

    # Put "Finding Dory" into the 10th place: index 9.
    dvdCollection[9] = findingDoryDVD;

    # Put "The Lion King" into the 3rd place: index 2.
    dvdCollection[2] = lionKingDVD;

    starWarsDVD = DVD("Star Wars", 1977, "George Lucas");
    dvdCollection[3] = starWarsDVD;

    print("Length: " , len(dvdCollection))
    # Print out what's in indexes 7, 10, and 3.
    print(dvdCollection[7]);
    print(dvdCollection[10]);
    print(dvdCollection[3]);
    print("========================")
    
    
      
    for i, dvd in enumerate(dvdCollection):
        print('{0}. {1}'.format(i, dvd))
    print("========================")
    
    #Inserting data in the begining
    for i in range(len(dvdCollection) - 2, -1, -1):
        dvdCollection[i+1] = dvdCollection[i]
    
    mulanDVD = DVD("Mulan", 2020, "Niki Caro");
    dvdCollection[0] = mulanDVD;
    
    for i, dvd in enumerate(dvdCollection):
        print('{0}. {1}'.format(i, dvd))
    print("========================") 
    
    #Inserting data in the xth position
    x = 7
    for i in range(len(dvdCollection) - 2, x - 1, -1):
        dvdCollection[i+1] = dvdCollection[i]
    
    avatarDVD = DVD("Avatar", 2020, "James Cameron");
    dvdCollection[x] = avatarDVD;
    
    for i, dvd in enumerate(dvdCollection):
        print('{0}. {1}'.format(i, dvd))