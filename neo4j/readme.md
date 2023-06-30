# neo4j
```
docker run -d --name neo4j_lwl -p 17474:7474 -p 17687:7687 -v $PWD/data:/data -v $PWD/logs:/logs -v $PWD/conf:/var/lib/neo4j/conf -v $PWD/import:/var/lib/neo4j/import --env NEO4J_AUTH=neo4j/password neo4j
```


用户名是：neo4j
密码是：password


# 查询所有节点
```
match(n) return n
```


# 删除所有
```
match(n) detach delete n
```