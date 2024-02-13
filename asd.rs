<ID> identificadores: CANT, PRECIO, TOTAL, IVA, 100, etc.
<OP_ARIT> operadores aritméticos: +, -, *, /, ^
<OP_ASIG> operadores de asignación: =
<GRP> agrupadores paréntesis: (, )
<SELECT> palabra reservada: SELECT


<SELECT> → SELECT <EXP> FROM <ID>
<EXP> → <ID> <OP_ASIG> <TERM> | <TERM>
<TERM> → <TERM> <OP_ARIT> <FACTOR> | <FACTOR>
<FACTOR> → <GRP> <EXP> <GRP> | <ID> | <ID> <OP_ARIT> <ID>
<OP_ARIT> → + | - | * | / | ^
<OP_ASIG> → =
<GRP> → ( | )
<ID> → identificador