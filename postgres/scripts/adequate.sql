CREATE OR REPLACE TABLE pessoas AS (
    SELECT DISTINCT
        CAST(masked_cartao as JSON) AS cartao,
        * EXCLUDE(masked_cartao)
    FROM pessoas
);