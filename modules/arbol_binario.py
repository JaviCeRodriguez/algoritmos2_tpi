import random
from typing import TypeVar, List, Tuple

import numpy as np

T = TypeVar('T')


class ArbolBinario:
    def __init__(self, profundidad_maxima: int, profundidad_actual: int = 0):
        self.valor: T = None
        self.caracteristica: int = None
        self.umbral: float = None
        self.izquierda: 'ArbolBinario' = None
        self.derecha: 'ArbolBinario' = None
        self.profundidad_maxima = profundidad_maxima
        self.profundidad_actual = profundidad_actual

    def insertar(self, data: List[Tuple[np.ndarray, int]]) -> None:
        if len(data) == 0:
            return
        etiquetas = [etiqueta for _, etiqueta in data]
        self.valor = max(set(etiquetas), key=etiquetas.count)

        if self.profundidad_actual >= self.profundidad_maxima or len(set(etiquetas)) == 1:
            return

        n_features = len(data[0][0])
        self.caracteristica = random.randint(0, n_features - 1)
        valores_caracteristica = [x[self.caracteristica] for x, _ in data]
        self.umbral = np.median(valores_caracteristica)

        izquierda_data = [(x, y) for x, y in data if x[self.caracteristica] <= self.umbral]
        derecha_data = [(x, y) for x, y in data if x[self.caracteristica] > self.umbral]

        self.izquierda = ArbolBinario(self.profundidad_maxima, self.profundidad_actual + 1)
        self.derecha = ArbolBinario(self.profundidad_maxima, self.profundidad_actual + 1)

        self.izquierda.insertar(izquierda_data)
        self.derecha.insertar(derecha_data)

    def predecir(self, instance: np.ndarray) -> T:
        if self.izquierda is None or self.derecha is None:
            return self.valor
        if instance[self.caracteristica] <= self.umbral:
            return self.izquierda.predecir(instance)
        else:
            return self.derecha.predecir(instance)