#!/usr/bin/env -S python3 -B

# NOTE: If you are using an alpine docker image
# such as pyaction-lite, the -S option above won't
# work. The above line works fine on other linux distributions
# such as debian, etc, so the above line will work fine
# if you use pyaction:4.0.0 or higher as your base docker image.

import sys
import os



def safe_float_conversion(value):
    """Try to convert the input to a float, return None if invalid."""
    try:
        return float(value)
    except ValueError:
        print(f"Error: '{value}' is not a valid number.")
        return None

if __name__ == "__main__" :
    # Get the inputs passed as command line arguments
    input1 = sys.argv[1]
    input2 = sys.argv[2]

    # Attempt to convert inputs to float
    num1 = safe_float_conversion(input1)
    num2 = safe_float_conversion(input2)

    # If either conversion fails, exit the script
    if num1 is None or num2 is None:
        sys.exit(1)  # Exit with error code 1 to indicate failure

    # Fake example outputs
    output1 = "Hello"
    output2 = "World"

    # This is how you produce workflow outputs.
    # Make sure corresponds to output variable names in action.yml
    if "GITHUB_OUTPUT" in os.environ :
        with open(os.environ["GITHUB_OUTPUT"], "a") as f :
            #print("{0}={1}".format("output-one", output1), file=f)
            #print("{0}={1}".format("output-two", output2), file=f)
	        print(f"sum={result}", file=f)

    print(f"The sum of {input1} and {input2} is: {result}")

# =======This is a change for testing the pipeline
# =======This is a second change for testing the pipeline

