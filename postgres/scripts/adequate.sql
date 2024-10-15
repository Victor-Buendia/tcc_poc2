CREATE OR REPLACE TABLE pessoas AS (
    SELECT DISTINCT
        CAST(cartao as JSON) AS cartao,
        * EXCLUDE(cartao)
    FROM pessoas
);