# Import necessary modules
from DSSC_FC_MVP import FinancialDataCollector
from DSSC_FC_MVP_Storage import DataStorage

def main():
    # Instantiate the FinancialDataCollector class
    data_collector = FinancialDataCollector()

    # List of stock symbols to retrieve data for (Microsoft and IBM in this case)
    symbols = ["MSFT", "IBM"]

    for symbol in symbols:
        print(f"Fetching data for {symbol} from {data_collector.start_date} to {data_collector.end_date}:")
        stock_data = data_collector.get_stock_data(symbol)

        # Instantiate the DataStorage class
        data_storage = DataStorage()

        if stock_data is not None:
            # Store data in AWS S3 with a file name (e.g., "MSFT_data.csv")
            file_name = f"{symbol}_data.csv"
            data_storage.store_data_in_s3(stock_data, file_name)

            # Display the fetched data
            data_collector.display_data(stock_data)
            print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()
