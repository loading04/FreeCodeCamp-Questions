# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

print(add_time("12:30 PM", "00:30", "MonDaY"))
# 01:00 AM

# Run unit tests automatically
main(module='test_module', exit=False)
