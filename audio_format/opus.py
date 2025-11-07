import os

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
        self.opus_frame_time = 60


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

        opus_data = []

        for i in range(0, len(raw_data), 960):
            opus_data.append(encoder.encode(raw_data[i:i+48000], 48000))