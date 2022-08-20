class CredentialsNotFoundError(Exception):
    def __init__(self, error, message="Credentials not found."):
        self.error = error
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n{self.error}"
