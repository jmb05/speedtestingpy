# Internet speed testing

## Speed-Testing

The `speedtesting.py` script connects to cloudflare to test the internet
speed. 

### Running the test

Execute the command in the `speedtesting/` directory: `.python/bin/python speedtesting.py`

### The Output

The script creates an output file `results_dd_mm_yyyy.csv`. The first line of the csv file shows which data is in which column.

## Plotting the Data

The `plotting.py` script plots the data of a given csv file.

### Usage

Execute the command: `.python/bin/python plotting.csv path/to/results_1.csv [path/to/results_2.csv...]`.

### Output

It creates a `bandwidth.svg` and a `ping_jitter.svg`, with the plot for up and down and the plot for ping and jitter respectively. The x-Axis shows the the time when the data was recorded and the y-Axis shows Mbps or ms.
