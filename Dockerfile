FROM mariadb
ENV MARIADB_ROOT_PASSWORD="12345"
ENV MARIADB_DATABASE="workplace"
ENV MARIADB_USER="hardi"
ENV MARIADB_PASSWORD="hardi"
ADD employees.sql /docker-entrypoint-initdb.d/employees.sql
EXPOSE 3306