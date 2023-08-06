Cave Utilities for the Cave App
==========
Basic utilities for the MIT Cave App. This package is intended to be used by the Cave App and the Cave API.

Setup
----------

Make sure you have Python 3.7.x (or higher) installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installation

```
pip install cave_utils
```

# Getting Started
## Example:
1. In your cave_app, update the following file:

    `cave_api/tests/test_init.py`
    ```
    from cave_api import execute_command
    from cave_utils.socket import Socket
    from cave_utils.validator import Validator


    init_session_data = execute_command(session_data={}, socket=Socket(), command="init")

    x = Validator(init_session_data)

    x.print_errors()
    # x.print_warnings()
    # x.write_warnings('./warnings.txt')
    # x.write_errors('./errors.txt')
    ```

2. Run the following command:
    `cave test test_init.py`
