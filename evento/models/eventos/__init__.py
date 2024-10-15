event_titles = [
    # Festa
    "Festa Junina Tradicional", "Carnaval de Rua Carioca", "Festa de Iemanjá Salvador", "Festa do Peão de Barretos", "Festa do Boi no Nordeste",
    "Festa do Vinho de Bento Gonçalves", "Festa Nacional da Cachaça", "Festival de Forró Pé de Serra", "Festa de São João de Campina Grande", "Festa do Divino Espírito Santo",
    "Festa do Carimbó", "Festival de Quadrilhas Juninas", "Festa do Maracatu", "Festa do Cavalo Crioulo", "Festa do Fandango",
    "Festa do Pirão", "Festa do Milho Verde", "Festa do Camarão", "Festa do Morango", "Festa do Churrasco Gaúcho",

    # Show
    "Show da Virada São Paulo", "Show de Verão no Guarujá", "Show do Rock In Rio", "Show de MPB na Praia", "Show de Samba na Lapa",
    "Show de Axé em Salvador", "Show de Forró Pé de Serra", "Show de Sertanejo Universitário", "Show de Bossa Nova", "Show de Jazz ao Ar Livre",
    "Show Tributo à Tropicália", "Show de Rock Nacional", "Show de Funk Carioca", "Show de Frevo Recife", "Show de Música Sertaneja",
    "Show de Chorinho na Praça", "Show de Música Indie", "Show de Música Clássica", "Show Acústico no Teatro", "Show de Reggae em São Luís",

    # Cultura
    "Festival de Cultura Popular", "Semana do Folclore Brasileiro", "Mostra de Cultura Indígena", "Festa das Culturas Negras", "Festival Quilombola",
    "Encontro de Culturas Tradicionais", "Festival de Capoeira", "Festival de Boi-Bumbá", "Festival de Cultura Nordestina", "Encontro de Violeiros",
    "Semana da Consciência Negra", "Festival da Diversidade Cultural", "Festa da Cultura Caiçara", "Festival de Cultura Sertaneja", "Feira de Cultura Brasileira",
    "Festival de Roda de Samba", "Semana da Cultura de Salvador", "Festival de Cultura Gaúcha", "Festival de Danças Regionais", "Festival de Maracatu Rural",

    # Cinema
    "Mostra de Cinema Brasileiro", "Festival Internacional de Cinema do Rio", "Semana de Cinema Pernambucano", "Festival de Curtas de São Paulo", "Mostra de Cinema Indígena",
    "Mostra de Cinema de Animação", "Festival de Filmes Independentes", "Festival de Cinema Ambiental", "Semana de Cinema Nordestino", "Festival de Cinema Infantil",
    "Mostra de Cinema Experimental", "Semana de Cinema Latino-Americano", "Mostra de Cinema Documentário", "Festival de Cinema Feminino", "Mostra de Cinema LGBTQIA+",
    "Mostra de Filmes Clássicos", "Mostra de Cinema Gaúcho", "Festival de Filmes de Horror", "Festival de Cinema de Aventura", "Mostra de Cinema de Arte",

    # Educação
    "Seminário de Educação Inclusiva", "Congresso Nacional de Educação", "Fórum de Educação Infantil", "Feira de Inovação Educacional", "Congresso de Pedagogia Moderna",
    "Semana de Alfabetização Digital", "Fórum de Tecnologia na Educação", "Simpósio de Educação Pública", "Conferência Nacional de Docentes", "Seminário de Educação de Jovens e Adultos",
    "Feira de Educação Profissional", "Congresso de Gestão Escolar", "Semana de Estudos Pedagógicos", "Fórum de Educação à Distância", "Simpósio de Educação Bilíngue",
    "Congresso de Psicopedagogia", "Fórum de Formação de Professores", "Seminário de Educação Inclusiva", "Congresso de Metodologias Ativas", "Semana de Desenvolvimento Educacional",

    # Esporte
    "Maratona do Rio de Janeiro", "Copa do Mundo de Futebol de Praia", "Corrida de São Silvestre", "Campeonato Brasileiro de Skate", "Copa de Jiu-Jitsu",
    "Campeonato Nacional de Vôlei de Praia", "Torneio Internacional de Judô", "Copa Sul-Americana de Futebol", "Festival de Kitesurf em Fortaleza", "Campeonato Brasileiro de Surf",
    "Torneio de Natação Paralímpica", "Campeonato Brasileiro de Basquete", "Copa do Mundo de Futsal", "Corrida da Independência", "Copa do Brasil de Ciclismo",
    "Torneio de Tênis do Brasil Open", "Campeonato de Futebol de Areia", "Copa Nacional de Rugby", "Torneio de Ginástica Artística", "Festival de Capoeira e Esportes Tradicionais",

    # Negócios
    "Fórum de Empreendedorismo", "Conferência de Startups", "Feira de Franquias e Negócios", "Congresso Nacional de Marketing", "Seminário de Negócios Internacionais",
    "Congresso de Comércio Exterior", "Feira de Empreendedorismo Social", "Congresso de Gestão Empresarial", "Simpósio de Liderança Empresarial", "Feira Nacional de E-commerce",
    "Fórum de Economia Criativa", "Semana de Inovação Empresarial", "Fórum de Negócios Sustentáveis", "Congresso Nacional de Logística", "Seminário de Investimentos Imobiliários",
    "Feira de Novos Negócios", "Congresso de Transformação Digital", "Feira de Empreendedores Jovens", "Semana de Networking Profissional", "Congresso de Consultoria Empresarial",

    # Tecnologia
    "Fórum de Inovação Tecnológica", "Congresso de Inteligência Artificial", "Feira Nacional de Tecnologia", "Semana de Robótica e Automação", "Congresso de Blockchain e Criptomoedas",
    "Feira de Startups de Tecnologia", "Conferência de Segurança Cibernética", "Congresso de Desenvolvimento de Software", "Semana de Inovação em TI", "Simpósio de Tecnologias Disruptivas",
    "Congresso de Realidade Virtual e Aumentada", "Fórum de Transformação Digital", "Feira de Tecnologia da Informação", "Semana de IoT (Internet das Coisas)", "Congresso de Desenvolvimento Web",
    "Simpósio de Computação em Nuvem", "Feira de Games e Entretenimento Digital", "Congresso Nacional de Engenharia de Software", "Fórum de Ciência de Dados", "Feira de Robótica Educacional",

    # Saúde
    "Congresso Brasileiro de Saúde Pública", "Feira de Inovações em Saúde", "Semana de Saúde Preventiva", "Fórum de Saúde e Bem-Estar", "Simpósio de Enfermagem",
    "Congresso Nacional de Fisioterapia", "Feira de Medicina Alternativa", "Congresso de Nutrição e Alimentação Saudável", "Seminário de Saúde Mental", "Fórum de Doenças Crônicas",
    "Congresso de Odontologia", "Semana de Prevenção ao Câncer", "Seminário de Saúde da Mulher", "Congresso de Cardiologia", "Feira de Produtos Naturais e Orgânicos",
    "Fórum de Tecnologia em Saúde", "Congresso de Terapias Holísticas", "Semana de Saúde e Bem-Estar", "Seminário de Fisioterapia Desportiva", "Congresso de Medicina Integrativa",

    # Moda
    "Semana de Moda de São Paulo", "Feira Nacional de Moda Sustentável", "Desfile de Moda Brasileira", "Congresso de Moda Inclusiva", "Feira de Têxteis e Confecção",
    "Semana de Moda Praia", "Encontro Nacional de Estilistas", "Feira de Moda e Beleza", "Semana de Design de Moda", "Mostra de Moda Afro-Brasileira",
    "Feira de Novos Estilistas", "Semana de Moda Vintage", "Feira de Tecidos e Acessórios", "Congresso de Criação de Moda", "Semana de Moda Infantil",
    "Encontro de Modelos e Estilistas", "Feira de Moda e Sustentabilidade", "Congresso de Moda e Tecnologia", "Semana de Estilo e Tendências", "Feira de Moda e Estilo Urbano",

    # Gastronomia
    "Festival Gastronômico de Tiradentes", "Semana da Culinária Brasileira", "Feira de Sabores do Brasil", "Festival de Comida Nordestina", "Festival de Comida de Rua",
    "Encontro de Chefs Brasileiros", "Feira de Vinhos e Gastronomia", "Festival de Pizza e Massa", "Feira de Cervejas Artesanais", "Festival de Queijos e Vinhos",
    "Semana do Café e Gastronomia", "Feira de Chocolate e Doces", "Festival de Gastronomia Caipira", "Encontro de Culinária Vegana", "Feira de Comidas Típicas Brasileiras",
    "Festival de Gastronomia Regional", "Feira de Gastronomia Orgânica", "Festival de Comida Internacional", "Semana de Sabores Tropicais", "Festival de Gastronomia e Música",

    # Arte
    "Bienal de Arte de São Paulo", "Semana de Arte Contemporânea", "Mostra de Arte Popular Brasileira", "Exposição de Arte Moderna", "Festival de Arte e Tecnologia",
    "Feira Nacional de Artes Plásticas", "Mostra de Arte Indígena", "Exposição de Arte de Rua", "Festival de Graffiti e Arte Urbana", "Mostra de Arte Digital",
    "Semana de Arte Fotográfica", "Feira de Arte e Design", "Mostra de Arte e Sustentabilidade", "Festival de Arte Contemporânea Brasileira", "Exposição de Arte Erótica",
    "Feira de Arte Popular", "Festival de Arte Regional", "Exposição de Arte Visual", "Mostra de Artes Visuais Inclusivas", "Festival de Pintura ao Ar Livre",

    # Dança
    "Festival de Dança de Joinville", "Mostra de Danças Folclóricas", "Semana de Dança Contemporânea", "Encontro Nacional de Ballet Clássico", "Festival de Dança Urbana",
    "Semana de Dança do Ventre", "Festival de Dança Popular Brasileira", "Mostra de Dança Moderna", "Encontro Nacional de Danças de Salão", "Festival de Dança Afro-Brasileira",
    "Mostra de Dança Experimental", "Festival de Dança e Música", "Encontro Nacional de Dançarinos", "Semana de Dança Flamenca", "Mostra de Dança e Performance",
    "Festival de Dança e Circo", "Semana de Dança Internacional", "Encontro de Grupos de Dança", "Mostra de Dança Contemporânea Brasileira", "Festival de Danças Tradicionais",

    # Teatro
    "Festival de Teatro de Curitiba", "Mostra de Teatro Experimental", "Semana de Teatro Popular", "Encontro Nacional de Companhias Teatrais", "Festival de Teatro de Bonecos",
    "Semana de Teatro Infantil", "Mostra de Teatro Independente", "Festival de Teatro de Rua", "Encontro de Diretores Teatrais", "Semana de Teatro Contemporâneo",
    "Mostra de Teatro de Improviso", "Festival de Monólogos Teatrais", "Semana de Comédia Teatral", "Encontro de Ator e Cena", "Festival de Teatro de Formas Animadas",
    "Mostra de Teatro de Animação", "Festival de Teatro Musical", "Semana de Teatro e Performance", "Encontro de Teatro e Literatura", "Festival de Teatro e Circo",

    # Literatura
    "Bienal do Livro de São Paulo", "Semana de Literatura Brasileira", "Feira Nacional de Escritores", "Mostra de Literatura Infantil", "Encontro de Poetas Brasileiros",
    "Festival de Literatura de Cordel", "Semana de Literatura Independente", "Feira de Livros e Quadrinhos", "Encontro de Contadores de Histórias", "Mostra de Literatura Feminina",
    "Festival de Literatura Fantástica", "Encontro de Escritores Contemporâneos", "Semana de Literatura e Poesia", "Mostra de Literatura Regional", "Festival de Literatura e Artes",
    "Encontro de Jovens Escritores", "Feira Nacional de Livros e Arte", "Semana de Literatura e Cinema", "Mostra de Literatura e Música", "Festival de Literatura LGBTQIA+",

    # Outro
    "Feira de Sustentabilidade e Meio Ambiente", "Encontro Nacional de Jardineiros", "Festival de Gastronomia Vegana", "Semana de Fotografia e Arte Visual", "Feira de Orgânicos e Produtos Naturais",
    "Festival de Cinema ao Ar Livre", "Semana da Arquitetura Moderna", "Encontro de Cultura e Arte de Rua", "Feira Nacional de Inovação", "Festival de Arte Inclusiva",
    "Semana de Design Brasileiro", "Feira de Artesanato Tradicional", "Mostra de Filmes Independentes", "Semana de Cultura Popular", "Encontro Nacional de Ecoturismo",
    "Feira de Ciências e Tecnologia", "Semana de Música Instrumental", "Festival de Animação Digital", "Encontro Nacional de Circo e Teatro", "Feira de Economia Criativa"
]