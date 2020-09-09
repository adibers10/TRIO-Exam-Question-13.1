class Library:
    def __init__(self,year,location,collection,patrons,checked_out):
        self.year=year
        self.location=location
        self.collection=collection
        self.patrons=patrons
        self.checked_out=checked_out
    def __str__(self):
        return("-- Library--\nName: {}{}Collection: {} books\nEstablished: {}{}Patrons: {}\nLocation: {}{}Books in Circulation: {}".format(self.name,(' '*(35-len('Name: '+self.name))),str(len(self.collection),str(self.year)),(' '*(35-len('Established: '+str(self.year)))),str(len(self.patrons)),self.location,(' '*(35-len('Location: '+self.location))),str(len(self.checked_out))))
        
    def add_books(self,add_books):
        self.collection += add_books
    def remove_books(self, remove_books):
        self.collection -= remove_books
    def add_patrons(self, add_patrons):
        self.patrons += add_patrons
    def remove_patrons(self, remove_patrons):
        self.patrons -= remove_patrons
    def library_size(self)
        library_size=len(self.collection)
        return library_size  
    def check_out_book(self,check_out_book,patron):
        self.checked_out[check_out_book]=patron
    def return_book(self,return_book):
        self.checked_out.pop(return_book)
        

    
    
        
        
        
        
        