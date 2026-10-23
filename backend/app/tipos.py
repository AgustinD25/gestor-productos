from typing import Annotated

from pydantic import StringConstraints

# Código con formato AAA-00 (por ejemplo MUE-01), compartido por varios módulos.
CodigoStr = Annotated[str, StringConstraints(pattern=r"^[A-Z]{3}-\d{2}$")]
