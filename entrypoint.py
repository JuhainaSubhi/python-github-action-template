#!/usr/bin/env -S python3 -B

# NOTE: If you are using an alpine docker image
# such as pyaction-lite, the -S option above won't
# work. The above line works fine on other linux distributions
# such as debian, etc, so the above line will work fine
# if you use pyaction:4.0.0 or higher as your base docker image.

import sys
import os

if __name__ == "__main__" :
    # Rename these variables to something meaningful
    input1 = float(sys.argv[1])
    input2 = float(sys.argv[2])
    # Attempt to convert inputs to float
    num1 = safe_float_conversion(input1)
    num2 = safe_float_conversion(input2)
    # Perform the addition
    result = input1 + input2


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

