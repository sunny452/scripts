import pandas as pd
import json

def lambda_handler(event, context):
    a = [5, 7, 4, 9]
    srs = pd.Series(a)
    
    print(srs)
    
    return {
        'statusCode': 200,
        'body': json.dumps('imported pandas')
    }
