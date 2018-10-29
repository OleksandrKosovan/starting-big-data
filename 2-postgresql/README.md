# PostgreSQL

![alt txt](https://miro.medium.com/max/1046/1*O7v5p22lVQXfFZbbv-PTkw.png)

### My goal

My main goal is build data cube with PostgreSQL, but i need to learn queries for it.

### What i do for it?

I use [PostgreSQL tutorial](http://www.postgresqltutorial.com/).

First, i installed PostgreSQL on Ubuntu 18.04. [Link - digitalocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Second, i created user.

`$ sudo -i -u postgres`

`$ psql`

`CREATE USER some-name-user WITH PASSWORD "some-password"`

`ALTER USER some-name-user WITH SUPERUSER`

Next step is using [pgAdmin III](https://www.pgadmin.org/). It is PostgreSQL Tools.

### After installing. About learning

I will use sample data set for learning. [Link](http://www.postgresqltutorial.com/postgresql-sample-database/)

**Scheme**

![alt txt](http://www.postgresqltutorial.com/wp-content/uploads/2018/03/dvd-rental-sample-database-diagram.png)
