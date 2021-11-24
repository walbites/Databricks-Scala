# Databricks notebook source
# MAGIC %scala
# MAGIC //##########################################################################################################
# MAGIC //# VERSION  	DESARROLLADOR             FECHA        DESCRIPCION
# MAGIC //# -------------------------------------------------------------
# MAGIC //#  1        Walter Albites Azarte     23/11/2021   Curso Basico de Scala - Programacion Orientada a Objetos.
# MAGIC //##########################################################################################################

# COMMAND ----------

# MAGIC %run ./FieldUtil

# COMMAND ----------

# MAGIC %scala
# MAGIC import org.apache.spark.sql.types._
# MAGIC 
# MAGIC object Fields {
# MAGIC   object Ubigeos{
# MAGIC      val Key: String = "ubigeos"
# MAGIC     case object UbigeoField extends FieldUtil{
# MAGIC       override def name: String = "ubigeo"
# MAGIC       override def dataType: DataType = StringType
# MAGIC     }
# MAGIC     
# MAGIC     case object DistritoField extends FieldUtil{
# MAGIC       override def name: String = "distrito"
# MAGIC       override def dataType: DataType = StringType
# MAGIC     }
# MAGIC     
# MAGIC     case object ProvinciaField extends FieldUtil{
# MAGIC       override def name: String = "provincia"
# MAGIC       override def dataType: DataType = StringType
# MAGIC     }
# MAGIC     
# MAGIC     case object DepartamentoField extends FieldUtil{
# MAGIC       override def name: String = "departamento"
# MAGIC       override def dataType: DataType = StringType
# MAGIC     }
# MAGIC     
# MAGIC     case object LatitudField extends FieldUtil{
# MAGIC       override def name: String = "Latitud"
# MAGIC       override def dataType: DataType = FloatType
# MAGIC     }
# MAGIC     
# MAGIC     case object LongitudField extends FieldUtil{
# MAGIC       override def name: String = "Longitud"
# MAGIC       override def dataType: DataType = FloatType
# MAGIC     }
# MAGIC     
# MAGIC   }
# MAGIC   
# MAGIC }