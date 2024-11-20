# TPI de Algoritmos 2

## Integrantes

- Juana Molina
- Silvia Fernández
- Javier Rodriguez

## Setup

```sh
# Clonamos repositorio
git clone https://github.com/JaviCeRodriguez/algoritmos2_tpi.git

# Entramos al repositorio clonado
cd ./algoritmos2_tpi

# Creamos un entorno virtual
python3 -m venv nombre_entorno

# (Para Mac o Linux) Activamos el entorno
source nombre_entorno/bin/activate

# (Para Windows) Activamos el entorno
nombre_entorno/Scripts/activate

# Instalamos los paquetes necesarios
(nombre_entorno) pip install -r requirements.txt
```

## Correr código

- En la carpeta `modules` están las clases utilizadas para entrenar los modelos, se pueden correr estos archivos por separado si lo desean.
- En el root van a encontrar dos notebooks: `analisis_datasets_scikit.ipynb` y `analisis_datasets_paper.ipynb`. La segunda notebook es la utilizada para elaborar el informe. Pueden abrirlo desde Google Colab (colocando las clases usadas en una carpeta `modules` o como parte de la notebook). También levantar esta notebook usando el comando en terminal `jupyter notebook`.

## Planificación

- [x] Elección de paper o trabajo de investigación para validar
- [x] Tipos de algoritmos a utilizar
- [x] Desarrollo de algoritmos propios para validar paper
- [x] Re-iterar pasos realizados y mejorar calidad de código + performance
- [x] Obtener resultados y describirlos en informe
