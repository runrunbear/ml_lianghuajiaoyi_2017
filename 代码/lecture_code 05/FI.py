################# Force Index ########################################################

# Load the necessary packages and modules
import pandas as pd
import pandas.io.data as web

# Force Index 
def ForceIndex(data, ndays): 
 FI = pd.Series(data['Close'].diff(ndays) * data['Volume'], name = 'ForceIndex') 
 data = data.join(FI) 
 return data


# Retrieve the Apple data from Yahoo finance:
data = web.DataReader('AAPL',data_source='yahoo',start='1/1/2010', end='1/1/2016')
data = pd.DataFrame(data)

# Compute the Force Index for Apple 
n = 1
AAPL_ForceIndex = ForceIndex(data,n)
print(AAPL_ForceIndex)