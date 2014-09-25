awsdbcreator
============

Script to continuously create PostgreSQL databases and store their definitions on a AWS SQS queue.
(It is typically used to e.g. create databases to host PostgreSQL FDW tables created on-demand.)

The script monitors the number of messages (i.e. the number of "available" databases) in the SQS queue.
Whenever this number drops under a threshold, new databases are automatically created.

# Databases vs Schemas

The script does not actually continuously create PostgreSQL databases.
Instead, it creates a single new database at startup and then continuously create schemas within that database.
This is done to circumvent a PostgreSQL limitation: PostgreSQL does not cope well with a very large number of databases but copes well with a very large number of schemas within a database.
