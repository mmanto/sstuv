

/* Se crea la columna organismo*/
ALTER TABLE documentos_expediente ADD COLUMN organismo integer;
ALTER TABLE documentos_expediente ALTER COLUMN organismo SET NOT NULL;
ALTER TABLE documentos_expediente ALTER COLUMN organismo SET DEFAULT 0;

/* Se crea la columna consolidación */
ALTER TABLE documentos_expediente ADD COLUMN consolidacion boolean;
ALTER TABLE documentos_expediente ALTER COLUMN consolidacion SET DEFAULT false;


/*Se popula la comuna organismo*/
ALTER TABLE documentos_expediente ALTER COLUMN organismo TYPE integer USING (trim(caracteristica)::integer);


/* Se popula la columna consolidación*/
UPDATE documentos_expediente
SET consolidacion=true
 WHERE cuerpo = 'cons';



