Los analisadores lexicos son una parte fundamental de esta disciplina, ya que se encargan de reconocer los componentes léxicos o tokens de un código fuente¹.

Para hacer tu proyecto final, necesitas tener claro los siguientes conceptos:

- **Alfabeto**: es el conjunto de símbolos que se pueden usar en el código fuente, como letras, dígitos, signos de puntuación, etc.
- **Cadena**: es una secuencia finita de símbolos del alfabeto, como palabras, números, identificadores, etc.
- **Lenguaje**: es un conjunto de cadenas que cumplen ciertas reglas o patrones, como las palabras reservadas, los operadores, los literales, etc.
- **Expresión regular**: es una forma de definir un lenguaje mediante símbolos especiales que indican la repetición, la alternancia, la concatenación, etc. de cadenas o subcadenas.
- **Autómata finito**: es una máquina abstracta que tiene un número finito de estados y puede cambiar de estado al leer un símbolo del alfabeto. Se usa para reconocer si una cadena pertenece o no a un lenguaje.
- **Tabla de símbolos**: es una estructura de datos que almacena la información de los tokens que se van reconociendo, como su tipo, su valor, su posición, etc.

El objetivo de tu proyecto es diseñar e implementar un analizador léxico que pueda reconocer los tokens de un lenguaje de programación simple, como el siguiente:

```
programa ejemplo;
var x, y: entero;
inicio
  leer(x);
  leer(y);
  si x > y entonces
    escribir(x);
  sino
    escribir(y);
  fin_si;
fin.
```

Para ello, debes seguir los siguientes pasos:

1. Definir el alfabeto y el lenguaje de tu código fuente, especificando los tipos de tokens que existen y sus patrones correspondientes. Por ejemplo, puedes usar expresiones regulares para definir los tokens, como:

    - `programa|var|inicio|fin|si|entonces|sino|fin_si` para las palabras reservadas.
    - `[a-zA-Z][a-zA-Z0-9]*` para los identificadores.
    - `[0-9]+` para los números enteros.
    - `;|,|:|\.|\(|\)|=|<|>|+|-|\*|/` para los signos de puntuación y los operadores.
    - `leer|escribir` para las funciones predefinidas.

2. Construir un autómata finito que pueda reconocer los tokens de tu lenguaje, usando las expresiones regulares como guía. Puedes usar un diagrama de estados y transiciones para representar el autómata, como el siguiente:

![Diagrama de autómata finito](^4^)

3. Implementar el analizador léxico en el lenguaje de programación de tu preferencia, usando una estructura de control que vaya leyendo los caracteres del código fuente y cambiando de estado según el autómata. También debes usar una tabla de símbolos para guardar la información de los tokens que se van reconociendo. Por ejemplo, puedes usar un pseudocódigo como el siguiente:

```
funcion analizar_lexico(codigo_fuente)
  estado <- 0
  token <- ""
  tabla_simbolos <- lista vacia
  para cada caracter en codigo_fuente
    segun estado
      caso 0: // estado inicial
        si caracter es espacio o salto de linea
          ignorar caracter
        sino si caracter es letra
          estado <- 1
          token <- token + caracter
        sino si caracter es digito
          estado <- 2
          token <- token + caracter
        sino si caracter es signo de puntuacion u operador
          estado <- 3
          token <- token + caracter
        sino
          reportar error de caracter invalido
      caso 1: // estado de identificador o palabra reservada
        si caracter es letra o digito
          token <- token + caracter
        sino
          retroceder una posicion en el codigo fuente
          si token es palabra reservada
            agregar (token, "palabra reservada") a tabla_simbolos
          sino
            agregar (token, "identificador") a tabla_simbolos
          estado <- 0
          token <- ""
      caso 2: // estado de numero entero
        si caracter es digito
          token <- token + caracter
        sino
          retroceder una posicion en el codigo fuente
          agregar (token, "numero entero") a tabla_simbolos
          estado <- 0
          token <- ""
      caso 3: // estado de signo de puntuacion u operador
        si caracter es signo de puntuacion u operador
          token <- token + caracter
        sino
          retroceder una posicion en el codigo fuente
          agregar (token, "signo u operador") a tabla_simbolos
          estado <- 0
          token <- ""
    fin segun
  fin para
  devolver tabla_simbolos
fin funcion
```

4. Probar el analizador léxico con diferentes ejemplos de código fuente y verificar que reconozca correctamente los tokens y los almacene en la tabla de símbolos. Por ejemplo, para el código fuente anterior, la tabla de símbolos resultante sería:

| Token | Tipo |
| ----- | ---- |
| programa | palabra reservada |
| ejemplo | identificador |
| ; | signo u operador |
| var | palabra reservada |
| x | identificador |
| , | signo u operador |
| y | identificador |
| : | signo u operador |
| entero | palabra reservada |
| ; | signo u operador |
| inicio | palabra reservada |
| leer | palabra reservada |
| ( | signo u operador |
| x | identificador |
| ) | signo u operador |
| ; | signo u operador |
| leer | palabra reservada |
| ( | signo u operador |
| y | identificador |
| ) | signo u operador |
| ; | signo u operador |
| si | palabra reservada |
| x | identificador |
| > | signo u operador |
| y | identificador |
| entonces | palabra reservada |
| escribir | palabra reservada |
| ( | signo u operador |
| x | identificador |
| ) | signo u operador |
| ; | signo u operador |
| sino | palabra reservada |
| escribir | palabra reservada |
| ( | signo u operador |
| y | identificador |
| ) | signo u operador |
| ; | signo u operador |
| fin_si | palabra reservada |
| ; | signo u operador |
| fin | palabra reservada |
| . | signo u operador |

*