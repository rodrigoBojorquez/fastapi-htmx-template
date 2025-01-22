# Plantilla de Clean Architecture y DI en Python

## Contenidos
- [Plantilla de Clean Architecture y DI en Python](#plantilla-de-clean-architecture-y-di-en-python)
  - [Contenidos](#contenidos)
  - [Requisitos](#requisitos)
  - [Demo](#demo)
  - [Motivación](#motivación)
  - [Conceptos](#conceptos)
  - [Curiosidades](#curiosidades)

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
He pasado los últimos meses leyendo y aprendiendo sobre patrones de diseño y de arquitectura para crear aplicaciones robustas y escalables, y me he percatado que en el ecosistema de Python no es algo de lo que se hable a menudo (y menos en la comunidad hispana!), ya que normalmente me he topado que la gente y sobre todo las personas que estan empezando en el mundo de la programación utilizan python como un lenguaje de scripting para realizar pequeñas automatizaciones.

Es por eso que me he dado a la tarea de intentar replicar en un proyecto de Python los conceptos de arquitectura y patrones de diseño que más me gustan personalmente a la hora de querer crear una aplicación robusta y con la que me sienta comodo de trabajar en ella.

Pero antes me gustaría compartir algunas definiciones de los conceptos que utilicé en esta pequeña demo.

---

## Conceptos
- **Clean Architecture**:  
  Un estilo de arquitectura que promueve la separación de responsabilidades mediante capas bien definidas, asegurando que la lógica de negocio no dependa de detalles externos como frameworks o bases de datos.

- **Arquitecturas basadas en capas**:  
  Dividen una aplicación en capas (como presentación, aplicación, dominio e infrastructura) para organizar el código de manera lógica y promover la mantenibilidad.

- **Inyección de dependencias**:  
  Es un patrón de diseño que consiste en proporcionar las dependencias (objetos que una clase necesita) desde fuera, en lugar de crearlas dentro de la propia clase. Esto facilita la prueba y el mantenimiento del código.

- **Inversión de dependencias**:  
  Principio de diseño que establece que los módulos de alto nivel no deben depender de los módulos de bajo nivel, sino de abstracciones. Este principio es fundamental en la **Clean Architecture**.

---

## Curiosidades
Para esta demo he decidido aventurarme a utilizar la filosofía **HATEOAS** para crear una aplicación que se comunique utilizando uno de los pilares de la web, el hipertexto, esto contrasta con la ampliamente utilizada aplicación SPA que observamos en todos  lados (como React, Angular o Vue).
Para lograrlo, utilicé la librería [HTMX](https://htmx.org/), que permite transformar HTML en una experiencia moderna y fluida sin necesidad de escribir cientos de lineas de javascript. Si quieres aprender más sobre HTMX, te recomiendo revisar su [documentación oficial](https://htmx.org/).

---

Espero que este proyecto te sea útil, si tienes dudas o sugerencias, no dudes en abrir un _issue_ o contribuir al repositorio.