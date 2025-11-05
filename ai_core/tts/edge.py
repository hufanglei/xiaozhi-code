import edge_tts
import asyncio


class Edge_TTS:
    def __init__(self):
        self.voice = "zh-CN-XiaoxiaoNeural"

    async def text_to_speech(self, text, audio_path):
        try:
            # 检查文本是否为空或无效
            if not text or not text.strip():
                raise ValueError("文本内容为空")

            print(f"TTS 正在生成语音，文本长度: {len(text)}")
            print(f"文本内容: {text[:100]}...")  # 只打印前100个字符

            communicate = edge_tts.Communicate(text, self.voice)
            await communicate.save(audio_path)

            print(f"语音文件已保存: {audio_path}")
            return audio_path

        except Exception as e:
            print(f"TTS 错误: {e}")
            raise

    def text_to_speech_sync(self, text, audio_path):
        """同步版本"""
        return asyncio.run(self.text_to_speech(text, audio_path))