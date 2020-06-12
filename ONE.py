class Data:
    import pandas as pd
    from pandas import DataFrame as pd_df
    from numpy import NaN
    from datetime import datetime
    import matplotlib.pyplot as plt
    
    def __init__(self, data_url=None, **kwargs):
        self.init_history()
        if data_url:
            self.load_data(data_url, **kwargs)

        self.col_types = {	'number':['number'],
							'object':['object'],
							'datetime':['datetime, datetime64'],
							'timedelta':['timedelta','timedelta64'],
							'category':['category'],
							'datetimetz':['datetimetz']
							}
            
    def load_data(self, data_url, **kwargs):
        '''This function let you load data from csv same like pandas.read_csv method'''
        self.DataFrame = self.pd.read_csv(data_url, **kwargs)
        self.update_history(f'Loaded DataFrame with shape {self.DataFrame.shape}')
        return self.DataFrame.head()

    @property
    def df(self):
        return self.DataFrame
    
    def head(self,rows=5):
        return self.DataFrame.head(rows)
    
    def init_history(self):
        self.history = self.pd.DataFrame({'Time': self.datetime.now(),'History':['Recording Started!',]})
        
    def update_history(self, update):
        self.history = self.pd.concat([self.history,self.pd_df({'Time': self.datetime.now(),'History':[update,]})])
        
    def print_history(self):
        print(self.history)
        
    def plotNaN(self, figsize=(10,10)):
        '''This function plots Missing Values in the dataset'''
        self.plt.figure(figsize=figsize)
        ( (self.DataFrame.isnull().sum() / self.DataFrame.shape[0]) * 100 ).sort_values().plot(kind='barh')
        self.plt.show()

class Clean():
    def __init__(self, data):
        self.Data = data
        self.backup = {}
        
    def replace(self, what, to_what=Data.NaN):
        """The Method replaces the dataframe's missed values with NaN.. 

        Args:
            what (any string or np.NaN): Example- '?' can be replaced to np.NaN
            to_what ([any type], optional): With what, the missing value should be replaced. Defaults to Data.NaN.

        Returns:
            Data Object: A class object custom made by PySanta
        """        
        self.store_backup(f'before replacing {what} with {to_what}', self.Data.DataFrame)
        self.Data.DataFrame = self.Data.DataFrame.replace(what, to_what)
        self.store_backup(f'after replacing {what} with {to_what}', self.Data.DataFrame)
        self.Data.update_history(f'Replaced {what} with {to_what}')
        return self
    
    def store_backup(self, key, data):
        """Stores backup of Data to a Data.backup dictionary with provided key in the args

        Args:
            key (string / int): [description]
            data ([type]): [description]
        """        
        self.backup[key] = data
    
    def dropRows(self, nan_limit=20):
        """Method to drop rows with NaN values (by default: 20 nan_limit)

        Args:
            nan_limit (int, optional): with what percent of nan-values, columns are to be dropped. Defaults to 20%.
        """        
        # backup before
        self.store_backup('before_drop_rows', self.Data.DataFrame)
        self.Data.update_history(f'Backup DF before Drop Rows of columns with nan values below {nan_limit}%')
        df = self.Data.DataFrame
        null = ((df.isnull().sum()/df.shape[0]) * 100).sort_values(ascending=False)
        print(f'Dropping Rows of all columns with below {nan_limit}% of null_values')
        for col in null[null < nan_limit].index:
            df = df[df[col].notna()]
        self.Data.DataFrame = df
        self.Data.update_history(f'Dropped Rows of columns by Applying dropRows method')
        self.Data.update_history(f'Backup DF after Drop Rows of columns with nan values below {nan_limit}%')
        self.store_backup('after_drop_rows', self.Data.DataFrame)
        
        
    def dropColumns(self, nan_limit=80, col_list=None):
        '''Method to drop columns with NaN values above nan_limit(by default: 80% )'''
        # backup before
        self.store_backup('before_drop_columns', self.Data.DataFrame)
        df = self.Data.DataFrame
        if col_list is None:
            null = ((df.isnull().sum()/df.shape[0]) * 100).sort_values(ascending=False)
            print(f'Dropping columns with above {nan_limit}% of null_values')
            drop_cols = list(null[null > nan_limit].index)
        else:
            drop_cols = col_list
        df = df.drop(drop_cols, axis=1)
        self.Data.DataFrame = df
        self.store_backup(f'after_drop_dropping_columns {", ".join(list(drop_cols))}', self.Data.DataFrame)

    def col_convert(self, col_list=False, type=False):
        '''This function tries to convert the dataframe columns to number col \
        after taking backup of the dataframe to backup dictionary of the Data Class'''
        self.store_backup('before_try_convert_columns', self.Data.DataFrame)
        df = self.Data.DataFrame
        if col_list and type:
        	print('This Fascility not implimented yet!')
        else:
	        for col in df.select_dtypes(include=self.Data.col_types['object']).columns:
	        	try:
	        		#df[col] = df[col].map(lambda x : int(str(x).split('.')[0]) if str(x).split('.')[-1][0]=='0' else x)
	        		df[col] = df[col].astype('int64')
	        	except:
	        		try:
	        			df[col] = df[col].astype('float')
	        		except:
	        			df[col] = df[col]
        self.Data.DataFrame = df
        self.Data.update_history(f'tried_convert function')
        self.store_backup('before_try_convert_columns', self.Data.DataFrame)


