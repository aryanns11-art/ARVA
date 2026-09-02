import asyncio
import tempfile
import os

import edge_tts
import pygame


VOICE = "en-US-AvaMultilingualNeural"


async def _generate_speech(text, output_file):
    text = text.replace("ARVA", "Arva")

    communicate = edge_tts.Communicate(
        text,
        VOICE
    )

    await communicate.save(output_file)


def speak(text):
    if not text:
        return

    with tempfile.NamedTemporaryFile(
        suffix=".mp3",
        delete=False
    ) as temp:
        audio_file = temp.name

    try:
        # Generate speech
        asyncio.run(_generate_speech(text, audio_file))

        # Play audio directly
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # Wait until speech finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

    except Exception as e:
        print(f"TTS Error: {e}")

    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)