import boto3
import json

class DataStorage:
    def __init__(self):
        # Load AWS S3 credentials from the JSON configuration file
        with open("DSSC-FC-MVP-Configuration.JSON", "r") as config_file:
            config_data = json.load(config_file)
        
        self.s3_access_key = config_data["aws_access_key"]
        self.s3_secret_key = config_data["aws_secret_key"]
        self.s3_bucket_name = config_data["s3_bucket_name"]
        
        # Initialize the S3 client
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=self.s3_access_key,
            aws_secret_access_key=self.s3_secret_key
        )

    def store_data_in_s3(self, data, file_name):
        try:
            # Upload data to AWS S3
            self.s3_client.put_object(
                Bucket=self.s3_bucket_name,
                Key=file_name,
                Body=data.to_csv(index=False)
            )
            print(f"Data stored in AWS S3 with key: {file_name}")
        except Exception as e:
            print(f"Error storing data in AWS S3: {str(e)}")
