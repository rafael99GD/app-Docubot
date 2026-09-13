# Plan de la semana — Aprender + Preparar el escaparate de GitHub

## 1. Lo que te falta y hay que aprender ESTA semana (priorizado)

No intentes dominarlo todo — el objetivo es entender lo suficiente para no quedarte en blanco y para poder decir "lo he probado" con honestidad.

### Prioridad alta (dedícale más tiempo)

**FastAPI** (2-3h)
- Es el framework más parecido conceptualmente a lo que ya sabes de Spring Boot: rutas, modelos de datos con Pydantic (equivalente a tus DTOs/entidades), inyección de dependencias.
- Tutorial oficial, hazlo con las manos en el teclado, no solo leyendo: https://fastapi.tiangolo.com/tutorial/
- Lo vas a **usar directamente** en el proyecto de abajo, así que esto no es teoría suelta — lo vas a aplicar ya.

**Django** (1-2h, solo para hablar de ello con soltura)
- No hace falta que lo domines para la entrevista de esta semana; con FastAPI ya demuestras que entiendes el patrón. Pero mira por encima el concepto de Django REST Framework y el ORM de Django (`models.py`), porque es probable que te pregunten "¿sabes la diferencia entre Django y FastAPI?"
- Respuesta corta que te sirve: "Django es más 'todo incluido' — ORM, admin panel, autenticación de serie —, mientras que FastAPI es más ligero y está pensado para APIs, con validación de datos automática vía Pydantic y mejor rendimiento en async. Para microservicios pequeños yo iría a FastAPI; para una plataforma grande con mucha lógica CRUD, Django tiene sentido."
- Documentación: https://docs.djangoproject.com/en/stable/intro/tutorial01/

**PostgreSQL** (1h)
- Ya conoces MySQL y MongoDB, así que los conceptos los tienes. Lo único realmente distinto: tipos de datos específicos de Postgres (`JSONB`, `ARRAY`, `SERIAL`), y que es más estricto con los tipos que MySQL.
- No necesitas instalarlo a fondo; con Docker lo levantas en un contenedor en 2 minutos (te lo dejo listo en el proyecto de abajo).

### Prioridad media

**Git — merge vs rebase, pull requests** (30-45 min)
- Practica visual e interactiva: https://learngitbranching.js.org/?locale=es
- Ten clara la respuesta corta: "`merge` conserva el historial completo con un commit de fusión; `rebase` reescribe tu rama por encima de la otra dejando un historial lineal, pero hay que tener cuidado si ya has compartido esa rama con otros."

**SQL — JOIN y GROUP BY con soltura** (30 min de práctica)
- Practica activa: https://sqlzoo.net/ (módulos de SELECT within SELECT y JOIN)

### Prioridad "actitud", no técnica

**Agentes de IA (Claude Code, Codex)**
- No necesitas ser experto — el propio anuncio busca curiosidad, no dominio. Pero pruébalos de verdad esta semana, aunque sea 20 minutos, para poder hablar de primera mano y no de oídas.
- Documentación de Claude Code: https://docs.claude.com — puedes pedirle que te ayude a montar parte del proyecto de abajo, y así ya tienes una anécdota real: "until lo usé para acelerar la parte de..." en vez de una frase genérica.

---

## 2. Inventario de proyectos para enseñar (con qué decir de cada uno)

Organiza así tu GitHub / pestañas abiertas antes de la entrevista, para no andar buscando en el momento:

### Python
- **Buzz! Virtual Controller** — servidor WebSocket en Python + app Android (Kotlin) + cliente web, emulando mandos XInput para que PCSX2 los detecte como mandos reales. Habla de esto para demostrar que sabes de comunicación entre procesos/servicios, no solo scripts sueltos.
- **Descargador de Spotify** — app de escritorio con GUI estilo Spotify, usa `yt-dlp` para audio y añade metadatos embebidos. Bueno para mostrar manejo de librerías externas y procesos en segundo plano.
- **GameShelf** — tu proyecto más reciente y completo (Spring Boot + Angular), aunque no es Python, es tu mejor prueba de arquitectura backend limpia. Tenlo como comodín para cualquier pregunta de "explícame un proyecto tuyo a fondo".

### Sobre el bot de Telegram — ojo con esto
Tu experiencia con **bots de Telegram fue en NEORIS**, como parte del trabajo de la empresa — no es un repositorio tuyo que puedas enseñar en GitHub (es código de la empresa, no tuyo). Puedes **hablar** de esa experiencia en la entrevista sin problema, pero no la listes como "proyecto para enseñar" porque no tienes el repo. Por eso te propongo abajo construir uno propio esta semana — así pasas de "lo mencioné en una empresa" a "aquí tienes el código, funcionando, y lo hice yo".

### Android
- **Mi Dieta** — app de seguimiento de dieta en Kotlin/Jetpack Compose. Es tu primer proyecto Android — bueno para mostrar que no te quedas solo en lo que te enseñan, sino que exploras plataformas nuevas por curiosidad.
- El componente Android de **Buzz! Virtual Controller** también cuenta aquí, y refuerza que sabes conectar apps móviles con backends/servicios en tiempo real.

### Web / didáctico y divertido
- **CS2 Map Quiz** — app web con estética temática de CS2, desplegada en GitHub Pages con Git LFS. Bueno para el "toque personal/curioso" — muestra que construyes cosas por diversión, no solo por obligación.
- **Portfolio personal** — bilingüe ES/EN, sección de proyectos data-driven y modales de vídeo. Enséñalo al principio de la entrevista como resumen visual de todo lo demás.

### Cómo mencionar la IA en tus proyectos ya hechos
Si has usado IA (Claude, ChatGPT, Copilot...) para acelerar partes de GameShelf, el portfolio o cualquier otro proyecto, dilo abiertamente y con un ejemplo concreto — "la usé para depurar el error de zone.js en Angular" es mil veces mejor que una frase genérica tipo "uso IA para programar". Cuanto más específico el ejemplo, más creíble.

---

## 3. El proyecto nuevo de esta semana: DocuBot

La idea: un bot de Telegram que recibe un documento, lo resume con IA, y guarda el histórico en PostgreSQL. No es casualidad — **mirra exactamente lo que hace MTGlobal** ("extractores de documentos, asistentes para eventos"), así que en la entrevista puedes decir literalmente: *"antes de venir, monté una versión pequeña de algo parecido a lo que hacéis vosotros, para entender el problema desde dentro"*. Es el mejor gancho posible para esta entrevista en concreto.

**Qué hace:**
1. Le mandas un PDF o un .txt al bot de Telegram.
2. El bot lo descarga, extrae el texto.
3. Se lo pasa a Claude (API de Anthropic) pidiendo un resumen + puntos clave.
4. Te responde por Telegram con el resumen.
5. Guarda cada interacción en PostgreSQL (quién, qué documento, qué resumen) — así también demuestras que sabes combinar API externa + IA + persistencia, las tres piezas del puesto.

**Stack**: Python + FastAPI (webhook de Telegram) + PostgreSQL (vía Docker) + API de Claude.

Te lo dejo montado y funcional a continuación — solo te faltará añadir tu propio token de Telegram y tu API key de Anthropic para probarlo de verdad.
