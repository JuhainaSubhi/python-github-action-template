# If you need Python 3 and the GitHub CLI, then use:
# FROM cicirello/pyaction:4

# If all you need is Python 3, use:
# FROM cicirello/pyaction-lite:3

# If Python 3 + git is sufficient, then use:
# FROM cicirello/pyaction:3


# =========================
FROM python:3.8-slim
# Set the working directory inside the container
WORKDIR /action
# Copy the entrypoint script into the container
COPY entrypoint.py .
# Run the script when the container starts
ENTRYPOINT ["python", "/action/entrypoint.py"]


# =========================

# To pull from the GitHub Container Registry instead, use one of these:
# FROM ghcr.io/cicirello/pyaction-lite:3
# FROM ghcr.io/cicirello/pyaction:4
# FROM ghcr.io/cicirello/pyaction:3

# COPY entrypoint.py /entrypoint.py
# ENTRYPOINT ["/entrypoint.py"]
