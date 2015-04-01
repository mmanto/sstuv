
/* Se crea la columna estado para la tabla pase*/
ALTER TABLE documentos_pase ADD COLUMN estado character(50);

/* Se setea el default value en aceptado*/
ALTER TABLE documentos_pase ALTER COLUMN estado SET DEFAULT 'Aceptado'::bpchar;

/* Se agrega número al pase*/
ALTER TABLE documentos_pase ADD COLUMN numero integer;


