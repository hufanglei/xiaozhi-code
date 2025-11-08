import os

import numpy as np
import opuslib_next
from pydub import AudioSegment


class Opus_Encode:
    def __init__(self):
        self.sample_rate = 16000
        self.channel = 1
        self.sample_width = 2
        self.opus_sample_rate = 16000
        self.opus_channel = 1
        self.opus_sample_width = 2
        self.opus_frame_time = 60 # 60ms

    # 将下面的代码补全注释
    def audio_to_opus(self, audio_file_path):
        file_type = os.path.splitext(audio_file_path)[1]
        if file_type:
            file_type = file_type.lstrip(".")

        # 加载音频文件
        audio = AudioSegment.from_file(audio_file_path, format=file_type)

        # 调整音频参数
        audio = audio.set_channels(self.channel).set_frame_rate(self.sample_rate).set_sample_width(self.sample_width)

        # 计算音频总时长，单位为秒
        duration = len(audio)
        print(f"音频总时长为：{duration} 秒")

        # 获取音频PCM数据
        raw_data = audio.raw_data
        print(f"音频PCM数据大小为：{ len(raw_data) } 字节")

        encoder = opuslib_next.Encoder(self.opus_sample_rate, self.opus_channel, opuslib_next.APPLICATION_AUDIO)

        # 获取每一帧的O采样数
        frame_num = int(self.opus_sample_rate / 1000 * self.opus_frame_time)

        # 计算每帧的采样字节数
        frame_bytes_size = frame_num * self.opus_channel * self.opus_sample_width

        opus_datas = []

        for i in range(0, len(raw_data), frame_bytes_size):
            # 获取当前帧的PCM数据
            chunk = raw_data[i:i+frame_bytes_size]
            # 计算当前帧长度
            chunk_len = len(chunk)
            if chunk_len < frame_bytes_size:
                # 补0
                chunk +=  b'\x00' * (frame_bytes_size - chunk_len)

            np_frame = np.frombuffer(chunk, dtype=np.int16)

            np_bytes = np_frame.tobytes()

            opus_data = encoder.encode(np_bytes, frame_num)

            opus_datas.append(opus_data)

        return opus_datas, duration

if __name__ == "__main__":
    opus = Opus_Encode()
    opus_datas, duration = opus.audio_to_opus("../../test.mp3")
    print(f"音频总时长为：{duration} 秒")
    print(f"音频OPUS数据大小为：{ len(opus_datas) } 字节")
    print()