# app/main.py

from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente
from datetime import date
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from flask import Flask, render_template, request

app = Flask(__name__)
console = Console()

# Función de consola para mostrar el menú con Rich
def mostrar_menu():
    table = Table(title="Sistema de Cotización de Ventanas")
    table.add_column("Opción", style="cyan", no_wrap=True)
    table.add_column("Descripción", style="magenta")
    table.add_row("1", "Crear cotización (Interfaz de Texto)")
    table.add_row("2", "Ejecutar Interfaz Web")
    table.add_row("3", "Salir")
    console.print(table)

# Función para crear una cotización usando la interfaz de texto (Rich)
def crear_cotizacion_texto():
    console.print("[bold green]Ingrese los datos del cliente:[/bold green]")
    nombre_cliente = Prompt.ask("Nombre del cliente")
    empresa_cliente = Prompt.ask("Nombre de la empresa")
    direccion_cliente = Prompt.ask("Dirección del cliente")
    cliente = Cliente(nombre_cliente, empresa_cliente, direccion_cliente)

    cantidad_ventanas = int(Prompt.ask("Cantidad de ventanas", default="1"))
    ventanas = []

    for i in range(cantidad_ventanas):
        console.print(f"[bold green]Ventana {i + 1}[/bold green]")
        estilo = Prompt.ask("Estilo de la ventana (O, XO, OXXO, OXO)")
        ancho = float(Prompt.ask("Ancho de la ventana (cm)"))
        alto = float(Prompt.ask("Alto de la ventana (cm)"))
        acabado = Prompt.ask("Acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado)")
        tipo_vidrio = Prompt.ask("Tipo de vidrio (Transparente, Bronce, Azul)")
        esmerilado = Prompt.ask("Esmerilado (S/N)?").lower() == 's'

        ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)
        ventanas.append(ventana)
    
    cotizacion = Cotizacion.get_instance(cliente, ventanas, date.today())
    total = cotizacion.calcular_total()

    console.print(f"[bold]Nombre:[/bold] {nombre_cliente}")
    console.print(f"[bold]Empresa:[/bold] {empresa_cliente}")
    console.print(f"[bold]Dirección:[/bold] {direccion_cliente}")
    console.print(f"[bold]El costo total de la cotización es:[/bold] ${total:.2f}", style="bold cyan")

# Flask - Interfaz Web
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_cotizacion', methods=['GET', 'POST'])
def crear_cotizacion():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre_cliente']
        empresa_cliente = request.form['empresa_cliente']
        direccion_cliente = request.form['direccion_cliente']
        cliente = Cliente(nombre_cliente, empresa_cliente, direccion_cliente)

        cantidad_ventanas = int(request.form['cantidad_ventanas'])
        ventanas = []
        for i in range(cantidad_ventanas):
            estilo = request.form[f'estilo_{i}']
            ancho = float(request.form[f'ancho_{i}'])
            alto = float(request.form[f'alto_{i}'])
            acabado = request.form[f'acabado_{i}']
            tipo_vidrio = request.form[f'tipo_vidrio_{i}']
            esmerilado = request.form.get(f'esmerilado_{i}') == 'on'

            ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)
            ventanas.append(ventana)

        cotizacion = Cotizacion.get_instance(cliente, ventanas, date.today())
        total = cotizacion.calcular_total()

        return render_template('resultado.html', cliente=cliente, total=total, cantidad_ventanas=cantidad_ventanas)
    
    return render_template('crear_cotizacion.html')

# Iniciar la aplicación en modo consola o web
if __name__ == "__main__":
    mostrar_menu()
    opcion = Prompt.ask("Seleccione una opción", default="3")
    if opcion == '1':
        crear_cotizacion_texto()
    elif opcion == '2':
        console.print("Ejecutando interfaz web... Acceda a [bold cyan]http://127.0.0.1:5001[/bold cyan]", style="bold green")
        app.run(debug=True, port=5001)  # Ejecuta Flask para la interfaz web
    else:
        console.print("Saliendo del sistema...", style="bold red")
