# Engineering Calculator

A modular Python library for engineering calculations and formulas.

The goal of this project is to build a reusable collection of engineering formulas that can be used across multiple applications, including command-line tools, desktop applications, web applications, APIs, and other Python projects.

Rather than writing engineering equations repeatedly in different projects, this library provides a centralized, tested, and well-documented implementation of commonly used engineering calculations.

---

## Objectives

* Create a reusable engineering calculation library.
* Organize formulas by engineering discipline.
* Maintain accurate and tested implementations.
* Support future expansion into a desktop application, web application, or API.
* Encourage clean software architecture and collaboration.

---

## Features

The project is designed to eventually include formulas from multiple engineering disciplines, including:

* Mechanical Engineering
* Structural Engineering
* Fluid Mechanics
* Electrical Engineering
* Materials Engineering
* Engineering Geometry
* Unit Conversions

---

## Project Structure

```text
engineering-calculator/
│
├── docs/
├── scripts/
├── src/
│   └── engineering_calc/
├── tests/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

---

# Directory Overview

## `docs/`

Contains project documentation.

```
docs/
├── api.md
├── formulas.md
└── examples.md
```

### `api.md`

Documents every function in the library.

Includes:

* Parameters
* Return values
* Exceptions
* Usage examples

---

### `formulas.md`

Contains engineering theory and mathematical equations used throughout the project.

Example topics include:

* Beam bending
* Fluid pressure
* Electrical power
* Stress and strain

---

### `examples.md`

Contains worked examples demonstrating how each calculation is used.

---

## `scripts/`

Contains helper scripts used during development.

Example:

```
scripts/
└── run.py
```

This file may later launch a command-line interface or perform development tasks.

---

## `src/`

Contains the actual source code for the Engineering Calculator library.

```
src/
└── engineering_calc/
```

Everything inside this package is importable into other Python projects.

Example:

```python
from engineering_calc.mechanics.beam import bending_stress
```

---

## `engineering_calc/`

The main package.

### `__init__.py`

Marks the folder as a Python package and exposes commonly used functions and constants.

---

### `constants.py`

Stores reusable engineering constants.

Examples:

* Gravity
* Pi
* Material densities
* Elastic modulus
* Standard atmospheric pressure

---

### `exceptions.py`

Defines custom exceptions specific to engineering calculations.

Example:

```python
raise InvalidUnitError("Pressure cannot be negative.")
```

---

### `cli.py`

Future command-line interface for interacting with the calculator.

Example:

```bash
python scripts/run.py
```

---

# Engineering Modules

Each engineering discipline has its own folder to keep the project organized and scalable.

---

## `mechanics/`

Mechanical engineering formulas.

Files include:

* `beam.py`
* `statics.py`
* `dynamics.py`
* `strength.py`

Example calculations:

* Beam bending stress
* Shear stress
* Equilibrium
* Newton's Laws
* Stress and strain
* Factor of Safety

---

## `fluids/`

Fluid mechanics calculations.

Files include:

* `pressure.py`
* `flow.py`
* `bernoulli.py`

Example calculations:

* Pressure
* Flow rate
* Velocity
* Hydraulic head
* Bernoulli's Equation

---

## `electrical/`

Electrical engineering calculations.

Files include:

* `dc.py`
* `ac.py`
* `power.py`

Example calculations:

* Ohm's Law
* Electrical Power
* Voltage
* Current
* Resistance
* Three-phase power

---

## `materials/`

Material property calculations.

Files include:

* `steel.py`
* `concrete.py`
* `timber.py`

Example calculations:

* Density
* Elastic modulus
* Yield strength
* Thermal expansion

---

## `geometry/`

Geometry calculations used throughout engineering.

Files include:

* `areas.py`
* `volumes.py`
* `centroids.py`

Example calculations:

* Area
* Volume
* Surface Area
* Centroid
* Moment of Inertia

---

## `units/`

Handles unit conversions.

Example conversions:

* mm → m
* cm → m
* kN → N
* MPa → Pa
* °C → K

Keeping conversions in one place helps prevent calculation errors caused by inconsistent units.

---

## `utils/`

General helper functions shared throughout the project.

### `validation.py`

Validates user input before calculations.

Examples:

* Positive numbers
* Non-zero values
* Valid dimensions

---

### `rounding.py`

Provides consistent rounding functions for engineering calculations.

---

# `tests/`

Contains automated tests.

Every engineering formula should have corresponding unit tests to verify correctness.

Example:

```
tests/
├── test_beam.py
├── test_fluids.py
├── test_geometry.py
└── test_units.py
```

Testing ensures formulas continue producing correct results as the project evolves.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Tokalxx/Custome_Calculator.git
```

Move into the project directory:

```bash
cd Custome_Calculator
```

(Optional) Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Development Workflow

1. Pull the latest changes.

```bash
git pull
```

2. Create a feature branch.

```bash
git checkout -b feature/new-formula
```

3. Implement your changes.

4. Run tests.

5. Commit your work.

```bash
git add .
git commit -m "Add beam deflection calculation"
```

6. Push your branch.

```bash
git push origin feature/new-formula
```

7. Open a Pull Request for review.

---

# Future Goals

* Comprehensive engineering formula library
* Automatic unit conversion
* Interactive command-line calculator
* Graphical desktop application
* REST API
* Web interface
* Engineering documentation website
* Full test coverage
* Continuous Integration (CI)

---

# Contributing

Contributions are welcome.

When contributing:

* Follow the existing project structure.
* Write clear and documented code.
* Include unit tests for new calculations.
* Keep formulas mathematically accurate.
* Document references where appropriate.

---

# License

This project is licensed under the terms of the LICENSE file included in this repository.
