# Mejoras Realizadas

Este archivo documenta las dos mejoras principales que se implementaron en el sistema de cotización de ventanas.

## 1. Modularización de las Clases `Nave`, `Vidrio` y `Acabado`

- **Descripción**: Se crearon tres nuevas clases para gestionar las naves de las ventanas, los tipos de vidrio y los acabados de aluminio de manera independiente. Estas clases están en los archivos `nave.py`, `vidrio.py` y `acabado.py`.
- **Motivación**: Inicialmente, todo el cálculo de naves, vidrio y acabados se hacía dentro de la clase `Ventana`, lo cual complicaba el mantenimiento y hacía el código menos flexible.
- **Beneficio**:
  - Aumenta la modularidad y separación de responsabilidades.
  - Facilita la extensión futura del sistema si se añaden más tipos de vidrio o acabados.
  - Simplifica la clase `Ventana`, delegando responsabilidades a las clases correspondientes.

## 2. Implementación del Patrón Singleton en `Cotización`

- **Descripción**: Se aplicó el patrón de diseño Singleton en la clase `Cotización` para garantizar que solo exista una única instancia activa de cotización durante la ejecución del programa.
- **Motivación**: Se detectó la necesidad de evitar la creación de múltiples instancias de `Cotización`, lo que podía provocar inconsistencias en los datos. Con el patrón Singleton, solo se permite una instancia activa.
- **Beneficio**:
  - Controla el acceso y la creación de cotizaciones, evitando la duplicación de instancias.
  - Asegura una única fuente de verdad dentro de la aplicación, facilitando la gestión de datos y reduciendo posibles errores.
