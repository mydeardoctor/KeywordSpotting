import numpy as np
import tensorflow as tf


class Model:
    def __init__(self,
                 model_filename: str,
                 labels: list[str],
                 threshold: float) -> None:
        super().__init__()
        interpreter: tf.lite.Interpreter = tf.lite.Interpreter(
            model_path=model_filename)
        self._model = interpreter.get_signature_runner()
        
        # Find out model input name and model output name.
        self._model_input_name: str = ""
        self._model_output_name: str = ""
        signature_defs = interpreter.get_signature_list()
        for signature_def_name, model_inputs_and_outputs in signature_defs.items():
            model_inputs_names = model_inputs_and_outputs["inputs"]
            self._model_input_name = model_inputs_names[0]
            model_outputs_names = model_inputs_and_outputs["outputs"]
            self._model_output_name = model_outputs_names[0]
        
        self._labels: list[str] = labels
        self._threshold: float = threshold

    def predict(self,
                audio: np.ndarray) -> str:
        model_input_kwarg = {self._model_input_name: audio}
        model_outputs = self._model(**model_input_kwarg)
        probabilities = model_outputs[self._model_output_name]
        index_of_max_probability = np.argmax(a=probabilities)
        max_probability = probabilities[index_of_max_probability]
        label: str = ""
        if max_probability >= self._threshold:
            label = self._labels[index_of_max_probability]
        return label