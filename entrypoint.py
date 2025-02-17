import sys
import os

if __name__ == "__main__":
    # Get the inputs passed as command line arguments
    input1 = sys.argv[1]
    input2 = sys.argv[2]

    # Concatenate the inputs as strings
    result = input1 + input2

    # Output the result as a GitHub Action output
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            print(f"concatenated-result={result}", file=f)

    print(f"The concatenated result of '{input1}' and '{input2}' is: {result}")
# Check if the pipeline pushes the docker image  to dockerhub 2