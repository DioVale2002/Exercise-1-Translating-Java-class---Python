# Dog Class - Object-Oriented Programming Exercise

## Overview
This project demonstrates object-oriented programming concepts by translating a Java class skeleton into Python. The `Dog` class encapsulates dog attributes and behaviors in a simple, easy-to-understand implementation.

## Objective
Practice object-oriented programming by implementing a Python class that:
- Stores and manages dog attributes
- Implements dog behaviors as methods
- Demonstrates encapsulation and method invocation

## Features
The `Dog` class includes the following functionality:

### Attributes
- **name** (str): The dog's name
- **age** (int): The dog's current age

### Methods
- **`__init__(name, age)`**: Constructor that initializes the dog with a name and age
- **`bark()`**: Makes the dog bark by printing "Woof! Woof!"
- **`celebateBirthday()`**: Increases the dog's age by 1 and prints a birthday message
- **`getInfo()`**: Displays the dog's name and current age

## Usage

### Creating a Dog Instance
```python
# Create a dog named "Max" who is 5 years old
my_dog = Dog("Max", 5)
```

### Using Dog Methods
```python
# Make the dog bark
my_dog.bark()  # Output: Woof! Woof!

# Celebrate the dog's birthday
my_dog.celebateBirthday()  # Output: Happy Birthday! Max is now 6 years old!

# Display dog information
my_dog.getInfo()  # Output: Dog Name: Max, Age: 6
```

## Example Output
```
Woof! Woof!
Happy Birthday! Doog is now 4 years old!
Dog Name: Doog, Age: 4
```

## Code Structure
```python
class Dog:
    def __init__(self, name, age):
        # Initialize dog attributes
        
    def bark(self):
        # Print barking sound
        
    def celebateBirthday(self):
        # Increment age and print birthday message
        
    def getInfo(self):
        # Display dog's information
```

## Learning Outcomes
By completing this exercise, you will understand:
- Class definition and instantiation in Python
- Constructor methods (`__init__`)
- Instance attributes (`self.name`, `self.age`)
- Instance methods and the `self` parameter
- Basic string formatting and concatenation
- Translating Java OOP concepts to Python

## Requirements
- Python 3.x

## Running the Code
1. Save the code in a file (e.g., `dog.py`)
2. Run the file using Python:
   ```bash
   python dog.py
   ```

## Future Enhancements
Potential improvements to extend this project:
- Add more attributes (breed, color, weight)
- Implement additional behaviors (sit, fetch, eat)
- Add input validation for age (must be non-negative)
- Create multiple dog instances and compare them
- Add a `__str__` method for cleaner object representation

## License
This is an educational project for learning object-oriented programming concepts.

---

**Note**: This project is based on translating a Java class skeleton into Python, demonstrating the similarities and differences between the two languages in implementing OOP principles.
