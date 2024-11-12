import numpy as np
import random
from typing import TypeVar, List, Tuple
from collections import Counter
from modules.arbol_binario import ArbolBinario

T = TypeVar('T')


class RandomForest:
    def __init__(self, n_trees: int, bootstrap_rate: float, nivel_peso: float, profundidad_maxima: int):
        self.n_trees = n_trees
        self.bootstrap_rate = bootstrap_rate
        self.nivel_peso = nivel_peso
        self.profundidad_maxima = profundidad_maxima
        self.trees: List[ArbolBinario] = []

    def bootstrap_sample(self, data: List[Tuple[np.ndarray, int]]) -> List[Tuple[np.ndarray, int]]:
        sample_size = int(len(data) * self.bootstrap_rate)
        etiquetas = [etiqueta for _, etiqueta in data]
        conteo_etiquetas = Counter(etiquetas)

        pesos = {etiqueta: (conteo_etiquetas[etiqueta] ** self.nivel_peso) for etiqueta in conteo_etiquetas}
        total_pesos = sum(pesos.values())
        probabilidades = [pesos[etiqueta] / total_pesos for _, etiqueta in data]

        return random.choices(data, weights=probabilidades, k=sample_size)

    def train(self, data: List[Tuple[np.ndarray, int]]) -> None:
        for _ in range(self.n_trees):
            sample = self.bootstrap_sample(data)
            tree = ArbolBinario(self.profundidad_maxima)
            tree.insertar(sample)
            self.trees.append(tree)

    def predict(self, instance: np.ndarray) -> T:
        predictions = [tree.predecir(instance) for tree in self.trees]
        return max(set(predictions), key=predictions.count)