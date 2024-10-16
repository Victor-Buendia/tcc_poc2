ATTACH '' AS psql (TYPE POSTGRES);
CREATE OR REPLACE TABLE psql.public.pessoas AS (
    SELECT
        id_pessoa,
        primeiro_nome,
        masked_cpf AS cpf,
        idade,
        genero,
        masked_telefone AS telefone,
        masked_email AS email
    FROM psql.public.pessoas
)