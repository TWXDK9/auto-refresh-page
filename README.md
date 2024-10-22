
# Auto Refresh Page Script

This Python script automatically refreshes a webpage at regular intervals. It is customizable, allowing you to define the refresh interval, webpage URL, and the total runtime duration. The script is built using the [DrissionPage](https://github.com/g1879/DrissionPage) library, which leverages Chrome for browser automation.

## Features

- Automatically refreshes a webpage at a user-defined interval.
- Customizable runtime duration.
- Customizable webpage URL.
- Logs each refresh with the current timestamp.
- Error handling for network or browser failures.

## Requirements

This project requires Python 3.6 or higher and the following Python libraries:

- `DrissionPage`
- `selenium`
- Other dependencies listed in the `requirements.txt` file.

## Installation

### 1. Clone the repository

To get started, first clone the repository to your local machine:

```bash
git clone https://github.com/your-username/auto-refresh-page.git
cd auto-refresh-page
```

### 2. Install dependencies

The project dependencies are listed in the `requirements.txt` file. You can install them using `pip`.

#### Using `pip`:

```bash
pip install -r requirements.txt
```


```

## Usage

### Running the script

To run the script, use the following command in the project directory:

```bash
python auto_refresh_page_script.py --url "https://xxxxxxx.com" --interval 240 --hours 2
```

### Parameters

You can customize the behavior of the script by modifying the following parameters:

- **`--url`**: The URL of the webpage to refresh.
- **`--interval`**: The time interval (in seconds) between each page refresh. (Default: 240 seconds)
- **`--hours`**: How long the script will run before stopping, measured in hours. (Default: 2 hours)

### Example Usage in Code

Here’s how you might call the function in the script to refresh the page every 240 seconds for 2 hours:

```bash
python auto_refresh_page_script.py --url "https://xxxxxxx.com" --interval 240 --hours 2
```

This will refresh the page located at the specified URL every 240 seconds (4 minutes) and will continue running for 2 hours before stopping.

### Output

During execution, the script will log the following information in the console:

- **Timestamp for each page refresh**.
- **Any errors encountered** during execution (with automatic retries).

Example output:

```
Page refreshed at 2024-10-21 10:30:00
Page refreshed at 2024-10-21 10:34:00
Page refreshed at 2024-10-21 10:38:00
...
Program has finished running.
```

### Customization

You can modify the following parameters in the script:

- **`url`**: The URL of the webpage you want to refresh.
- **`refresh_interval`**: The time interval between each refresh, in seconds.
- **`run_hours`**: The total time the script will run, in hours.

## Error Handling

The script includes basic error handling. If an error occurs while refreshing the page (e.g., network issues or browser crashes), the script will attempt to reload the webpage and continue running.

## Dependencies

The required Python packages can be found in the `requirements.txt` file. Here are the main dependencies:

- `DrissionPage`: A Python library for automating browsers using Chrome or Chromium.
- `selenium`: The underlying framework for browser automation.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! If you’d like to improve the script or add more features, feel free to fork the repository and submit a pull request.
