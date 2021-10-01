#Aquí Mon me recomienda meter todas las validaciones que no sean estandares, las que yo me cree, y utilizarlas importandolas.
import datetime
from wtforms import ValidationError

class Validators():
    def validate_fecha(self, campo): #Cuando ejecutas el formulario.validate en views, además de ejecutar los validadores de arriba, tambien ejecuta los "validate_xxx" que crees, reconoce el nombre validate.
        hoy = datetime.date.today()
        if campo.data > hoy:
            raise ValidationError("La fecha no puede ser futuro")