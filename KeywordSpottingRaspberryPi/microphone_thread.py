import queue

import pyaudio


class MicrophoneThread:
    def __init__(self,
                 sampling_frequency: int,
                 format_of_sample,
                 number_of_bytes_in_sample: int,
                 number_of_channels: int,
                 number_of_samples_in_chunk: int,
                 multithread_queue: queue.Queue) -> None:
        super().__init__()
        self._sampling_frequency: int = sampling_frequency

        self._format_of_sample = format_of_sample
        self._number_of_bytes_in_sample: int = number_of_bytes_in_sample
        self._number_of_channels: int = number_of_channels

        self._number_of_samples_in_chunk: int = number_of_samples_in_chunk

        self._multithread_queue: queue.Queue = multithread_queue

        self._pyaudio_object = pyaudio.PyAudio()
        self._microphone_stream: pyaudio.PyAudio.Stream \
            = self._pyaudio_object.open(
                input=True,
                rate=self._sampling_frequency,
                format=self._format_of_sample,
                channels=self._number_of_channels,
                frames_per_buffer=self._number_of_samples_in_chunk,
                stream_callback=self._callback)
     
    def _callback(self,
                  in_data: bytes,
                  frame_count: int,
                  time_info,
                  status):
        # Check arguments.
        if ((status == pyaudio.paInputUnderflow) or
            (status == pyaudio.paInputOverflow)):
            dummy_bytes: bytes = bytes(frame_count *
                                       self._number_of_channels *
                                       self._number_of_bytes_in_sample)
            return (dummy_bytes, pyaudio.paAbort)

        # If multithread queue is not full.
        try:
            for byte in in_data:
                self._multithread_queue.put(item=byte,
                                            block=False)
            return (None, pyaudio.paContinue)

        # If multithread queue is full.
        except queue.Full:
            print("Multithread queue is full! Terminating microphone thread!")
            dummy_bytes: bytes = bytes(frame_count *
                                       self._number_of_channels *
                                       self._number_of_bytes_in_sample)
            return (dummy_bytes, pyaudio.paAbort)

    def is_active(self) -> bool:
        return self._microphone_stream.is_active()
        
    def close(self) -> None:
        self._microphone_stream.close()
        self._pyaudio_object.terminate()