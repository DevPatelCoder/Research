# Fast Short Convolution

A Python implementation demonstrating the **short cyclic convolution algorithms** described by R. C. Agarwal and J. W. Cooley, with a comparison against direct cyclic convolution.

## Overview

This project implements and compares two approaches for computing **cyclic convolution**:

1. **Direct cyclic convolution** – computes the convolution directly from its mathematical definition.
2. **Agarwal–Cooley short convolution** – reorganizes the computation to reduce the number of multiplications required for short convolution lengths.

The main purpose of this project is to demonstrate how a specialized convolution algorithm can significantly reduce the number of **multiplication operations**, while using additional additions.

For **N = 4**, the research paper reports:

| Method | Multiplications | Additions |
|---|---:|---:|
| Direct convolution | 16 | 12 |
| Agarwal–Cooley | 5 | 15 |

This represents a **68.75% reduction in multiplications**:

```text
(16 - 5) / 16 × 100 = 68.75%
```

The trade-off is an increase in additions from **12 to 15**.

> Note: The Agarwal–Cooley multiplication count of 5 does not include the calculation of the precomputed `Ah` transform, as specified in the research paper.

## What the Code Does

The `Comparison.py` file demonstrates the arithmetic advantage of the short convolution algorithm.

The code:

- Implements **direct cyclic convolution** using the defining convolution formula.
- Implements the **Agarwal–Cooley short convolution algorithm**.
- Uses short input sequences to demonstrate the specialized computation.
- Counts the number of **multiplications and additions**.
- Compares the operation counts of the two approaches.
- Calculates the percentage reduction in multiplication operations.

The main focus is on comparing the **arithmetic complexity** of the two convolution methods rather than comparing raw Python execution time.

## Cyclic Convolution

For an N-point cyclic convolution, the output is defined as:

```text
y_i = Σ h_(i-k) x_k
```

where the indices are evaluated modulo `N`.

The direct approach performs the required multiplication and addition for every combination of input elements.

The Agarwal–Cooley approach reorganizes these calculations into intermediate quantities so that fewer multiplications are required.

## Research Paper

This implementation is based on the research paper:

**R. C. Agarwal and J. W. Cooley,  
"New Algorithms for Digital Convolution,"  
IEEE Transactions on Acoustics, Speech, and Signal Processing,  
Vol. ASSP-25, No. 5, October 1977, pp. 392–410.**

The paper presents algorithms for digital convolution using multidimensional transformations and specialized short convolution algorithms.

It describes how short cyclic convolutions can be computed with fewer multiplications than direct convolution. The paper also develops algorithms for different short sequence lengths and shows how these algorithms can be used as building blocks for longer convolutions.

For `N = 4`, the paper specifically gives:

- **5 multiplications**
- **15 additions**

compared with:

- **16 multiplications**
- **12 additions**

for direct use of the defining convolution formula.

## Paper Links

### IBM Research

[New Algorithms for Digital Convolution — IBM Research](https://research.ibm.com/publications/new-algorithms-for-digital-convolution)

### IEEE Xplore

[New Algorithms for Digital Convolution — IEEE Xplore](https://doi.org/10.1109/TASSP.1977.1162981)

### DOI

[10.1109/TASSP.1977.1162981](https://doi.org/10.1109/TASSP.1977.1162981)

## Comparison

For `N = 4`:

| Operation | Direct Convolution | Agarwal–Cooley |
|---|---:|---:|
| Multiplications | 16 | 5 |
| Additions | 12 | 15 |

### Multiplication Reduction

```text
Direct multiplications = 16
Agarwal–Cooley multiplications = 5

Reduction = (16 - 5) / 16 × 100

Reduction = 68.75%
```

Therefore, the short convolution algorithm reduces the number of multiplication operations by **68.75%** for the `N = 4` case reported in the paper.

## Project Structure

```text
Research/
│
├── Comparison.py
└── README.md
```

## Requirements

```text
Python 3.x
```

No external Python libraries are required for the basic implementation.

## How to Run

Clone the repository:

```bash
git clone https://github.com/DevPatelCoder/Research.git
```

Navigate to the project directory:

```bash
cd Research
```

Run the Python program:

```bash
python Comparison.py
```

## Purpose

The purpose of this project is to provide a practical implementation of the ideas presented in the Agarwal–Cooley research paper and demonstrate the reduction in multiplication operations achieved by a specialized short convolution algorithm.

This project can be used to:

- Understand cyclic convolution.
- Study short convolution algorithms.
- Compare direct and optimized convolution approaches.
- Analyze multiplication and addition counts.
- Reproduce the `N = 4` operation-count comparison from the research paper.

## Reference

Agarwal, R. C., & Cooley, J. W. (1977).

**New Algorithms for Digital Convolution.**

*IEEE Transactions on Acoustics, Speech, and Signal Processing, ASSP-25*(5), 392–410.

DOI: [10.1109/TASSP.1977.1162981](https://doi.org/10.1109/TASSP.1977.1162981)
