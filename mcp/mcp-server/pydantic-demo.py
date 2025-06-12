from pydantic import BaseModel, ValidationError

class MyIntModel(BaseModel):
    value: int

def parse_large_number():
    large_number = 1e25

    print(f"Attempting to validate {large_number} as an integer...")

    try:
        MyIntModel(value=large_number)
        print("\nValidation succeeded!")
    except ValidationError as e:
        print("\nValidation failed!")
        print(e)

def parse_number():
    number = 1e5

    print(f"Attempting to validate {number} as an integer...")

    try:
        MyIntModel(value=number)
        print("\nValidation succeeded!")
    except ValidationError as e:
        print("\nValidation failed!")
        print(e)

parse_large_number()
parse_number()
