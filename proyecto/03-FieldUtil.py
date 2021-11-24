# Databricks notebook source
# MAGIC %scala
# MAGIC //##########################################################################################################
# MAGIC //# VERSION  	DESARROLLADOR             FECHA        DESCRIPCION
# MAGIC //# -------------------------------------------------------------
# MAGIC //#  1        Walter Albites Azarte     23/11/2021   Curso Basico de Scala - Programacion Orientada a Objetos.
# MAGIC //##########################################################################################################

# COMMAND ----------

# MAGIC %scala
# MAGIC import org.apache.spark.sql.Column
# MAGIC import org.apache.spark.sql.functions.col
# MAGIC import org.apache.spark.sql.types.DataType
# MAGIC import org.apache.spark.sql.functions.substring
# MAGIC 
# MAGIC trait FieldUtil {
# MAGIC   def name: String
# MAGIC   def dataType: DataType
# MAGIC   def column: Column = col(name)
# MAGIC   def value(valueColumn: Column): Column = valueColumn.cast(dataType).alias(name)
# MAGIC }