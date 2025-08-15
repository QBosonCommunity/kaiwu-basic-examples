<img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python Version">
<img src="https://img.shields.io/badge/License-Apache%202.0-green" alt="License">

[中文版本](README-zh.md)

## Project Introduction

`kaiwu-basic-examples` is an open-source collection of examples focused on quantum optimization problems, designed to help developers and researchers get started in the field of quantum optimization through hands-on practice. This project provides a systematic learning path for users who want to learn quantum optimization from scratch, covering the entire process from basic concepts to practical examples. The community's goals are:

- **Knowledge Popularization**: Help users understand the core concepts of quantum optimization problems and their modeling methods. For more information, please refer to the [Community Documentation](https://kaiwu.qboson.com/plugin.php?id=knowledge).
- **Practical Skills**: Learn how to implement quantum optimization algorithms using Python through real-world examples.
- **Community Growth**: Foster the transition of users from learners to contributors, promoting the collective progress of the community.

This project is not just a tool, but a platform for learning and growth. Whether you are a beginner in quantum computing or an experienced developer, you can benefit from it.

## Contribution Guide

### Why Contribute?

By participating in this project, you can not only deepen your understanding of quantum optimization problems but also contribute to the community and help other learners grow. We also offer cutting-edge research topics in our quantum development lab and provide certain rewards to contributors. We hope to build a vibrant learning and contribution-oriented community with your participation.

### How to Start Contributing?

1. **Report Issues**:
   - If you find a bug or have suggestions for improvement, please submit them in GitHub Issues.
   - When submitting, please describe the context of the problem and the steps to reproduce it clearly.

2. **Contribute Code**: 
   - Write code according to the task requirements.
   - Submit code by forking the repository and creating a branch.
   - Before submitting, please ensure that the code passes tests and complies with the project's standards.

3. **Participate in Discussions**:
   - Participate in feature discussions or share your experience in GitHub Discussions.

### Code Contribution Workflow

1. **Fork the Repository**:
   - Click the `Fork` button to copy the project to your own account.

2. **Clone the Code**:
   ```bash
   git clone https://github.com/your-username/kaiwu-basic-examples.git
   cd kaiwu-basic-examples
   ```

3. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Commit Your Code**:
   ```bash
   git add .
   git commit -m "Describe your changes"
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**:
   - On GitHub, click `New Pull Request` and fill in the description of your changes.

## Quick Start

### Requirements

- Python 3.10+
- NumPy >= 1.19.0
- Pandas >= 1.0.0
- Matplotlib >= 3.0.0
- Networkx >= 2.0
- Pytest >= 7.0.0 (for testing)

### Code Style

- Follow PEP 8 guidelines
- Use type annotations
- Write detailed docstrings

### Installation Steps

1. **Create and Activate Environment**:
   ```bash
   # It is recommended to use conda to create a new environment
   conda create -n quantum_env python=3.10
   conda activate quantum_env
   ```

2. **Clone this repository**:
   ```bash
   git clone https://github.com/QBosonCommunity/kaiwu-basic-examples.git
   cd kaiwu-basic-examples
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install in Development Mode (Optional)**:
   ```bash
   pip install -e .
   ```

### kaiwu-sdk Installation (Required)

Before you begin, you need to install the `kaiwu-sdk` dependency:

1. **Get the SDK**:
   - Visit the [kaiwu-sdk download page](https://platform.qboson.com/sdkDownload) (account registration required).
   - See the [kaiwu-sdk installation guide](https://kaiwu.qboson.com/plugin.php?id=knowledge&modac=docs&link=KaiwuSDK&name=%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B).

2. **Configure Authorization**:
   Obtain your SDK authorization credentials:
   ```
   User ID: <your-user-id>
   SDK Token: <your-sdk-token>
   ```
   > Please replace the above with your actual credentials.

### Getting Access to a Real Quantum Computer

To help you experience the practical application of quantum computing, you can follow these steps to get access to a real machine:

1. Register an account on the [Coherent Ising Machine Cloud Platform](https://platform.qboson.com/).
2. Complete the platform's SDK beginner tutorial to get credits for real machine calls. Refer to the [documentation](https://kaiwu-sdk-docs.qboson.com/en/latest/). 

### Running Your First Example

Replace this line in the example code:
```python
kw.license.init(user_id="xxxxxxx", sdk_code="xxxxxxx")
```

For example (this is not a real account, please apply for one on the cloud platform):
```python
kw.license.init(user_id="39302589031902227330", sdk_code="v1A22GNmyhP063a4t7Osa2HsAMkuaB")
```

Here is an example of how to run the QUBO matrix construction and solving script:
```bash
python tutorial/tutorial1_qubo_matrix.py
```
This example will help you quickly call the functions and solve a problem.

## Example Cases

### Classical Optimization Problems
- [QUBO Matrix](tutorial/tutorial1_qubo_matrix.py): Basic QUBO model construction and solving.
- [TSP Problem](tutorial/tutorial2_tsp.py): QUBO modeling for the Traveling Salesman Problem.
- [Max Cut Problem](tutorial/tutorial3_max_cut.py): Example of solving the Max Cut problem.
- [Submit TSP Task to a Real Machine](tutorial/tutorial4_cimoptimizer.py): Example of solving the TSP problem using a real machine.

### Classical Optimization Problems (Notebook)
- [QUBO Matrix](tutorial/notebook/tutorial1_qubo_matrix.ipynb): Basic QUBO model construction and solving.
- [TSP Problem](tutorial/notebook/tutorial2_tsp.ipynb): QUBO modeling for the Traveling Salesman Problem.
- [Max Cut Problem](tutorial/notebook/tutorial3_max_cut.ipynb): Example of solving the Max Cut problem.

## Directory Structure

```
kaiwu-basic-examples/
├── tutorial/
│   ├── notebook/
│   │   ├── tutorial1_qubo_matrix.ipynb     # QUBO Matrix notebook
│   │   ├── tutorial2_tsp.ipynb             # TSP notebook
│   │   └── tutorial3_max_cut.ipynb         # Max Cut notebook
│   ├── tutorial1_qubo_matrix.py            # QUBO Matrix example
│   ├── tutorial2_tsp.py                    # TSP example
│   ├── tutorial3_max_cut.py                # Max Cut example
│   └── tutorial4_cimoptimizer.py           # CIM Optimizer example
├── requirements.txt                        # List of dependencies
├── setup.py                                # Installation script
└── README.md                               # This document
```

## Community and Support

1. **Questions and Discussions**:
   - [GitHub Discussions](https://github.com/QBosonCommunity/kaiwu-basic-examples/discussions)

2. **Reporting Issues**:
   - [GitHub Issues](https://github.com/QBosonCommunity/kaiwu-basic-examples/issues)

3. **Contact via Email**:
   - developer@boseq.com

## Acknowledgments

- Thanks to all contributors for their valuable contributions.
- Thanks to the quantum computing community for their support and feedback.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

