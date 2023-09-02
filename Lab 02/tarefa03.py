import redis

client_redis = redis.Redis(
  host='host',
  port=11614,
  password='password')

############ Exercícios 1 e 2: criar modelos de dados no Redis para artigos e tags 
# (utilizando HASH para artigos e SET para tags), populando ambos com dados
# e relacionando-os.

tags = ["Tag1", "Tag2", "Tag3"]

for tag in tags:
  client_redis.sadd("tags:set", tag)

tags_no_conjunto = client_redis.smembers("tags:set")
print("Tags no conjunto:", tags_no_conjunto)

# Artigo 1
article_key1 = "article:1"  
article_data1 = {
  "name": "Artigo 1",
  "description": "Descrição do Artigo 1",
  "filename": "artigo1.txt",
  "postingdate": "2023-09-01",
}

# Artigo 2
article_key2 = "article:2"  
article_data2 = {
  "name": "Artigo 2",
  "description": "Descrição do Artigo 2",
  "filename": "artigo2.txt",
  "postingdate": "2022-09-01",
}

for field, value in article_data1.items():
  client_redis.hset(article_key1, field, value)

tagkey1 = "article:1:tags"
tags_associadas1 = ["Tag1", "Tag2"]
for tag in tags_associadas1:
  client_redis.sadd(tagkey1, tag)

for field, value in article_data2.items():
  client_redis.hset(article_key2, field, value)

tagkey2 = "article:2:tags"
tags_associadas2 = ["Tag3"]
for tag in tags_associadas2:
  client_redis.sadd(tagkey2, tag)


############ Exercícios 3 e 4

chaves_artigos = client_redis.keys("article:*")

for chave in chaves_artigos:
  if client_redis.type(chave) == b'hash':  # Verifica se a chave é um hash
    article_data = client_redis.hgetall(chave)

    print("Informações do Artigo:")
    print(f"Chave: {chave}")
    print(f"Nome: {article_data.get(b'name', b'N/A').decode('utf-8')}")
    print(f"Descrição: {article_data.get(b'description', b'N/A').decode('utf-8')}")
    print(f"Arquivo: {article_data.get(b'filename', b'N/A').decode('utf-8')}")
    print(f"Data de Publicação: {article_data.get(b'postingdate', b'N/A').decode('utf-8')}")

    tags_associadas = client_redis.smembers(f"{chave}:tags")
    tags_associadas = [tag.decode('utf-8') for tag in tags_associadas]

    print(f"Tags Associadas: {', '.join(tags_associadas)}")
    print("\n")


# Exibindo apenas artigo 1
article_data = client_redis.hgetall(article_key1)
print("Informações do Artigo:")
print(f"Chave: {article_key1}")
print(f"Nome: {article_data.get(b'name', b'N/A').decode('utf-8')}")
print(f"Descrição: {article_data.get(b'description', b'N/A').decode('utf-8')}")
print(f"Arquivo: {article_data.get(b'filename', b'N/A').decode('utf-8')}")
print(f"Data de Publicação: {article_data.get(b'postingdate', b'N/A').decode('utf-8')}")


tags_associadas_artigo1 = client_redis.smembers(f"{article_key1}:tags")
tags_associadas_artigo1 = [tag.decode('utf-8') for tag in tags_associadas_artigo1]
# Exibindo tags do artigo 1
print(f"Tags Associadas ao Artigo 1: {', '.join(tags_associadas_artigo1)}")

########## Exercicio 5

tag_desejada = "Tag1"

# Consultar os IDs dos artigos associados à tag específica
ids_dos_artigos = client_redis.smembers(f"tags:{tag_desejada}:articles")

if not ids_dos_artigos:
  print(f"Nenhum artigo associado à Tag '{tag_desejada}' foi encontrado.")
else:
  print(f"Artigos Associados à Tag '{tag_desejada}':")
  for artigo_id in ids_dos_artigos:
    artigo_data = client_redis.hgetall(artigo_id)
    artigo_data = {key.decode('utf-8'): value.decode('utf-8') for key, value in artigo_data.items()}

    print(f"ID do Artigo: {artigo_id.decode('utf-8')}")
    print(f"Nome: {artigo_data.get('name', 'N/A')}")
    print(f"Descrição: {artigo_data.get('description', 'N/A')}")
    print(f"Arquivo: {artigo_data.get('filename', 'N/A')}")
    print(f"Data de Publicação: {artigo_data.get('postingdate', 'N/A')}")
    print("\n")




