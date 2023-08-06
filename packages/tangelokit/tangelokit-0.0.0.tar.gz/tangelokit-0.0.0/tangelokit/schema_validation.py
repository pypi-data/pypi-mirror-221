import jsonschema


def credit_line_validator(credit_lines):
    credit_lines_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "key1": {"type": "string"},
                "key2": {"type": "number"},
                "key3": {"type": "boolean"}
            },
            "required": ["key1", "key2", "key3"]
        }
    }
    validator = jsonschema.Draft7Validator(credit_lines_schema)
    errors = []
    for error in validator.iter_errors(credit_lines):
        errors.append(error.message)

    return errors
