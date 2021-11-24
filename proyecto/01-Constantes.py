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
# MAGIC import org.apache.spark.sql.functions.{lit, typedLit}
# MAGIC 
# MAGIC object Constantes {
# MAGIC   object FiltroUbigeo{
# MAGIC       val Cajamarca="06"
# MAGIC     }
# MAGIC }