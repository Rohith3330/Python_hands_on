def admit_student(max_capacity=10):
  """
  A function that checks if admitting a student will exceed the maximum capacity.
  Uses closure to remember the current number of admitted students.
  """
  admitted_count = 0

  def admit():
    """Inner function that admits a student and returns a message."""
    nonlocal admitted_count  # Modify admitted_count from the enclosing scope
    if admitted_count < max_capacity:
      admitted_count += 1
      return "Student admitted successfully!"
    else:
      return "Admission failed: Maximum capacity reached."

  return admit

# Create an instance of the admit function with the specific capacity
school_admit = admit_student()

# Simulate admitting students
print(school_admit())
print(school_admit())
print(school_admit())
print(school_admit())
print(school_admit())
print(school_admit())
print(school_admit())
print(school_admit())
print(school_admit())
print(school_admit())  
print(school_admit())  # Output: Admission failed: Maximum capacity reached.

# Note: You can call school_admit() multiple times to simulate admissions
