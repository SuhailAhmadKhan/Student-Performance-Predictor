import sys
from src.logger import logging  # Import the 'logging' module from the 'src.logger' package

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get information about the exception
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extract the filename where the error occurred
    # Create a formatted error message with file name, line number, and error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message  # Return the formatted error message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the constructor of the parent class (Exception) with the error message
        # Create a detailed error message using the 'error_message_detail' function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message  # Return the detailed error message when the exception is converted to a string


# The purpose of this code is to  create a custom exception class ('CustomException') with additional details
# about the error, including the filename, line number, and the original error message.
