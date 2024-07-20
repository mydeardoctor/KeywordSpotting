import collections
import queue

import numpy as np
import pyaudio

from microphone_thread import MicrophoneThread
from model import Model
from preprocessor import Preprocessor


def main():
    # Parameters.

    # Frequency.
    SAMPLING_FREQUENCY: int = 16000

    # Time.
    FORMAT_OF_SAMPLE = pyaudio.paInt16
    NUMBER_OF_BYTES_IN_SAMPLE: int = pyaudio.get_sample_size(
        format=FORMAT_OF_SAMPLE) # 2
    NUMBER_OF_CHANNELS: int = 1

    NUMBER_OF_SECONDS_IN_BUFFER: int = 1
    NUMBER_OF_SAMPLES_IN_BUFFER: int = (SAMPLING_FREQUENCY *
                                        NUMBER_OF_SECONDS_IN_BUFFER *
                                        NUMBER_OF_CHANNELS) # 16000
    NUMBER_OF_BYTES_IN_BUFFER: int = (NUMBER_OF_SAMPLES_IN_BUFFER *
                                      NUMBER_OF_BYTES_IN_SAMPLE) # 32000

    NUMBER_OF_SECONDS_IN_CHUNK: float = 0.05  # 50 ms
    NUMBER_OF_SAMPLES_IN_CHUNK: int = (int(SAMPLING_FREQUENCY *
                                           NUMBER_OF_SECONDS_IN_CHUNK *
                                           NUMBER_OF_CHANNELS)) # 800
    NUMBER_OF_BYTES_IN_CHUNK: int = (NUMBER_OF_SAMPLES_IN_CHUNK *
                                     NUMBER_OF_BYTES_IN_SAMPLE) # 1600

    # Model.
    MODEL_FILENAME: str = "lite_model.tflite"
    LABELS: list[str] = ["down",
                         "go",
                         "left",
                         "no",
                         "off",
                         "on",
                         "right",
                         "stop",
                         "up",
                         "yes",
                         "silence",
                         "unknown"]
    THRESHOLD: float = 0.90

    # Create one second buffer.
    empty_list: list[int] = [0] * NUMBER_OF_BYTES_IN_BUFFER
    one_second_buffer: collections.deque = collections.deque(
        empty_list,
        maxlen=NUMBER_OF_BYTES_IN_BUFFER)

    # Create multithread queue for chunks.
    multithread_queue: queue.Queue = queue.Queue(
        maxsize=NUMBER_OF_BYTES_IN_BUFFER * 2)

    # Load model.
    model: Model = Model(model_filename=MODEL_FILENAME,
                         labels=LABELS,
                         threshold=THRESHOLD)
    # Dummy first call, because first call is slow.
    dummy_audio: np.ndarray = Preprocessor.preprocess(
        one_second_buffer=one_second_buffer)
    dummy_label: str = model.predict(audio=dummy_audio)

    # Create microphone thread.
    microphone_thread: MicrophoneThread = MicrophoneThread(
        sampling_frequency=SAMPLING_FREQUENCY,
        format_of_sample=FORMAT_OF_SAMPLE,
        number_of_bytes_in_sample=NUMBER_OF_BYTES_IN_SAMPLE,
        number_of_channels=NUMBER_OF_CHANNELS,
        number_of_samples_in_chunk=NUMBER_OF_SAMPLES_IN_CHUNK,
        multithread_queue=multithread_queue)

    # Main thread.
    print("Speak:")
    try:
        while microphone_thread.is_active() is True:
            # Remove chunk from beginning of one second buffer.
            for i in range(0, NUMBER_OF_BYTES_IN_CHUNK, 1):
                one_second_buffer.popleft()

            # Append chunk to one second buffer.
            for i in range(0, NUMBER_OF_BYTES_IN_CHUNK, 1):
                # Waiting for chunk in blocking mode.
                byte = multithread_queue.get(block=True,
                                             timeout=None)
                one_second_buffer.append(byte)

            # Preprocess.
            audio: np.ndarray = Preprocessor.preprocess(
                one_second_buffer=one_second_buffer)

            # Predict.
            label: str = model.predict(audio=audio)
            if label:
                print(label)

    except BaseException as e:
        print(type(e))
        print(e)
        print("Stopping main thread!")

    finally:
        microphone_thread.close()


if __name__ == "__main__":
    main()