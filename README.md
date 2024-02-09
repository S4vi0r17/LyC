# LyC

SQL es un lenguaje de programación que te permite trabajar con bases de datos relacionales, es decir, que almacenan información en forma de tablas con filas y columnas. Con SQL puedes crear, modificar y eliminar tablas y datos, así como hacer consultas para obtener información de una o varias tablas. También puedes usar funciones, operadores y cláusulas para manipular y calcular los datos, y crear vistas, índices y procedimientos almacenados para optimizar y automatizar tu trabajo con las bases de datos.

# SQL: Lenguaje de consulta estructurado

## ¿Qué es SQL y para qué sirve?

- SQL significa **Structured Query Language** (Lenguaje de consulta estructurado).
- SQL se utiliza para **comunicarse con una base de datos** y SQL es el lenguaje estándar para los sistemas de gestión de bases de datos relacionales.
- Las sentencias SQL se utilizan para realizar tareas como **actualizar datos o recuperar datos** de una base de datos.

## ¿Cómo crear, modificar y eliminar tablas y datos?

- Para crear una tabla se usa la sentencia **CREATE TABLE**, seguida del nombre de la tabla y los nombres y tipos de datos de las columnas. Por ejemplo:

```sql
CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE,
  telefono VARCHAR(15)
);
```

- Para insertar datos en una tabla se usa la sentencia **INSERT INTO**, seguida del nombre de la tabla y los valores a insertar. Por ejemplo:

```sql
INSERT INTO clientes (id, nombre, email, telefono) VALUES
(1, 'Ana', 'ana@gmail.com', '123456789'),
(2, 'Luis', 'luis@hotmail.com', '987654321'),
(3, 'Pedro', 'pedro@yahoo.com', NULL);
```

- Para modificar datos en una tabla se usa la sentencia **UPDATE**, seguida del nombre de la tabla, la columna a modificar y el nuevo valor, y opcionalmente una condición para filtrar los datos a modificar. Por ejemplo:

```sql
UPDATE clientes SET email = 'ana@outlook.com' WHERE id = 1;
```

- Para eliminar datos de una tabla se usa la sentencia **DELETE FROM**, seguida del nombre de la tabla y opcionalmente una condición para filtrar los datos a eliminar. Por ejemplo:

```sql
DELETE FROM clientes WHERE nombre = 'Pedro';
```

- Para eliminar una tabla se usa la sentencia **DROP TABLE**, seguida del nombre de la tabla. Por ejemplo:

```sql
DROP TABLE clientes;
```

## ¿Cómo hacer consultas simples y complejas?

- Para hacer consultas a una tabla se usa la sentencia **SELECT**, seguida de las columnas que se quieren mostrar y el nombre de la tabla. Por ejemplo:

```sql
SELECT nombre, email FROM clientes;
```

- Para filtrar los datos que se quieren mostrar se usa la cláusula **WHERE**, seguida de una condición que debe cumplir los datos. Por ejemplo:

```sql
SELECT nombre, email FROM clientes WHERE telefono IS NOT NULL;
```

- Para ordenar los datos que se quieren mostrar se usa la cláusula **ORDER BY**, seguida de la columna por la que se quiere ordenar y opcionalmente la dirección (ASC o DESC). Por ejemplo:

```sql
SELECT nombre, email FROM clientes ORDER BY nombre ASC;
```

- Para limitar el número de datos que se quieren mostrar se usa la cláusula **LIMIT**, seguida de un número que indica la cantidad máxima de filas a mostrar. Por ejemplo:

```sql
SELECT nombre, email FROM clientes LIMIT 10;
```

- Para hacer consultas a varias tablas se usa la cláusula **JOIN**, seguida del nombre de la otra tabla y la condición que relaciona las tablas. Por ejemplo:

