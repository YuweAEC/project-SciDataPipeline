#!/bin/bash
# Test script for data processing

echo "Running tests..."

# Check if the combined data file is created
if [ -f "../data/combined.dat" ]; then
    echo "Test Passed: Combined data file exists."
else
    echo "Test Failed: Combined data file does not exist."
fi
