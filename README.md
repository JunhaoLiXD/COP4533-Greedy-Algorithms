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
  - `FIFO.py` : Implements the FIFO (First-In, First-Out) cache replacement algorithm.
  - `LRU.py` : Implements the LRU (Least Recently Used) cache replacement algorithm using a doubly linked list and a hashmap.
  - `OPTFF.py` : Implements the OPTFF (Optimal Farthest-in-Future) cache replacement algorithm.
  - `io_utils.py` : Provides helper functions for reading input files and writing output files.

- `inputs/` : Example input files for testing cache policies
  - `example_input.txt` : Sample request sequence input.
  - `bad_sequence.txt` : Example bad sequence demonstrating OPTFF outperforming other policies.
  - `file1.txt` : Benchmark input file with 60 requests.
  - `file2.txt` : Benchmark input file with 64 requests.
  - `file3.txt` : Benchmark input file with 70 requests.

- `outputs/` : Generated program outputs
  - `example_output.txt` : Example output produced by running the simulator.
  - `file1.txt` : Output results for file1 benchmark
  - `file2.txt` : Output results for file2 benchmark
  - `file3.txt` : Output results for file3 benchmark.

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

## Written Component

### Question 1: Empirical Comparison

We tested three nontrivial input files (each with 50+ requests).  
The number of cache misses for each policy is shown below.

| Input File | k | m | FIFO | LRU | OPTFF |
|-----------:|--:|--:|-----:|----:|------:|
| file1.txt  | 3 | 60 | 48 | 36 | 28 |
| file2.txt  | 4 | 64 | 64 | 64 | 28 |
| file3.txt  | 5 | 70 | 46 | 64 | 25 |

**Observations**
- OPTFF has the fewest misses in all cases, as expected for an optimal offline algorithm.
- FIFO vs LRU depends on access patterns: LRU is better on file1, tied on file2, and worse on file3.


### Question 2: Bad Sequence for LRU or FIFO

For cache size 𝑘 = 3, there exists a request sequence where OPTFF has strictly fewer misses than LRU and FIFO.

Consider the sequence:

    1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4


This sequence repeats the pattern 1, 2, 3, 4 five times.

The cache can only hold 3 pages, but the sequence uses 4 different pages.

**Under FIFO and LRU**

After the first three requests, the cache becomes full.

From that point on, every request asks for the one page that is not currently in the cache.

FIFO and LRU both use only past information.
They cannot predict the future.

So they repeatedly remove a page that will soon be requested again.

As a result, every request causes a miss.

Miss counts:
- FIFO misses: 20
- LRU misses: 20

**Under OPTFF**

OPTFF knows the future. When it must evict a page, it removes the page whose next use is farthest in the future.

This avoids removing the next-needed page.

Miss count:

- OPTFF misses: 9

Since 9 < 20, OPTFF has strictly fewer misses than FIFO and LRU on this sequence.

### Question 3: Prove OPTFF is Optimal

Let the request sequence be:

r1, r2, ..., rm.

Let A be any offline algorithm that knows the full request sequence.

We want to prove that the number of misses of OPTFF is no larger than that of A on any fixed sequence.

**Proof**

Assume that A is an optimal offline algorithm.

If A always makes the same eviction choices as OPTFF, then both algorithms have the same number of misses.

Now suppose there is a first time when A and OPTFF choose different pages to evict during a miss.

At this step:

- OPTFF evicts page p, which is used farthest in the future.
- A evicts a different page q.

We construct a new algorithm A′ that behaves exactly like A, except at this step it evicts p instead of q.

After this change:

- A keeps p but not q.
- A′keeps q but not p.

Since OPTFF chose p as the page used farthest in the future, the next request to q occurs before the next request to p.

When q is requested:

- A will have a miss.
- A′ will have a hit.

So A′ does not have more misses than A.

We can repeat this process every time A differs from OPTFF.
Each change does not increase the number of misses.

Therefore, OPTFF has no more misses than any other offline algorithm A.

Hence, OPTFF is optimal.