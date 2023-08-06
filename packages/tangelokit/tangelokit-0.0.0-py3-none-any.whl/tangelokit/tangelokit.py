from tangelokit.schema_validation import credit_line_validator


class GenerateDataStructure:
    def __init__(self,
                 credit_lines: list = None,
                 disbursements: list = None,
                 products: list = None,
                 clients: list = None
                 ) -> dict:

        self.credit_lines = credit_lines
        self.disbursements = disbursements
        self.products = products
        self.clients = clients

        self.error_messages = {}
        if self.credit_lines:
            self.errors = credit_line_validator(self.credit_lines)
            if self.errors:
                self.error_messages["credit_line_erros"] = self.errors

    def build_information(self):
        return {"Suceeesss": len(self.credit_lines)}
