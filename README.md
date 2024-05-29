*Introducción

Para esta entrega se trabajó la parte de la tokenización, la limpieza de los datos, y la clusterisación permitiendo una clasificación básica de los documentos enviados. Se trabajo en la reducción de las etiquetas utilizadas por el cliente para manejar la facilidad con el modelo de clasificación, se dio el comienzo de un scraper el cual nos permite recolectar más documentos para tener una muestra mayor.

*Arquitectura

Funcionamiento 
![Funcionamiento.jpg](https://github.com/eisazav/idp/blob/main/imagenes/Items.jpeg)

*Tecnologías y librerías usadas:
Lenguaje de programación y base de datos
- [ ]Python 
- [ ]Postgre [BD]
  
Preparación de datos
- [ ]Tika [Lector pdf]
- [ ]Nltk
- [ ]Sklearn [Cluster]
  
Modelo
- [ ]Sklearn [IA]
- [ ]Docker

Balanceo de las etiquetas
El cliente tiene un total de 68 etiquetas y 213 archivos etiquetados con múltiples etiquetas.
Realizamos un conteo de las etiquetas para reducir las etiquetas posibles lo que nos dio que de las 68 etiquetas 38 no se usan en los archivos etiquetas

|ID|Nombre etiqueta|Cantidad|
|--|--|--|
| 892 | Industria Agrícola y Cultivos|114|
| 893 | Producción Pecuaria|115|
| 894 | Producción Pecuaria: Ganadero|108|
| 895 | Producción Pecuaria: Piscícola|105|
| 896 | Producción Pecuaria: Porcícola|106|
| 897 | Producción Pecuaria: Avícola|105|
| 898 | Industria Minera: Metales y Pétreos|110|
| 899 | Explotación Forestal|0|
| 900 | Industria de la Construcción|120|
| 901 | Industria de Infraestructura|118|
| 902 | Industria Fabricación de Muebles|0|
| 903 | Industria Fabricación y Transformación de Vidrio|0|
| 904 | Industria Papel y Cartón|0|
| 905 | Industria Alimentos y Bebidas|114|
| 906 | Industria Textil|107|
| 907 | Industria del Calzado|0|
| 908 | Industria Marroquinera|0|
| 909 | Industria Automotriz|0|
| 910 | Industria Fabricación de Repuestos Automotriz|0|
| 911 | Industria Eléctricos, Electrónicos y Electrodomésticos|107|
| 912 | Industria Maderera|0|
| 913 | Industria Cerámica y Porcelana|0|
| 914 | Industria Cementera|0|
| 915 | Industria Siderúrgica|0|
| 916 | Industria Reciclaje de Materiales|0|
| 917 | Industria Editorial e Imprenta|0|
| 918 | Industria Química|108|
| 919 | Industria Química: Cosméticos|114|
| 920 | Industria Química: Agroquímicos|115|
| 921 | Industria Química: Farmacéutica|117|
| 922 | Industria Polímeros|0|
| 923 | Industria Química: Solventes, Pinturas y Colorantes|105|
| 925 | Tratamiento de Agua|0|
| 926 | Suministro de Gas|0|
| 927 | Recolección y Disposición de Residuos Sólidos|0|
| 928 | Educación: Universidades, Institutos, Colegios, Escuelas y Jardines Infantiles (Público)|99|
| 930 | Ayudas Diagnosticas|0|
| 931 | Consultorios Médicos y Odontológicos|0|
| 932 | Laboratorios Clínicos|0|
| 933 | Centros Veterinarios|0|
| 934 | Administración de Propiedad Horizontal|0|
| 935 | Cosmetología y Peluquerías|83|
| 936 | Morgues y Funerarias|0|
| 937 | Hotelería y Turismo|0|
| 938 | Transporte Terrestre: Pasajeros|88|
| 939 | Transporte Terrestre: Carga|87|
| 940 | Transporte Férreo|0|
| 941 | Servicios Financieros|69|
| 942 | Servicios Administrativos, Consultoría y Asesoría|69|
| 943 | Call Center|69|
| 944 | Telecomunicaciones|0|
| 945 | Centros Comerciales|69|
| 946 | Restaurantes|56|
| 947 | Venta de Combustibles y Lubricantes|0|
| 948 | Almacenes de Cadena y Grandes Superficies|71|
| 949 | Tiendas y Abarrotes|0|
| 950 | Farmacias|0|
| 951 | Almacenes y Distribuidores de Productos en General|0|
| 952 | Establecimientos de Ocio y  Esparcimiento|0|
| 958 | Educación: Universidades, Institutos, Colegios, Escuelas y Jardines Infantiles (Privado)|94|
| 959 | Clínicas y Hospitales (Privado)|112|
| 960 | Clínicas y Hospitales (Público)|39|
| 961 | Año diferente|0|
| 962 | Etiquetas|0|
| 963 | Tema|0|
| 964 | Subtema|0|
| 965 | Temporales|0|
| 966 | Derogatoria tácita|0|

Teniendo en cuenta el conteo y la opinión del cliente se agruparon las etiquetas en 5 grupos:

- Producción
- Educación
- Transporte
- Clínicas y Hospitales
- Industria

Con estos grupos se realizo la agrupación de los archivos según la cantidad de etiquetas de cada grupo
resultado
![Figure_1.png](https://github.com/eisazav/idp/blob/main/imagenes/Items2.png)

*Clusterización

![Coso4.png](https://github.com/eisazav/idp/blob/main/imagenes/Items3.png)

![Coso.png](https://github.com/eisazav/idp/blob/main/imagenes/Items4.png)
