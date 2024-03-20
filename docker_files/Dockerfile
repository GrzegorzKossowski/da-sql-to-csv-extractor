FROM postgres

#WORKDIR /the/workdir/path - where to execute commands
#WORKDIR /sql

ENV POSTGRES_DB=northwind
ENV POSTGRES_USER=northwind
ENV POSTGRES_PASSWORD=northwind

# Skopiuj plik SQL z zewnętrznego źródła do kontenera
COPY ./northwind.sql /docker-entrypoint-initdb.d/

# Wyeksponuj port 5432, na którym działa PostgreSQL
EXPOSE 5432

#RUN command
#RUN sh -c "psql -U postgres -a -f northwind.sql"