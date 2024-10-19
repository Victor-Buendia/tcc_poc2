ALTER TABLE inscricaos RENAME TO inscricoes;

ALTER TABLE empresas ADD CONSTRAINT id_empresa_pk PRIMARY KEY (id_empresa);
ALTER TABLE eventos ADD CONSTRAINT id_evento_pk PRIMARY KEY (id_evento);
ALTER TABLE pessoas ADD CONSTRAINT id_pessoa_pk PRIMARY KEY (id_pessoa);
ALTER TABLE inscricoes ADD CONSTRAINT id_inscricao_pk PRIMARY KEY (id_inscricao);

ALTER TABLE eventos ADD CONSTRAINT id_empresa__eventos_to_empresas_fk FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa);
ALTER TABLE inscricoes ADD CONSTRAINT id_evento__inscricoes_to_eventos_fk FOREIGN KEY (id_evento) REFERENCES eventos(id_evento);
ALTER TABLE inscricoes ADD CONSTRAINT id_pessoa__inscricoes_to_pessoas_fk FOREIGN KEY (id_pessoa) REFERENCES pessoas(id_pessoa);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO consumer;
-- REVOKE ALL PRIVILEGES ON TABLE pessoa FROM consumer;