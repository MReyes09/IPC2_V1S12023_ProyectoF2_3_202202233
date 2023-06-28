
class Sala:

    def __init__(self, numero: str, asientos: int):
        self._numero = numero
        self._asientos = asientos

    def get_numero(self) -> str:
        return self._numero

    def set_numero(self, numero: str) -> None:
        self._numero = numero

    def get_asientos(self) -> int:
        return self._asientos

    def set_asientos(self, asientos: int) -> None:
        self._asientos = asientos