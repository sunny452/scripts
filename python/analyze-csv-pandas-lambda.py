import json
import boto3
import base64
import pandas as pd

def lambda_handler(event, context):
    
   s3_client =boto3.client('s3')
   s3_bucket="s3fileupload"
   
   file_content=event["content"]
   params = event["params"]
   print(params)
   content_decoded=base64.b64decode(file_content)
   s3_upload =s3_client.put_object(Bucket=s3_bucket, Key='uploaded-file.csv', Body=content_decoded)
   
   #bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
   #s3_file_name = event["content"][0]["s3"]["object"]["key"]
   #print(s3_file_name)
   resp = s3_client.get_object(Bucket=s3_bucket, Key='uploaded-file.csv')
       
   df = pd.read_csv(resp['Body'], sep=',')
   #print(df.info())

   return {
       'statusCode': 200,
       'body': json.dumps('worked')
   }
