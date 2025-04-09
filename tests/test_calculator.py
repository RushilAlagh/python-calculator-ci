import pytest
from calculator import add, subtract, multiply, divide

class TestCalculator:
    """Test suite for the calculator functions"""
    
    def test_add(self):
        """Test addition function with various inputs"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(2.5, 3.5) == 6.0
        
    def test_subtract(self):
        """Test subtraction function"""
        assert subtract(5, 2) == 3
        assert subtract(10, 10) == 0
        assert subtract(-5, -3) == -2
        
    def test_multiply(self):
        """Test multiplication function"""
        assert multiply(3, 4) == 12
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6
        
    def test_divide(self):
        """Test division function with valid inputs"""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(5, 2) == 2.5
        
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)