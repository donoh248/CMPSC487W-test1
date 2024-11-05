# test_basic_gates.py
import pytest
from lg import ANDGate, ORGate, NOTGate, XORGate, NANDGate, NORGate

def test_and_gate_basic():
    gate = ANDGate("test_and")
    
    # Test all possible combinations
    test_cases = [
        (0, 0, 0),  # (input_a, input_b, expected_output)
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1)
    ]
    
    for input_a, input_b, expected in test_cases:
        gate.set_pins(input_a, input_b)
        assert gate.get_output() == expected

def test_or_gate_basic():
    gate = ORGate("test_or")
    
    test_cases = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ]
    
    for input_a, input_b, expected in test_cases:
        gate.set_pins(input_a, input_b)
        assert gate.get_output() == expected

def test_not_gate_basic():
    gate = NOTGate("test_not")
    
    test_cases = [
        (0, 1),  # (input, expected_output)
        (1, 0)
    ]
    
    for input_val, expected in test_cases:
        gate.set_pin(input_val)
        assert gate.get_output() == expected

def test_xor_gate_basic():
    gate = XORGate("test_xor")
    
    test_cases = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ]
    
    for input_a, input_b, expected in test_cases:
        gate.set_pins(input_a, input_b)
        assert gate.get_output() == expected

def test_nand_gate_basic():
    gate = NANDGate("test_nand")
    
    test_cases = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ]
    
    for input_a, input_b, expected in test_cases:
        gate.set_pins(input_a, input_b)
        assert gate.get_output() == expected

def test_nor_gate_basic():
    gate = NORGate("test_nor")
    
    test_cases = [
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 0)
    ]
    
    for input_a, input_b, expected in test_cases:
        gate.set_pins(input_a, input_b)
        assert gate.get_output() == expected

def test_gate_labels():
    """Test that gates properly store and return their labels"""
    gates = [
        (ANDGate, "test_and"),
        (ORGate, "test_or"),
        (NOTGate, "test_not"),
        (XORGate, "test_xor"),
        (NANDGate, "test_nand"),
        (NORGate, "test_nor")
    ]
    
    for gate_class, label in gates:
        gate = gate_class(label)
        assert gate.get_label() == label

def test_pin_setters():
    """Test individual pin setters for binary gates"""
    gate = ANDGate("test_pins")
    
    # Test setting pins individually
    gate.set_pin_a(1)
    gate.set_pin_b(0)
    assert gate.get_pin_a() == 1
    assert gate.get_pin_b() == 0
    assert gate.get_output() == 0
    
    # Test setting both pins at once
    gate.set_pins(1, 1)
    assert gate.get_pin_a() == 1
    assert gate.get_pin_b() == 1
    assert gate.get_output() == 1

def test_uninitialized_pins():
    """Test that gates properly handle uninitialized pins"""
    gate = ANDGate("test_uninit")
    
    # Attempting to get output with uninitialized pins should raise an assertion error
    with pytest.raises(AssertionError):
        gate.get_output()