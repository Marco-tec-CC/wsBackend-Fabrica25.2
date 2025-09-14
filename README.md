📺 Projeto Django - Animes Favoritos (com API Jikan)

Este projeto é uma aplicação Django que consome a API Jikan
 para buscar informações sobre animes, permitindo que o usuário:

🔎 Pesquise animes na API.

⭐ Adicione animes aos favoritos.

🗑 Remova favoritos.

✏ Edite informações de um favorito (como a categoria).

🏷 Organize animes por categorias personalizadas.

⚙️ Tecnologias utilizadas

Python 3.11+

Django 5+

SQLite3 (banco de dados padrão do Django)

Jikan API (API gratuita de animes)

HTML + Django Templates

📂 Estrutura principal do projeto
projeto_principal/
│── projeto/               # Configuração principal do Django
│── app/                   # Aplicação com lógica do sistema
│   │── migrations/        # Migrações do banco
│   │── templates/         # Templates HTML
│   │   ├── anime_base.html
│   │   ├── favoritos.html
│   │   ├── edit_favorito.html
│   │── models.py          # Modelos (Anime, Categoria)
│   │── views.py           # Regras de negócio
│   │── urls.py            # Rotas da aplicação
│   │── forms.py           # Formulários
│── db.sqlite3             # Banco de dados local
│── manage.py              # Comando de gerenciamento do Django
│── requirements.txt       # Dependências

📑 Funcionalidades
🔎 Pesquisa de Animes

O usuário digita o nome do anime na barra de pesquisa.

A aplicação consulta a API Jikan (https://api.jikan.moe/v4/anime?q=nome).

Mostra uma lista de animes com título, imagem e descrição.

⭐ Favoritar Anime

Cada anime listado possui um botão "Adicionar aos Favoritos".

O usuário pode escolher uma categoria (ou deixar "Sem categoria").

O anime é salvo no banco de dados.

📂 Categorias

O usuário pode criar categorias (ex: "Shounen", "Romance", "Comédia").

Ao favoritar, pode selecionar a categoria.

Na página de favoritos, aparece o título, imagem, descrição e a categoria.

✏ Edição de Favorito

O usuário pode editar um favorito, alterando a categoria.

🗑 Remoção de Favorito

O usuário pode remover qualquer anime salvo nos favoritos.

📸 Telas principais
Página inicial (Pesquisa de Animes)

Barra de pesquisa

Resultados com botão de favoritar e selecionar categoria

Favoritos

Lista com todos os favoritos

Mostrar categoria de cada anime

Botões de editar/remover

Editar Favorito

Formulário para trocar categoria

Admin Django

Gerenciar Categorias e Animes Favoritos diretamente no painel
