import asyncio
import os

from ai_core.llm.chatglm import ChatGLM_LLM
from ai_core.tts.edge import Edge_TTS

if __name__ == "__main__":
    llm = ChatGLM_LLM()
    response = llm.generate_response("你好")
    print("ChatGLM-4-Flash:", response)

    tts = Edge_TTS()
    output_file = asyncio.run(tts.text_to_speech(response, "test.mp3"))
    # windows播放
    os.system(f"start {output_file}")
