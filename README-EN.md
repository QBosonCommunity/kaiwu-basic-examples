# kaiwu-examples

[中文版本](README.md)

A Python toolkit for quantum optimization problems.


## Project Structure

```
kaiwu_quantum_toolkit/
└── tutorial/
    ├── tutorial1_qubo_matrix.py
    ├── tutorial2_tsp.py
    └── tutorial3_max_cut.py
```

## Requirements

- Python 3.8+
- NumPy >= 1.19.0
- Pandas >= 1.0.0
- Matplotlib >= 3.0.0
- Networkx >= 2.0
- Pytest >= 7.0.0 (for testing)

## Installation

```bash
# Recommended: Create a new conda environment
conda create -n quantum_env python=3.8
conda activate quantum_env

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Quick Start

### kaiwu-sdk Installation Guide

For detailed documentation, please visit [kaiwu-sdk Installation Instructions](https://kaiwu-sdk-docs.qboson.com/en/source/sdk_installation_instructions.html)

## Example Cases

### Classical Optimization Problems
- [QUBO Matrix](examples/tutorial1_qubo_matrix.py): Basic QUBO model construction and solution
- [TSP Problem](examples/tutorial2_tsp.py): Traveling Salesman Problem QUBO modeling
- [Max Cut Problem](examples/tutorial3_max_cut.py): Maximum Cut problem solution example

### Classical Optimization Problems (notebook)
- [QUBO Matrix](tutorial/notebook/tutorial1_qubo_matrix.ipynb): Basic QUBO model construction and solution
- [TSP Problem](tutorial/notebook/tutorial2_tsp.ipynb): Traveling Salesman Problem QUBO modeling
- [Max Cut Problem](tutorial/notebook/tutorial3_max_cut.ipynb): Maximum Cut problem solution example


## Development Guide

### Running Examples
```bash
python tutorial/tutorial1_qubo_matrix.py

python tutorial/tutorial2_tsp.py

python tutorial/tutorial3_max_cut.py
```

### Code Style
- Follow PEP 8 guidelines
- Use type annotations
- Write detailed docstrings

## Documentation

For detailed documentation, visit [documentation](https://kaiwu-sdk-docs.qboson.com/en/source/introduction.html)

## Contributing Guidelines

Pull Requests are welcome! Please ensure you follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Before Contributing
- Ensure all tests pass
- Update relevant documentation
- Add necessary unit tests
- Follow code standards

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

