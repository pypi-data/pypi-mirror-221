import PAMI.extras.dbStats.transactionalDatabaseStats as tds

class frequenciesOfItems:
    """
    A class used to calculate the frequency of every item
    in the database and outputit as a dictionary.
    
    Attributes
    ----------
    transactional_database : str
        the path tothe database (csv file)
    separator : character
        the separator of the database
    
    Methods
    -------
    getFrequencies()
        calculates the frequency of each sensor and output as a
        dictionary.
    """
    
    def __init__(self, transactional_database, separator):
        """
        Parameters
        ----------
        transactional_database : str
            the path tothe database (csv file)
        separator : character
            the separator of the database
        """
        self.transactional_database = transactional_database
        self.separator = separator
    
    def getFrequencies(self):
        """
        Function to calculate the frequency each sensor and output as a
        dictionary.
        """
        #initialize the program
        obj = tds.transactionalDatabaseStats(self.transactional_database)
        obj = tds.transactionalDatabaseStats(self.transactional_database,sep=self.separator) 
        
        #execute the program
        obj.run()
        
        itemFrequencies = obj.getSortedListOfItemFrequencies()
        return dict(itemFrequencies)
