# Internet Speed Test

This is a simple Python script to measure the download and upload speeds of your internet connection using the [speedtest-cli](https://github.com/sivel/speedtest-cli) library.

## Requirements

- Python 3.x
- speedtest-cli library (install it using `pip install speedtest-cli`)

## How to Use

1. Make sure you have Python 3.x installed on your system.
2. Install the required library by running `pip install speedtest-cli`.
3. Download the script from this repository.
4. Open a terminal or command prompt in the directory where the script is located.
5. Run the script using the command `python internet_speed_test.py`.

## Output

The script will perform an internet speed test by measuring the download and upload speeds using the speedtest-cli library. The results will be displayed on the console in Megabits per second (Mbps).

## Example Output

```
Getting download speed...
Getting upload speed...
Download: 50.23 Mbps
Upload: 20.11 Mbps
```

## How it Works

The script utilizes the `speedtest.Speedtest` class from the speedtest-cli library to perform the speed test. It measures the download and upload speeds in bytes per second and then converts them to Megabits per second (Mbps) for better readability.

## Disclaimer

Please note that the results of the speed test may vary based on various factors, including network congestion, server location, and your internet service provider. This script provides a general estimation of your internet speed at the time of running the test.

## Contribution

If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request in this repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per the terms of the license.
