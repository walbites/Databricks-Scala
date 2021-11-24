# Databricks notebook source
# MAGIC %scala
# MAGIC //##########################################################################################################
# MAGIC //# VERSION  	DESARROLLADOR             FECHA        DESCRIPCION
# MAGIC //# -------------------------------------------------------------
# MAGIC //#  1        Walter Albites Azarte     23/11/2021   Curso Basico de Scala - Programacion Orientada a Objetos.
# MAGIC //##########################################################################################################

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls dbfs:/FileStore/tables/

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/FileStore/INICIAL")

# COMMAND ----------

dbutils.fs.cp("dbfs:/FileStore/tables/ubigeo.csv", "dbfs:/FileStore/INICIAL/ubigeo.csv")

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/FileStore/INICIAL/

# COMMAND ----------

# MAGIC %scala
# MAGIC import org.apache.spark.sql.types._
# MAGIC 
# MAGIC val path = "/FileStore/INICIAL/ubigeo.csv"
# MAGIC 
# MAGIC val schema = new StructType()
# MAGIC   .add("UBIGEO",StringType,true)
# MAGIC   .add("DISTRITO",StringType,true)
# MAGIC   .add("PROVINCIA",StringType,true)
# MAGIC   .add("DEPARTAMENTO",StringType,true)
# MAGIC   .add("LATITUD",FloatType,true)
# MAGIC   .add("LONGITUD",FloatType,true)
# MAGIC 
# MAGIC val df_ubigeo = spark.read.format("csv")
# MAGIC   .option("header", "true")
# MAGIC   .schema(schema)
# MAGIC   .load(path)