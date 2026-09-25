import os

var_name = "TEST_VAR"  # change to whatever variable you want to check
print(os.environ.get(var_name) is not None)