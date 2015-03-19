/* Actualiza la tabla grupos con los nombre de departamentos*/

​INSERT INTO auth_group( name)
SELECT nombre FROM comun_departamento
