# Databricks notebook source
# MAGIC %scala
# MAGIC //##########################################################################################################
# MAGIC //# VERSION  	DESARROLLADOR             FECHA        DESCRIPCION
# MAGIC //# -------------------------------------------------------------
# MAGIC //#  1        Walter Albites Azarte     23/11/2021   Curso Basico de Scala - Programacion Orientada a Objetos.
# MAGIC //##########################################################################################################

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP DATABASE IF EXISTS databricks;
# MAGIC CREATE DATABASE IF NOT EXISTS databricks;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS databricks.cajamarca;
# MAGIC CREATE TABLE IF NOT EXISTS databricks.cajamarca
# MAGIC (
# MAGIC UBIGEO STRING,
# MAGIC DEPARTAMENTO STRING,
# MAGIC PROVINCIA STRING,
# MAGIC DISTRITO STRING,
# MAGIC LATITUD DOUBLE,
# MAGIC LONGITUD DOUBLE
# MAGIC )
# MAGIC USING PARQUET
# MAGIC OPTIONS ('compression'='snappy')
# MAGIC LOCATION 'dbfs:/FileStore/INTERMEDIA/UBIGEO/cajamarca';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricks.cajamarca LIMIT 5;