import redis

client_redis = redis.Redis(
  host='redis-11614.c308.sa-east-1-1.ec2.cloud.redislabs.com',
  port=11614,
  password='kpTCvmSuK4TjXT3wf2CU384PMElVFpOA')

# Exercicios 1 e 2:  criar modelos de dados no redis para artigos e tags 
# (utilizando HASH para artigos e SET para tags) Populando ambos com dados
# e relacionando-os.

# Defina um conjunto para armazenar as tags
tags = ["Tag1", "Tag2", "Tag3"]

for tag in tags:
    client_redis.sadd("tags:set", tag)

# Para verificar as tags no conjunto:
tags_no_conjunto = client_redis.smembers("tags:set")
print("Tags no conjunto:", tags_no_conjunto)

# Agora, você pode associar tags a artigos usando os conjuntos de tags
article_data = {
    "name": "Artigo 1",
    "description": "Descrição do Artigo 1",
    "filename": "artigo1.txt",
    "postingdate": "2023-09-01",
}

# Defina o hash para o artigo
article_key = "article:1"
client_redis.hmset(article_key, article_data)

# Associe as tags ao artigo usando os conjuntos de tags
tags_associadas = ["Tag1", "Tag2"]
for tag in tags_associadas:
    client_redis.sadd(f"article:{article_key}:tags", tag)

# Para verificar as tags associadas a um artigo:
tags_associadas_artigo = client_redis.smembers(f"article:{article_key}:tags")
print("Tags associadas ao artigo:", tags_associadas_artigo)