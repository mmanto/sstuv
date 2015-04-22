/* Se crea la tabla de partidos */

CREATE TABLE comun_partido
(
  id serial NOT NULL,
  codigo integer NOT NULL,
  nombre character varying(200) NOT NULL,
  codcas character varying(20) NOT NULL,
  CONSTRAINT comun_partido_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE comun_partido
  OWNER TO postgres;



/* Se crea la tabla de departamentos */
CREATE TABLE comun_departamento
(
  id serial NOT NULL,
  codigo integer NOT NULL,
  nombre character varying(200) NOT NULL,
  CONSTRAINT comun_departamento_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE comun_departamento
  OWNER TO postgres;



/* Se crea la tabla de barrios */

CREATE TABLE comun_barrio
(
  codigo integer,
  nombre character(200)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE comun_barrio
  OWNER TO postgres;




