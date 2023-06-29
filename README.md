# TP-Containers
**Trabajo Práctico - Laboratorio de Programación III**

*Etapa 1:*

En un principio, se nos solicita realizar un sistema para gestionar el transporte de contenedores en barcos siguiendo ciertas reglas específicas. A continuación vamos a enumerar las peticiones y cómo las fuimos solucionando.

**Barcos**

La empresa cuenta con dos tipos de Barcos, los básicos y los especializados. Para resolver la división de clases utilizamos una clase abstracta **barco** que luego cuenta con dos subclases “BarcoBasico” y “BarcoEspecial”. Estos heredan los atributos y métodos de barco. La división se realizó pensando en la diferencia de uso que se le da a los barcos dependiendo de sus capacidades. Contiene una lista de contenedores que se van cargando si pueden ingresar al barco.

**Contenedores**

En un principio, seguimos la misma lógica que con Barco. Se nos planteó la existencia de 3 tipos de contenedores. Básico, HighCube, Flat Rack. No existía una gran división entre las mercaderías más allá de las medidas, así que nos regimos por estas mismas, diferenciando con un bool de “esEspecial” en caso de que la mercadería sea especial y deba ingresar a un Flat Rack. Básico, HC y FlatRack heredan de Contenedor. Cuenta con una lista de Mercadería que se va cargando al contenedor, así como lo va llenando.

**Mercadería**

Existencia de la clase a grandes rasgos, marcando si era especial o no. Cuenta con una relación con Cliente.

**Cliente**

Resuelve para tener a quién entrega la mercadería, decide si quiere ir a retirar el pedido o si utiliza el servicio puerta a puerta. Se le asigna también un precio a su pedido.

**Modulo GPS**

Utilizamos un mock para “hacer de GPS”. Este nos sirve para los cálculos de distancias recorridas entre barcos.

*Etapa 2 – Patrones y Principios SOLID*

**Barcos**

Nuevas peticiones:

\1) Sistema de propulsión: Vela y Motor, afectan el gasto de combustible En grupo planteamos utilizar el Patrón State\. La Interfaz State seria nuestro Sistema de Propulsion, los estados concretos son Vela y Motor, y el contexto es el Barco\.

Este patrón nos sirve dado que en tiempo de ejecución debemos cambiar el sistema de propulsion de nuestro barco, afectando el gasto de combustible.

Vela: no gasta combustible cuando se utiliza Motor: gasta 6 litros de combustible por hora

Implementación del patrón :

![](Test/diag_sistema_prop.png)

**Modulo Contable :**

La aplicación debe contar con un módulo cuya función principal es obtener el resultado económico de un determinado barco. El resultado económico de un barco se puede calcular como el beneficio obtenido a partir de los contenedores transportados menos los gastos de combustible reportados.

Para resolverlo planteamos crear una clase Viaje, la misma tendrá información importante del viaje que esté realizando el Barco. Es importante aclarar que medimos el viaje por hora, para poder trabajar más cómodamente. Información de la clase Viaje:

- Sede por la que se inicia
- Sede por la que se finaliza
- Duración del viaje medido en horas
- Kilómetros recorridos

![](Test/diag_viaje.jpeg)

Es importante aclarar que tanto el viaje como el módulo darán resultados correctos si se ejecutan los métodos en el momento correcto, dado que en el caso de no actualizar el combustible total al final de cada viaje y pasar ese objeto Viaje(sin actualizar) al Módulo Contable éste dará falsos resultados, ya que no se registró de forma correcta el uso del combustible en ese viaje.

Antes de pasar el objeto Viaje al Módulo Contable, se debe estar seguro de que ese objeto (o sea Viaje) tiene los datos actualizados

![](Test/diag_modulo_cont.png)

**Distribución de la Mercadería**

En la nueva versión del trabajo, se nos plantean nuevas reglas en relación a la mercadería. Esta misma se especializa un poco más, dividiéndose entre Mercadería (normal), Alimentos y Residuos Tóxicos. Teniendo en cuenta esto, no todas las mercaderías pueden ser transportadas por cualquier contenedor. Lo tóxico no se mezcla con los alimentos, los contenedores Ventilados son los que pueden llevar alimento, se crean nuevos contenedores más amplios, etc.

Decidimos que la mejor manera de manipular la mercadería sería a través del patrón Chains of Responsibility. El patrón está compuesto por los diferentes tipos de Contenedores, estos tendrán las validaciones necesarias para ver si pueden llevar o no al producto (teniendo en cuenta las medidas, el tipo de mercadería, si está completo, etc…) y contamos con un manejador que es la interfaz que lleva el patrón.

![](Test/diag_cor_mercaderia.png)

**Distribución de los contenedores en los barcos**

Teniendo en cuenta que teníamos dos tipos de barcos, elegimos usar nuevamente el patrón Chains of Responsibility para controlar el manejo de a dónde entra cada contenedor. Seguimos la misma lógica de tener un manejador y las clases que lo implementan.

![](Test/diag_cor_contenedores.png)