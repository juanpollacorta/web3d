import matplotlib.pyplot as plt

# Datos de los procesadores mencionados
procesadores = [
    "Ryzen 5 5600G", 
    "Ryzen 7 5700G", 
    "Ryzen 9 7900X", 
    "Ryzen 9 7950X"
]

# Potencia estimada en función del número de núcleos de cada procesador
# Para simplificar, asignamos una "potencia" basada en el número de núcleos
potencia = [6, 8, 12, 16]  # Número de núcleos de cada procesador

# Creación de la gráfica
plt.figure(figsize=(10, 6))
plt.bar(procesadores, potencia, color='skyblue')

# Añadiendo detalles
plt.title('Potencia Estimada de Procesadores Ryzen para Diferentes Tareas')
plt.xlabel('Procesador')
plt.ylabel('Número de Núcleos (Potencia Estimada)')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Mostrar gráfica
plt.tight_layout()
plt.show()
