# Databricks notebook source
# MAGIC %scala
# MAGIC //##########################################################################################################
# MAGIC //# VERSION  	DESARROLLADOR             FECHA        DESCRIPCION
# MAGIC //# -------------------------------------------------------------
# MAGIC //#  1        Walter Albites Azarte     23/11/2021   Curso Basico de Scala - Programacion Orientada a Objetos.
# MAGIC //##########################################################################################################

# COMMAND ----------

# MAGIC %run ./Fields

# COMMAND ----------

# MAGIC %run ./Constantes

# COMMAND ----------

# MAGIC %scala
# MAGIC trait UbigeoFilter{
# MAGIC   def filterUbigeoCajamarca: Column={
# MAGIC     substring(Fields.Ubigeos.UbigeoField.column,1,2)===Constantes.FiltroUbigeo.Cajamarca
# MAGIC   }
# MAGIC   //def FilterUbigeoLima
# MAGIC   //def FilterUbigeoArequipa
# MAGIC }