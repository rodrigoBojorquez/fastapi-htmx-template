# Plantilla de Clean Architecture y DI en Python

## Contenidos
1. [Requisitos](#requisitos)
2. [Demo](#demo)
3. [Motivación](#motivación)
4. [Conceptos](#conceptos)
5. [Curiosidades](#curiosidades)

---

## Requisitos
- **Python** 3.12
- **Node.js**

---

## Demo
Sigue estos pasos para descargar y ejecutar la demo de esta plantilla:

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/rodrigoBojorquez/python-clean-architecture.git
   ```
2. Entra a la carpeta del proyecto:  
   ```bash
   cd python-clean-architecture
   ```
3. Instala `pipenv` (te recomiendo instalarlo globalmente si no lo tienes):  
   ```bash
   pip install pipenv
   ```
4. Instala las dependencias del proyecto con `pipenv`:  
   ```bash
   pipenv install
   ```
5. Activa el entorno virtual:  
   ```bash
   pipenv shell
   ```
6. Inicia el servidor web:  
   ```bash
   fastapi dev presentation
   ```
7. En una nueva pestaña de la consola, instala las dependencias de Node.js:  
   ```bash
   npm install
   ```
8. Inicia el servidor de desarrollo para compilar **TailwindCSS**:  
   ```bash
   npm run dev
   ```
9. Abre tu navegador e ingresa a la dirección: [http://localhost:8000](http://localhost:8000).

---

## Motivación
Durante los últimos meses, he dedicado tiempo a aprender sobre patrones de diseño y arquitectura que permiten crear aplicaciones robustas y escalables. En el ecosistema de Python, especialmente en la comunidad hispana, no es común encontrar recursos sobre este tema. 

Python es frecuentemente utilizado como lenguaje de scripting para automatizaciones, pero quise llevarlo más allá replicando conceptos de arquitectura y patrones de diseño que, en mi experiencia, hacen más cómodo y eficiente trabajar en aplicaciones complejas. 

Esta plantilla es el resultado de ese esfuerzo, y espero que sirva como una guía para quienes deseen explorar estos conceptos.

---

## Conceptos
A continuación, se describen los principales conceptos utilizados en esta demo:

- **Clean Architecture**:  
  Un estilo de arquitectura que promueve la separación de responsabilidades mediante capas bien definidas, asegurando que la lógica de negocio no dependa de detalles externos como frameworks o bases de datos.

- **Arquitecturas basadas en capas**:  
  Dividen una aplicación en capas (como presentación, aplicación, dominio y datos) para organizar el código de manera lógica y promover la mantenibilidad.

- **Inyección de dependencias**:  
  Es un patrón de diseño que consiste en proporcionar las dependencias (objetos que una clase necesita) desde fuera, en lugar de crearlas dentro de la propia clase. Esto facilita la prueba y el mantenimiento del código.

- **Inversión de dependencias**:  
  Principio de diseño que establece que los módulos de alto nivel no deben depender de los módulos de bajo nivel, sino de abstracciones. Este principio es fundamental en la **Clean Architecture**.

---

## Curiosidades
En esta demo, me aventuré a utilizar la filosofía **HATEOAS** para crear un servidor que se comunique utilizando hipertexto, uno de los pilares fundamentales de la web. Esto contrasta con el enfoque tradicional de aplicaciones SPA (como React, Angular o Vue).

Para lograrlo, utilicé la librería [HTMX](https://htmx.org/), que permite transformar HTML en una experiencia moderna y fluida sin necesidad de un framework pesado. Si quieres aprender más sobre HTMX, te recomiendo revisar su [documentación oficial](https://htmx.org/).

---

Espero que este proyecto te sea útil, si tienes dudas o sugerencias, no dudes en abrir un _issue_ o contribuir al repositorio.