import yfinance as yf
import pandas as pd
import boto3
import os

class FinancialDataCollector:
    def __init__(self):
        self.start_date = "2021-01-01"
        self.end_date = "2021-12-31"

    def get_stock_data(self, symbol):
        try:
            data = yf.download(symbol, start=self.start_date, end=self.end_date)
            return data
        except Exception as e:
            print(f"Error fetching data for {symbol}: {str(e)}")
            return None

    def display_data(self, data):
        if data is not None:
            print(data)

    def save_to_s3(self, data, s3_object_name):
        aws_access_key_id = "AKIA42ARABXML56IV7UQ"  # Replace with your AWS Access Key ID
        aws_secret_access_key = "haAdVOaruJJ+1kKvEI8nxQnSP60C2VwSaFUx1XMR"  # Replace with your AWS Secret Access Key
        bucket_name = 'financial-data-storage'

        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        # Specify the local file path based on the symbol
        local_file_path = f'{s3_object_name}.csv'
        s3.upload_file(local_file_path, bucket_name, s3_object_name)

        print(f'File {local_file_path} uploaded to S3 bucket {bucket_name} as {s3_object_name}.csv')

def main():
    data_collector = FinancialDataCollector()
    symbols = ["MSFT", "IBM"]

    for symbol in symbols:
        print(f"Fetching data for {symbol} from {data_collector.start_date} to {data_collector.end_date}:")
        stock_data = data_collector.get_stock_data(symbol)
        data_collector.display_data(stock_data)

        if stock_data is not None:
            # Dynamically generate local file name based on the symbol
            local_file_name = f'{symbol}_financial_data'
            stock_data.to_csv(f'{local_file_name}.csv', index=False)
            data_collector.save_to_s3(stock_data, f'{local_file_name}')

        print("\n" + "=" * 40 + "\n")

if __name__ == "__main__":
    main()
