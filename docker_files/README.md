<!--
https://medium.com/@newianlin/dockerize-sql-server-with-build-in-adventureworks-and-northwinds-e21d10c20a6b 

https://bricefotzo.medium.com/how-to-quickly-run-sql-queries-using-docker-3f310eaf6d3e
-->

# Setup docker PostgresSQL serwer with Northwind database

1. pull docker image

```bash
# get (pull) postgres image
docker pull postgres
```
### Dockerfile
```dockerfile
FROM postgres

ENV POSTGRES_DB=northwind
ENV POSTGRES_USER=northwind
ENV POSTGRES_PASSWORD=northwind

# Skopiuj plik SQL z zewnętrznego źródła do kontenera
COPY ./northwind.sql /docker-entrypoint-initdb.d/

# Wyeksponuj port 5432, na którym działa PostgreSQL
EXPOSE 5432

#RUN command
#RUN sh -c "psql -U postgres -a -f northwind.sql"
```

### Build new image with db
```bash
docker buildx build -t nwdb .
```

```bash
# run container
# -d - detached (background)
# -rm - remove container after quit
# -p - expose port
# -e - setting password for db
sudo docker run -d --rm -p 5432:5432 --name nwdbc -e POSTGRES_PASSWORD=northwind -d nwdb
```