/*Eliminar expediente duplicados

Se considera duplicado si la clave conformada por organismo. número, anio, alcance existe mas de una vez.
En caso caso de encontrar duplicados elimina aquellos expedientes duplicados que no posean pases.
*/ 

DELETE FROM documentos_expediente as expediente
USING  (Select repe.id  from documentos_pase as pase RIGHT JOIN (
		Select id from 
			(Select id from documentos_expediente as exp RIGHT JOIN( 
				SELECT organismo, numero, anio, alcance, count(*)
				FROM documentos_expediente
				GROUP BY organismo, numero, anio, alcance
				HAVING count(*) > 1
				) AS repetidos ON (exp.organismo = repetidos.organismo AND exp.anio= repetidos.anio AND exp.numero = repetidos.numero AND exp.alcance = repetidos.alcance)
			)
			AS rep LEFT JOIN documentos_expedienteley ON (rep.id = documentos_expedienteley.expediente_ptr_id) 
			where documentos_expedienteley.expediente_ptr_id IS NULL
	) AS repe ON (pase.expediente_id = repe.id)
	WHERE (pase.id IS NULL)) AS del
	WHERE (expediente.id = del.id);






/*Eliminar expediente ley duplicados

Se considera duplicado si la clave conformada por organismo. número, anio, alcance existe mas de una vez.
En caso caso de encontrar duplicados elimina aquellos expedientes duplicados que no posean pases.
*/ 

Begin transaction;
CREATE TEMP TABLE del ON COMMIT DROP AS
       Select repe.id  from documentos_pase as pase RIGHT JOIN (
		Select id from 
			(Select id from documentos_expediente as exp RIGHT JOIN( 
				SELECT organismo, numero, anio, alcance, count(*)
				FROM documentos_expediente
				GROUP BY organismo, numero, anio, alcance
				HAVING count(*) > 1
				) AS repetidos ON (exp.organismo = repetidos.organismo AND exp.anio= repetidos.anio AND exp.numero = repetidos.numero AND exp.alcance=repetidos.alcance)
			)
			AS rep LEFT JOIN documentos_expedienteley ON (rep.id = documentos_expedienteley.expediente_ptr_id) 
			where documentos_expedienteley.expediente_ptr_id IS NOT NULL
	) AS repe ON (pase.expediente_id = repe.id)
	WHERE (pase.id IS NULL);
Select * from del;        
DELETE FROM documentos_expedienteley as expediente
USING  del
WHERE (expediente.expediente_ptr_id = del.id);
DELETE FROM documentos_expediente as expediente
USING  del
	WHERE (expediente.id = del.id);
commit;
