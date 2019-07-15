class ProductName:

    def __init__( self, name = None ):
        self.name = name
    
    def getName( self ):
        return self.name
    
    def readproductname( self ):
        return self.name
    
    def __repr__( self ):
        s = '{0:<10}'.format( self.name )
        return s

class ProductInfo( ProductName ):

    def __init__( self, name = None, price = 0 ):
        super().__init__( name )
        self.price = price

    def getPrice( self ):
        return self.price

    def readProductInfo( self ):
        return super().readproductname, self.price

    def __repr__( self ):
        s = super().__repr__()
        for i in range( len(self.price) )
            s = s + '{0:3}'.format( self.price[ i ])
        s = s + '{0:3}'.format( self.price )

        return s

class SalesInfo( ProductName ):

    def __init__( self, name = None, ea = 0 ):
        super().__init__( name )
        self.ea = ea

    def getEa( self ):
        return self.ea

    def readProductInfo( self ):
        return super().readproductname, self.ea

    def __repr__( self ):
        s = super().__repr__()
        for i in range( len(self.ea) )
            s = s + '{0:3}'.format( self.ea[ i ])
        s = s + '{0:3}'.format( self.ea )

        return s


class SalesHistory( ProductInfo, SalesInfo ):

    def __init__( self, name = None, price = 0, ea = 0, saleprice = 0 ):
        super().__init__( name, price, ea )
        self.saleprice = saleprice

    def getSalePrice( self ):
        return self.getSalePrice
    
    def readSalesHistoryInfo( self ):
        return 
