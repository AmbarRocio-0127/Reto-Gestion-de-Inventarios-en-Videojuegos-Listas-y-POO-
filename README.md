# 🎮 Gestión de Inventarios en Videojuegos (Listas + POO)

Práctica integrada en Python que simula el inventario de un jugador de videojuegos, combinando **listas** y **Programación Orientada a Objetos (POO)**. El programa se ejecuta desde la consola mediante un **menú interactivo** que permite consultar, mejorar, ampliar y filtrar los objetos de la mochila.

---

## 📁 Estructura del proyecto

```
├── clases/
│   └── Item.py      # Clase Item (molde de los objetos del juego)
└── main.py          # Programa principal con el menú interactivo
```

- **`clases/Item.py`**: define la clase `Item`, que representa cada objeto del inventario con un nombre, un tipo (Arma, Poción o Escudo) y un valor de poder.
- **`main.py`**: contiene la mochila inicial del jugador, las funciones de cada opción del menú y el ciclo principal del programa.

---

## 🎒 Inventario inicial

La mochila es una lista de objetos `Item` que comienza con tres elementos:

| Ítem | Tipo | Poder |
|------|------|-------|
| Daga de Plata | Arma | 45 |
| Poción de Vida | Poción | 50 |
| Escudo de Acero | Escudo | 20 |

---

## 🕹️ Menú principal

Al ejecutar el programa se muestra el siguiente menú, que se repite hasta que el usuario decide salir:

| Opción | Acción | Descripción |
|:------:|--------|-------------|
| **1** | Mostrar equipamiento de Arsenal | Muestra la cantidad de ítems en la mochila, el artículo equipado (el primero de la lista) y su daño base. |
| **2** | Modificando Arsenal | Mejora el objeto equipado aumentando su poder en 15 puntos. |
| **3** | Insertar un Arsenal extra | Agrega un nuevo objeto (una *Espada de Acero*, tipo Arma) a la mochila mediante `append()`. |
| **4** | Arsenal Disponible | Recorre toda la mochila con un ciclo `for`, muestra los datos de cada ítem y, si es un **Arma**, imprime el mensaje *¡LISTA PARA LUCHAR!*. |
| **5** | Salir | Finaliza el programa. |

Si el usuario ingresa un número fuera del rango, el programa muestra un mensaje de **opción inválida** y vuelve a mostrar el menú.

---

## 🧠 Conceptos aplicados

- **Clases y objetos**: la clase `Item` como molde de los objetos del juego.
- **Listas de objetos**: la mochila almacena instancias de `Item`, no textos ni números.
- **Acceso y modificación de atributos** con el operador punto (`.`).
- **Método `append()`** para agregar nuevos objetos a la lista.
- **Ciclo `for`** para recorrer el inventario.
- **Condicionales** para filtrar los ítems según su tipo.
- **Funciones** para organizar cada acción del programa.
- **Ciclo `while` y estructura `match`** para construir el menú interactivo.
- **Módulos**: separación de la clase en la carpeta `clases/` e importación en `main.py`.

---

## ▶️ Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/AmbarRocio-0127/Reto-Gestion-de-Inventarios-en-Videojuegos-Listas-y-POO-.git
   ```
2. Entra a la carpeta del proyecto:
   ```bash
   cd Reto-Gestion-de-Inventarios-en-Videojuegos-Listas-y-POO-
   ```
3. Ejecuta el programa (requiere **Python 3.10 o superior**, por el uso de `match`):
   ```bash
   python main.py
   ```

---

## 🎯 Objetivo de aprendizaje

Reforzar el manejo de listas, clases y ciclos en Python aplicando condiciones sobre los atributos de los objetos, en un contexto cercano al mundo de los videojuegos y organizado en un menú de consola.
