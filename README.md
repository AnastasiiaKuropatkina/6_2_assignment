# Temperature and Distance Conversion Tool

This project provides a simple tool for converting temperature readings between Celsius and Fahrenheit, as well as distance measurements between meters and feet. It can process input data .csv files to convert measurement units according to user specifications.

## Features

Temperature conversion: **Celsius** <-> **Fahrenheit**

Distance conversion: **Meters** <-> **Feet**

Bulk processing of data from **CSV files**

## Getting Started
### Prerequisites

Before running the conversion tool, ensure you have Python 3.8 or later installed on your system.

### Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/AnastasiiaKuropatkina/6_2_assignment/
```

Navigate to the cloned directory:

```bash
cd 6_2_assignment
```

### Usage

To use the conversion tool, you need to have an input CSV file with the format specified in the project documentation. Here's a quick example of how to run a conversion:

1. Prepare your input CSV file (e.g., `input.csv`) with the appropriate data.
2. Run the conversion script with the desired parameters. For example, to convert temperatures to Celsius and distances to meters, use:

```bash
python3 main.py
```

The function has 4 parameters `convert_temperatures('input.csv', 'output.csv', 'm', 'C')`

Replace `C` to `F` for Fahrenheit, and `m` to `ft` for feet as needed.

### Contributing

We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.