```sql
SELECT clientes.nombre, pedidos.fecha, pedidos.total FROM clientes JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

- Para hacer consultas más avanzadas se pueden usar funciones, operadores y cláusulas adicionales, como **GROUP BY**, **HAVING**, **CASE**, **IN**, **LIKE**, etc. Por ejemplo:

```sql
SELECT clientes.nombre, COUNT(pedidos.id) AS num_pedidos, SUM(pedidos.total) AS total_pedidos FROM clientes JOIN pedidos ON clientes.id = pedidos.cliente_id GROUP BY clientes.id HAVING total_pedidos > 1000;
```

## ¿Cómo usar funciones, operadores y cláusulas?

- SQL tiene muchas funciones integradas que se pueden usar para manipular y calcular los datos. Algunas de las funciones más comunes son:

  - **Funciones de cadena**: CONCAT, LENGTH, SUBSTRING, UPPER, LOWER, etc.
  - **Funciones numéricas**: ABS, ROUND, CEIL, FLOOR, MOD, etc.
  - **Funciones de fecha y hora**: CURDATE, CURTIME, NOW, DATE, TIME, DATEDIFF, etc.
  - **Funciones de agregación**: COUNT, SUM, AVG, MIN, MAX, etc.

- SQL también tiene muchos operadores que se pueden usar para comparar, combinar y operar los datos. Algunos de los operadores más comunes son:

  - **Operadores aritméticos**: +, -, *, /, %
  - **Operadores de comparación**: =, <>, >, <, >=, <=
  - **Operadores lógicos**: AND, OR, NOT
  - **Operadores de conjuntos**: UNION, INTERSECT, EXCEPT

- SQL también tiene muchas cláusulas que se pueden usar para especificar condiciones, agrupaciones, ordenamientos, etc. Algunas de las cláusulas más comunes son:

  - **WHERE**: para filtrar los datos según una condición
  - **ORDER BY**: para ordenar los datos según una columna
  - **GROUP BY**: para agrupar los datos según una columna
  - **HAVING**: para filtrar los datos agrupados según una condición
  - **LIMIT**: para limitar el número de datos a mostrar
  - **JOIN**: para unir dos o más tablas según una condición
  - **CASE**: para crear expresiones condicionales
  - **IN**: para verificar si un valor está dentro de un conjunto de valores
  - **LIKE**: para verificar si un valor coincide con un patrón

## ¿Cómo unir, agrupar y ordenar datos?

- Para unir dos o más tablas se usa la cláusula **JOIN**, seguida del nombre de la otra tabla y la condición que relaciona las tablas. Existen diferentes tipos de JOIN, según cómo se quieran combinar las tablas:

  - **INNER JOIN**: devuelve las filas que coinciden en ambas tablas
  - **LEFT JOIN**: devuelve todas las filas de la tabla izquierda y las filas que coinciden de la tabla derecha
  - **RIGHT JOIN**: devuelve todas las filas de la tabla derecha y las filas que coinciden de la tabla izquierda
  - **FULL JOIN**: devuelve todas las filas de ambas tablas, coincidan o no
  - **CROSS JOIN**: devuelve el producto cartesiano de ambas tablas, es decir, todas las combinaciones posibles de filas

- Para agrupar los datos según una o más columnas se usa la cláusula **GROUP BY**, seguida de las columnas por las que se quiere agrupar. Esto permite aplicar funciones de agregación a los datos agrupados, como COUNT, SUM, AVG, etc. Por ejemplo:

```sql
SELECT categoria, COUNT(producto) AS num_productos, AVG(precio) AS precio_promedio FROM productos GROUP BY categoria;
```

- Para ordenar los datos según una o más columnas se usa la cláusula **ORDER BY**, seguida de las columnas por las que se quiere ordenar y opcionalmente la dirección (ASC o DESC). Por ejemplo:

```sql
SELECT producto, precio, categoria FROM productos ORDER BY precio DESC, categoria ASC;
```

## ¿Cómo crear vistas, índices y procedimientos almacenados?

- Una vista es una tabla virtual que se crea a partir de una consulta SQL. Las vistas se pueden usar para simplificar consultas complejas, restringir el acceso a ciertos datos o mejorar el rendimiento de las consultas. Para crear una vista se usa la sentencia **CREATE VIEW**, seguida del nombre de la vista y la consulta SQL que define la vista. Por ejemplo:

```sql
CREATE VIEW productos_caros AS
SELECT producto, precio, categoria FROM productos WHERE precio > 100;
```

- Un índice es una estructura de datos que mejora la velocidad de las operaciones en una tabla. Los índices se pueden crear sobre una o más columnas de una tabla, y permiten encontrar rápidamente los datos sin tener que recorrer toda la tabla. Para crear un índice se usa la sentencia **CREATE INDEX**, seguida del nombre del índice y la columna o columnas sobre las que se crea el índice. Por ejemplo:

```sql
CREATE INDEX idx_categoria ON productos (categoria);
```

- Un procedimiento almacenado es un conjunto de sentencias SQL que se guardan en la base de datos y se pueden ejecutar como una sola unidad. Los procedimientos almacenados se pueden usar para automatizar tareas repetitivas, mejorar la seguridad y el rendimiento, y pasar parámetros a las consultas. Para crear un procedimiento almacenado se usa la sentencia **CREATE PROCEDURE**, seguida del nombre del procedimiento, los parámetros opcionales y el cuerpo del procedimiento. Por ejemplo:

```sql
CREATE PROCEDURE obtener_productos_por_categoria (IN cat VARCHAR(50))
BEGIN
  SELECT producto, precio FROM productos WHERE categoria = cat;
END;
```