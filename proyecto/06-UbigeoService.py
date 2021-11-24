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

# MAGIC %run ./InputDataFrame

# COMMAND ----------

# MAGIC %run ./Filter

# COMMAND ----------

# MAGIC %scala
# MAGIC import org.apache.spark.sql.DataFrame
# MAGIC object UbigeosServices{
# MAGIC   def buildUbigeos(df:DataFrame): DataFrame = {df}
# MAGIC }

# COMMAND ----------

# MAGIC %scala
# MAGIC import org.apache.spark.sql.functions._
# MAGIC object ubigeoFilter extends UbigeoFilter{}
# MAGIC val dfBuildUbigeos= UbigeosServices.buildUbigeos(df_ubigeo)
# MAGIC                         .select(Fields.Ubigeos.UbigeoField.column,
# MAGIC                                 Fields.Ubigeos.DepartamentoField.column,
# MAGIC                                 Fields.Ubigeos.ProvinciaField.column,
# MAGIC                                 Fields.Ubigeos.DistritoField.column
# MAGIC                          ).filter(ubigeoFilter.filterUbigeoCajamarca)
# MAGIC display(dfBuildUbigeos)

# COMMAND ----------

# MAGIC %python
# MAGIC ##########################################################################################################
# MAGIC # Crear el directorio INTERMEDIA UBIGEO
# MAGIC # El objetivo es copiar la data que se necesita a INTERMEDIA UBIGEO la data filtrada
# MAGIC ##########################################################################################################
# MAGIC dbutils.fs.mkdirs("dbfs:/FileStore/INTERMEDIA/UBIGEO")

# COMMAND ----------

# MAGIC %scala
# MAGIC val targetPath = "/FileStore/INTERMEDIA/UBIGEO/cajamarca"
# MAGIC dfBuildUbigeos.write.mode("overwrite").parquet(targetPath)

# COMMAND ----------

# MAGIC %run ./WriteDataDrame