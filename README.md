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
