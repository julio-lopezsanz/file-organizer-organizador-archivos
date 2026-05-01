# File Organizer (Python)

A Python-based utility to automatically organize local files into categorized folders by extension. Designed for efficiency and clean workspace management.

## Purpose
I built this project to automate the process of organizing directories (like the Downloads folder). This is a **learning project** focused on mastering Python fundamentals and file system automation.

## Features
- **Automatic Sorting:** Groups files into categories like `Images`, `Documents`, and `Media`.
- **Safety Checks:** Verifies directory existence before moving files.
- **Extensible:** Easy to add new file extensions and categories.
- Real-time monitoring using Watchdog.
- Automatic handling of naming conflicts (file_1, file_2...).
- Pre-cleaning of existing files on startup.
- Cross-platform compatibility (Path.home).

## How it works
The script scans a target directory and moves files into subfolders based on their extension:
- `.jpg, .png, .gif` -> **Images**
- `.pdf, .docx, .txt` -> **Documents**
- `.mp3, .wav, .aac` -> **Audio**
- `.mp4, .avi, .mkv` -> **Video**
- `.zip, .rar, .7z` -> **Archives**

## Technologies Used
* **Python 3.6 or higher**
* **Pathlib Module** (best option and more modern than the OS module)
* **Shutil Module** (for high-level file operations)
* **Watchdog Library** (monitor file system events in real time)

## Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/julio-lopezsanz/file-organizer.git
   ```
2. **Install dependencies:**
   ```bash 
   pip install watchdog
   ```
3. **Run the script:**
   ```bash 
   python main.py
   ```

## Learning Journey
**By building this project, I am practicing:**
- Using Python's standard library for real-world tasks.
- Managing code versions with Git and GitHub.
- Documentation best practices for developers.

Created with 💻 by [**Julio Cesar Lopez Sanchez**](https://github.com/julio-lopezsanz)

------------------

# Organizador de Archivos (Python)

Una utilidad basada en Python para organizar automáticamente archivos locales en carpetas categorizadas por extensión. Diseñado para la eficiencia y la gestión limpia del espacio de trabajo.

## Propósito

Construí este proyecto para automatizar el proceso de organización de directorios (como la carpeta de Descargas). Este es un **proyecto de aprendizaje** enfocado en dominar los fundamentos de Python y la automatización del sistema de archivos.

## Características

- **Clasificación Automática**: Agrupa archivos en categorías como `Imágenes`, `Documentos` y `Multimedia`.
- **Controles de Seguridad**: Verifica la existencia del directorio antes de mover los archivos.
- **Extensible**: Es fácil añadir nuevas extensiones de archivo y categorías.
- Monitoreo en tiempo real utilizando Watchdog.
- Manejo automático de conflictos de nombres (archivo_1, archivo_2...).
- Limpieza previa de archivos existentes al iniciar.
- Compatibilidad multiplataforma (Path.home).

## Cómo funciona
El script escanea un directorio objetivo y mueve los archivos a subcarpetas según su extensión:

`.jpg, .png, .gif` -> **Imágenes**
`.pdf, .docx, .txt` -> **Documentos**
`.mp3, .wav, .aac` -> **Audio**
`.mp4, .avi, .mkv` -> **Video**
`.zip, .rar, .7z` -> **Archivos Comprimidos**

## Tecnologías Utilizadas

* **Python 3.6 o superior**
* **Módulo Pathlib** (la mejor opción y más moderna que el módulo OS)
* **Módulo Shutil** (para operaciones de archivos de alto nivel)
* **Librería Watchdog** (monitoreo de eventos del sistema de archivos en tiempo real)

## Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/julio-lopezsanz/file-organizer.git
   ```
2. **Instalar dependencias:**
   ```bash 
   pip install watchdog
   ```
3. **Ejecutar el script:**
   ```bash 
   python main.py
   ```

## Ruta de Aprendizaje

**Al construir este proyecto, estoy practicando:**
- El uso de la librería estándar de Python para tareas del mundo real.
- La gestión de versiones de código con Git y GitHub.
- Buenas prácticas de documentación para desarrolladores.

Creado con 💻 por [**Julio Cesar Lopez Sanchez**](https://github.com/julio-lopezsanz)