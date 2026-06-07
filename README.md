# IoT-Data-Optimizer

A lightweight utility for IoT developers to reduce data transmission and storage costs by downsampling high-frequency sensor readings.

## Why this tool?
IoT sensors often generate more data than needed. This script intelligently reduces the dataset size while preserving the signal's trend, saving bandwidth and cloud storage costs.

## Usage
`python downsampler.py input.csv output.csv <factor>`
Example: `python downsampler.py sensor_data.csv optimized.csv 10` (keeps every 10th sample).

## Support the Developer
If this helped you cut your cloud bill, consider supporting the project:
USDT (TRC20): `TN7GmnsAt8K1nZQPHEz9LWZrY1aEPL22iK`

