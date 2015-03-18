ALTER TABLE documentos_expediente ADD COLUMN consolidacion boolean;
ALTER TABLE documentos_expediente ALTER COLUMN consolidacion SET DEFAULT false;


UPDATE documentos_expediente
SET consolidacion=true
 WHERE cuerpo = 'cons';