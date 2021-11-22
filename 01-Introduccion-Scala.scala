// Databricks notebook source
//##########################################################################################################
//# VERSION  	DESARROLLADOR             FECHA        DESCRIPCION
//# -------------------------------------------------------------
//#  1        Walter Albites Azarte     22/11/2021   Curso Basico de Scala - Programacion Orientada a Objetos.
//##########################################################################################################

// COMMAND ----------

// MAGIC %md
// MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Scala-full-color.svg/512px-Scala-full-color.svg.png" width="128" height="128" style="float: left: margin: 20px "/>
// MAGIC #### Scala Programacion Orientada a Objetos.

// COMMAND ----------

// MAGIC %md
// MAGIC ###### 1. Creación de una Clase Persona MUTABLE, con dni, nombre, telefono y edad. Los campos van definidos en el bloque, utilizando los argumentos del constructor.

// COMMAND ----------

// MAGIC %md
// MAGIC ###### 2. Versión INMUTABLE de la clase Persona anterior, con dni, nombre, telefono y edad. Los campos van definidos en el bloque, utilizando los argumentos del constructor.

// COMMAND ----------

// MAGIC %md
// MAGIC ###### 3. Los constructores y los campos se pueden unificar. Si algún argumento prescinde del modificador val no se creará un campo para él en la clase. En tal caso, será considerado como un argumento de entrada del constructor

// COMMAND ----------

// MAGIC  %md
// MAGIC ######4. Podemos declarar constructores adicionales mediante def this:

// COMMAND ----------

// MAGIC %md
// MAGIC ######5. Los métodos se añaden utilizando def. Podemos, por ejemplo, permitir que nuestra persona pueda disminuir su edad  dado un decremento.

// COMMAND ----------

// MAGIC %md
// MAGIC ######6. Es posible tener clases con una única instancia, lo que se conoce como Singleton Objects. Este componente nos permite reemplazar los miembros de clase propios de Java. Crearemos un Objeto Persona con valores iniciales y un método de creación de persona crear.

// COMMAND ----------

// MAGIC %md
// MAGIC ######7. Podemos aplicar herencia basica entre clases, definamos una clase Persona Juridica que hereda de nuestra clase Persona añadiendo un campo ruc

// COMMAND ----------

// MAGIC %md
// MAGIC ######8. Los Traits son interfaces que permiten la implementacion parcial, con lo que se permite la herencia multiple 

// COMMAND ----------

// MAGIC %md
// MAGIC ######9. Una clase Abstract. solo necesita usar cuando: Quieres crear una clase base que requiera argumentos de constructor o se requiera invocar a su código Scala desde el código Java
