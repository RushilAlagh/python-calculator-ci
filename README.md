
# 🧮 Python Calculator with CI/CD


## 📜 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Testing](#-testing)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [Contact](#-contact)

## ✨ Features
- ➕ Addition, subtraction, multiplication, division
- 🚫 Division by zero protection
- ✅ Comprehensive unit testing
- ⚙️ GitHub Actions automation
- 📊 Code coverage tracking
- 🔄 Multi-Python version support (3.8+)

## 🛠️ Installation
```bash
# Clone repository
git clone https://github.com/your-username/python-calculator-ci.git
cd python-calculator-ci

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage
```python
from calculator import add, subtract, multiply, divide

print(add(5, 3))        # 8
print(divide(10, 2))    # 5.0
print(divide(5, 0))     # Raises ValueError
```

## 🧪 Testing
Run all tests:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest --cov=calculator --cov-report=term-missing
```

## ⚙️ CI/CD Pipeline
Automatically runs on:
- Every push to `main` branch
- Every pull request
- Tests against Python 3.8, 3.9, 3.10, 3.11
- Enforces 90%+ code coverage

View workflow: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

## 📁 Project Structure
```
.
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions config
├── calculator/
│   ├── __init__.py          # Package initialization
│   └── calculator.py        # Core logic
├── tests/
│   ├── __init__.py
│   └── test_calculator.py   # Unit tests
├── requirements.txt         # Dependencies
├── LICENSE
└── README.md                # This file
```

## 📚 API Reference
### `add(a: float, b: float) -> float`
Returns the sum of two numbers
```python
add(2.5, 3.5)  # 6.0
```

### `divide(a: float, b: float) -> float`
Returns a/b. Raises `ValueError` if b=0

## 🤝 Contributing
1. Fork the project
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/your-feature`)
5. Open a Pull Request


## 📧 Contact
Your Name - rushil.alagh@gmail.com  
Project Link: [https://github.com/RushilAlagh/python-calculator-ci.git](https://github.com/RushilAlagh/python-calculator-ci.git)

---
