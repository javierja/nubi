# Nubi Encuestas

Dado el siguiente listado de features solicitadas por el Product Owner (PO):

- Quiero tener una API que me permita crear encuestas.
- Quiero poder responder cada encuesta muchas veces.
- Quiero poder acceder a un listado de todas las encuestas y sus respuestas.

el equipo de desarrollo realizó un MVP de la API en Python utilizando Flask. Ahora necesitamos hacer un refactor para poder encarar una nueva etapa de desarrollo y trabajar sobre bases más sólidas.

Por esto, te pedimos que revises el código y nos entregues:

- Una lista priorizada con los puntos débiles que hayas encontrado, justificando por qué son un problema y proponiendo una mejora para cada uno
- La implementación de los puntos más críticos que hayas encontrado (al menos 3)

No hace falta analizar la parte de infraestructura, poné el foco en el código Python.

Para ayudarte, el equipo de desarrollo preparó algunos ejemplos de uso de la API:

`curl http://localhost:5000`

`curl http://localhost:5000/addPoll --request GET --header "Content-Type: application/json" --data '{"question": "¿Te gusta Python?"}'`

`curl http://localhost:5000/addAnswer --request GET --header "Content-Type: application/json" --data '{"poll_id": "5fc9129482d4589e8d7d687e", "answer": "Me encanta Python"}'`

`curl http://localhost:5000/getPolls`

Las propuestas que hagas pueden ser de cualquier tipo, siempre que sean coherentes entre sí.

Podés preguntar cualquier duda que tengas respecto a los requerimientos del PO.

La solución del ejercicio deberás subirla a un repositorio privado, darnos acceso compartirnos el link.

El commit original tendrá que ser con los archivos tal cual te los damos.

Cada propuesta que elijas implementar deberá ser desarrollada en un commit independiente.

La documentación de la solución (problemas encontrados y justificaciones) también deberá estar en el mismo repo. Podés usar el formato que prefieras, mientras más detallado mejor.
