import numpy as np
import pandas as pd
from pymongo import MongoClient

class PandasProcessor():
    '''
    Pull limited data from the spark processor/postgres to manipulate to be ready for graphing and analysis
    '''
    def __init__(self):
        self.read_mongo('craigslist','all_listings')
        self.clean_df()

    def _connect_mongo(self,host, port, db):
        """ A util for making a connection to mongo """

        conn = MongoClient(host, port)
        return conn[db]

    def read_mongo(self,db, collection, query={}, host='localhost', port=27017,no_id=True):
        """ Read from Mongo and Store into DataFrame """

        d = self._connect_mongo(host, port, db)
        cursor = d[collection].find(query)#.limit(10000)#use limit to control entity count for tests
        df =  pd.DataFrame(list(cursor))
        print('df loaded')
        if no_id:
            del df['_id']

        self.df = df

    def clean_df(self):
        ''' Call all cleaning methods '''
        self.df = self.df.convert_dtypes()
        self.clean_price()
        self.clean_postID()
        self.clean_name()
        self.clean_description()
        self.df = self.df.convert_dtypes()
        self.df.dropna(inplace=True)
        self.df = self.df.convert_dtypes()

    def clean_price(self):
        ''' Get price as a numeric value '''
        self.df['price'] = pd.to_numeric(self.df['price'].str.replace(r'\D','')) #.astype(int)
    def clean_postID(self):
        ''' Remove filler content from post id '''
        self.df['post_id'] = self.df['post_id'].str.replace('post id: ','')
    def clean_name(self):
        ''' Name was stored as a list, get the name '''
        self.df['name'] = self.df['name'].apply(lambda x: x[0]).astype(str)
    def clean_description(self):
        ''' description may be a list of strings, process it into one string '''
        self.df['des'] = self.df['des'].apply(lambda x: ' '.join(x)).astype(str)