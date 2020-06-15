#!/bin/sh

python output_generator.py
python output_verifier.py
echo "\n\ntime required for input_6:"
time python solver_mysolver.py input_6.csv