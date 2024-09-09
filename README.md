# Car Data Analysis Project

## Project Overview

The **Car Data Analysis** project is designed to collect and analyze data about various cars using an external API. The project is divided into several steps, including data collection, storage in a PostgreSQL database, and performing data analysis using Python and SQL. This documentation will provide a step-by-step explanation of each component of the project.

## Key Features

- **Data Collection:** Data is retrieved from the car information API available at [carapi.app](https://carapi.app/).
- **Data Storage:** The collected data is stored in a PostgreSQL database.
- **Data Analysis:** We perform data analysis on the collected data using Python's `pandas` library and SQL queries.

## Project Structure

The project consists of the following key files:

### 1. `carAPI.py`

- **Purpose:** This script is responsible for connecting to the external API and retrieving car data.
- **Key Functionality:**
  - Establishes a connection to the car API.
  - Sends requests to retrieve car-related data such as make, model, year, and other specifications.
  - Formats the retrieved data into a structured format for easy storage.

### 2. `database.py`

- **Purpose:** This script handles database operations, including connecting to PostgreSQL and inserting the data.
- **Key Functionality:**
  - Connects to a PostgreSQL database.
  - Creates necessary tables to store the car data.
  - Inserts the car data retrieved by `carAPI.py` into the database for further analysis.

### 3. `main.py`

- **Purpose:** This is the main script that coordinates the entire process of data collection and storage.
- **Key Functionality:**
  - Calls functions from `carAPI.py` to retrieve car data.
  - Calls functions from `database.py` to store the data in the PostgreSQL database.
  - Acts as the central point of execution for the project.

### 4. `car_data_analysis.ipynb`

- **Purpose:** This Jupyter Notebook file is used to analyze the stored car data.
- **Key Functionality:**
  - Connects to the PostgreSQL database to retrieve the data.
  - Uses Python's `pandas` library to perform various analyses, such as:
    - Summarizing car models by make and year.
    - Identifying trends in car specifications.
    - Analyzing the distribution of car prices, fuel types, and other metrics.
  - SQL queries are also used to perform more complex database operations directly on the stored data.

## How It Works

### 1. Data Collection

- The project uses Python to send requests to the [carapi.app](https://carapi.app/) API to collect car-related data.
- This data is then cleaned and organized to ensure it can be easily inserted into the database.

### 2. Data Storage

- The project connects to a PostgreSQL database.
- Tables are created to store the different types of data (e.g., car make, model, year, price).
- Data from the API is inserted into these tables for future analysis.

### 3. Data Analysis

- Using `pandas` in Python, we analyze the data to extract valuable insights.
- The analysis focuses on identifying trends, summarizing data, and answering specific questions related to the car industry.
- SQL is used to query the data in the database for more detailed analysis.

## Getting Started

### Prerequisites

To run this project, you'll need the following:

- Python 3.x
- PostgreSQL database
- Required Python libraries (can be installed via `requirements.txt`):
  - `pandas`
  - `requests`
  - `psycopg2` (for connecting to PostgreSQL)

### Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/car-data-analysis.git
   ```
