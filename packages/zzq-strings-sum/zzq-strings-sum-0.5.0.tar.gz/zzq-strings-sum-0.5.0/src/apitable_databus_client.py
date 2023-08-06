import requests
import logging

class DatabusClient:
    """
    DatabusClient is a client for making HTTP requests to the Databus API.
    It provides a simple interface to send GET requests and retrieve JSON data.

    Parameters:
        host (str): The base URL of the Databus API.

    Usage:
        host_address = "https://integration.vika.ltd"
        client = DatabusClient(host_address)

        datasheet_id = "dstbUhd5coNXQoXFD8"
        result = client.get_datasheet_pack(datasheet_id)

        if result:
            print(result)
        else:
            print("Request failed.")
    """

    def __init__(self, host):
        """
        Initialize a new DatabusClient instance.

        Args:
            host (str): The base URL of the Databus API.
        """
        self.host = host
        self.logger = logging.getLogger("DatabusClient")
        self.logger.setLevel(logging.DEBUG)

        # Create a console handler for logging
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create a formatter and attach it to the handler
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)

        # Add the console handler to the logger
        self.logger.addHandler(ch)

    def get_datasheet_pack(self, datasheet_id):
        """
        Send a GET request to the Databus API to fetch the datasheet pack data.

        Args:
            datasheet_id (str): The ID of the datasheet to retrieve.

        Returns:
            dict or None: A dictionary containing the JSON data from the response,
                          or None if the request failed.
        """
        url = f"{self.host}/databus/get_datasheet_pack/{datasheet_id}"
        headers = {'accept': '*/*'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception if the request is unsuccessful

            json_data = response.json()
            return json_data
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error occurred during the request: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    # Configure logging to show debug messages
    import logging
    logging.basicConfig(level=logging.DEBUG)

    host_address = "https://integration.vika.ltd"
    client = DatabusClient(host_address)

    datasheet_id = "dst9zyUXiLDYjowMvz"
    result = client.get_datasheet_pack(datasheet_id)
    if result:
        print("result message", result['message'])
        print("result code", result['code'])
    else:
        print("Request failed.")
