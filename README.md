# NewNews API Flask
##### Cadastre autores, poste notícas e pesquise sobre algo.

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/MartinsMessias/NewNews-flask-api-mongodb)](https://github.com/MartinsMessias/NewNews-flask-api-mongodb)<space> <space>[![GitHub license](https://img.shields.io/github/license/MartinsMessias/NewNews-flask-api-mongodb)](https://github.com/MartinsMessias/NewNews-flask-api-mongodb/blob/master/LICENSE)<space> <space>[![GitHub forks](https://img.shields.io/github/forks/MartinsMessias/NewNews-flask-api-mongodb)](https://github.com/MartinsMessias/NewNews-flask-api-mongodb/)

</div>
---

## 📖 Sobre:

Uma api onde é possível cadastrar autores e notícias, também é possível realizar pesquisa por notícias.

--- 

## 🚀 Tecnologias Utilizadas:

- Python
- Flask
- MongoDB Atlas
- PyMongo

--- 

### Documentação básica
## Authors
```
Listar autores
GET /authors
```

```
Cadastrar autor
POST /authors

BODY raw

{
    "name":"Nome do autor"
}

```

```
Listar autor pelo id
GET /authors/<id>

```
```
Atualizar dados de autor
PUT /authors/<id>

BODY raw

{
    "name":"Nome do autor"
}
```
```
Remover autor
DELETE /authors/<id>
```
---------------------------------------------
## News
```
Listar notícias
GET /news
```
```
Cadastrar notícias
POST /news

BODY raw

{
    "title": "Título da notícia",
    "content": "Conteúdo da notícia",
    "author": "Autor"
}

/*Caso o autor não exista ele irá ser criado.*/

```
```
Listar notícia pelo id
GET /news/<id>

```
```
Atualizar dados de notícia
PUT /news/<id>

BODY raw

{
    "title": "Título da notícia",
    "content": "Conteúdo da notícia",
    "author": {"_id": "Id do autor"}
}
```
```
Remover notícia
DELETE /news/<id>
```
```
Pesquisar notícias
Traz notícias que contenham a query de busca no seu título, conteúdo ou nome do autor.

GET /search/<string>
```
