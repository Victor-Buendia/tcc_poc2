CREATE OR REPLACE TABLE empresas AS (
    SELECT DISTINCT
        ROW_NUMBER() OVER() AS id_empresa,
        * EXCLUDE(id_empresa)
    FROM empresas
);

CREATE OR REPLACE TABLE eventos AS (
    SELECT DISTINCT
        ROW_NUMBER() OVER() AS id_evento,
        * EXCLUDE(id_evento)
    FROM eventos
);

CREATE OR REPLACE TABLE pessoas AS (
    SELECT DISTINCT
        ROW_NUMBER() OVER() AS id_pessoa,
        * EXCLUDE(id_pessoa)
    FROM pessoas
);

CREATE OR REPLACE TABLE inscricaos AS (
    SELECT DISTINCT
        ROW_NUMBER() OVER() AS id_inscricao,
        * EXCLUDE(id_inscricao)
    FROM inscricaos
);