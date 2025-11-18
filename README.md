# Math Shape Calculator

A simple calculator for computing geometric shapes: area, perimeter, volume, etc.

* **Usage**

  * 2-D shapes
  * 3-D solids
* **Project Structure**
* **Contributing**
* **Future Enhancements**
* **License**
* **Acknowledgements**

---

## Overview

The Math Shape Calculator is a tool designed to help users easily compute common geometric properties of shapes — for example area and perimeter of 2-D figures, or surface area and volume of 3-D solids.
It aims to be simple to use and intuitive, making it ideal for educational use, quick calculations, or as a base for further development.

---

## Features

* Calculate **perimeter** and **area** for 2-dimensional shapes.
* Calculate **surface area** and **volume** for 3-dimensional solids.
* Simple user interface / command line (whichever your implementation uses).
* Extensible: easy to add new shapes or formulas in future.

---

## Getting Started

### Prerequisites

* Python 3


### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nareeco/Math-Shape-Calculator.git  
   ```
2. Change into the project directory:

   ```bash
   cd Math-Shape-Calculator  
   ```

### Running the Calculator

Run the program via the appropriate command. For example:

```bash
python mathshapecalc.py 
```

Follow the on-screen prompts to select a shape, enter dimensions, and get results.

---

## Usage

### 2-D Shapes

Examples of shapes you can compute:

* **Square** — input side length → compute area and perimeter
* **Rectangle** — input length and width → area, perimeter
* **Circle** — input radius → area (πr²) and circumference (2πr)
* **Triangle** (optional) — base & height → area, perhaps sides → perimeter

### 3-D Solids

Examples of solids:

* **Cube** — side length → surface area (6s²), volume (s³)
* **Sphere** — radius → surface area (4πr²), volume (4/3πr³)
* **Rectangular prism**, **cylinder**, etc (if implemented)

---

## Future Enhancements

Here are some ideas for improvements:

* Add support for more shapes (e.g., parallelogram, trapezoid, ellipsoid)
* Add unit conversion (e.g., cm → m)
* Add GUI/web interface (for web-based version)
* Add more robust input validation (e.g., negative values, non-numbers)
* Add more detailed documentation and examples
* Add theme or dark mode if GUI
* Implement logging or history of calculations
