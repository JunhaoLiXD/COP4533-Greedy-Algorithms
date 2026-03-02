# COP4533–Greedy-Algorithms

This repository contains the implementation for a COP4533 Greedy Algorithms programming assignment. The project simulates cache eviction policies and compares their performance by counting cache misses for a given request sequence.

## Team Members
- Name: Yuyang Sun, UFID: 38133550  
- Name: Junhao Li, UFID: 51521823

## Requirements / Dependencies
- Python **3.x**
- No external libraries are required.

## Project Structure
- `src/` : Core implementation files for cache simulation
  - `OPTFF.py` : Implements the OPTFF (Optimal Farthest-in-Future) cache replacement algorithm.
  - `io_utils.py` : Provides helper functions for reading input files and writing output files.

- `inputs/` : Example input files for testing cache policies
  - `input_file1.txt` : Sample request sequence input.
  - `bad_sequence.txt` : Example bad sequence demonstrating OPTFF outperforming other policies.

- `outputs/` : Generated program outputs
  - `output_file1.txt` : Example output produced by running the simulator.

- `scripts/` : Helper scripts for generating and testing inputs
  - `generate_inputs.py` : Generates random input files following the required assignment format.

- `main.py` : Program entry point; parses arguments, runs cache policies, and writes results.

- `.gitignore` : Specifies files and directories ignored by Git.

- `README.md` : Project documentation and usage instructions.

## Input Format

The program reads a cache simulation input file describing the cache capacity
and a sequence of requests.

The input file must contain **exactly two lines**:

1. First line: two integers `k m`
   - `k` : cache capacity (`k ≥ 1`)
   - `m` : number of requests

2. Second line: a sequence of `m` integers:

    r1 r2 r3 ... rm

Each integer represents the ID of a requested item.

### Example Input

    3 20
    2 1 5 4 4 3 2 9 2 10 7 1 1 2 4 4 9 10 1 9


## Output Format

The program writes cache miss counts to an output file.

Each line reports the number of misses for one cache replacement policy:

    FIFO:  <number_of_misses>
    LRU:   <number_of_misses>
    OPTFF: <number_of_misses>

### Example Output

    FIFO  : 15
    LRU   : 15
    OPTFF : 11


## How to Run

The program is executed from the repository root directory and requires
two command-line arguments:

    python main.py <input_file> <output_file>

Where:

- `<input_file>` : path to the cache request input file
- `<output_file>` : path where the program will write the results

### Step-by-step Instructions

1. Open a terminal.
2. Navigate to the project root directory.
3. Run the program using Python with an input file and an output file path.

### Example

Suppose the repository contains the following file:

    inputs/example_input.txt

Run the program using:

    python main.py inputs/example_input.txt outputs/example_output.txt
