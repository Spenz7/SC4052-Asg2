# PageRank Implementation

This repository contains a Python implementation of the PageRank algorithm and the dataset used for evaluation.

## Files

- **calcPageRank.py** – Python script implementing both iterative and closed-form PageRank algorithms using a sparse matrix representation. Handles dangling nodes, non-consecutive page IDs, and large sparse graphs efficiently.
- **web-Google_10k.txt** – Sample dataset (10,000 pages, 78,323 links) used for testing. The first 4 lines are metadata and are skipped by the script.

## Dependencies

- Python 3.x
- NumPy
- SciPy

Install required libraries using:

```bash
pip install numpy scipy
```

## Usage

1.  Clone the repository or download the file:

```bash
git clone https://github.com/Spenz7/SC4052-Asg2.git
cd SC4052-Asg2/Task3
```

2.  Run the script:

```bash
python calcPageRank.py
```
