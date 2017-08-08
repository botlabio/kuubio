import pandas as pd
import pkg_resources

data_path = 'https://github.com/autonomio/datasets/raw/master/autonomio-datasets/'

def load_data(name,mode):

    if mode == 'default':
    
        if name == 'election_in_twitter':
            out = pd.read_msgpack(data_path+'election_in_twitter')
        if name == 'sites_category_and_vec':
            out = pd.read_msgpack(data_path+'sites_category_and_vec')
        if name == 'programmatic_ad_fraud':
            out = pd.read_msgpack(data_path+'programmatic_ad_fraud')
        if name == 'parties_and_employment':
            out = pd.read_msgpack(data_path+'parties_and_employment')
        if name == 'tweet_sentiment':
            out = pd.read_msgpack(data_path+'tweet_sentiment')
        if name == 'random_tweets':
            out = pd.read_msgpack(data_path+'random_tweets')
        
        return out
            
    elif mode == 'file':
        
        if name.endswith('.csv'):
            
            try:
                out = pd.read_csv(name)
            except:
                out = pd.read_csv(name,error_bad_lines=False)
        
        elif name.endswith('.msgpack'):
            out = pd.read_msgpack(name)
        
        elif name.endswith('.json'):
            out = pd.read_json(name)
        
        else: 

            out = ''
            print "MAYBE UNSUPPORTED? only csv, json, and msgpack"
            
        return out