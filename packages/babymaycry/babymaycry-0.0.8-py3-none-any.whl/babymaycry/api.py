import pyaudio
import telegram
import asyncio
import audioop


class BabyMayCry:
    def __init__(self, bot_token, chat_id, threadhold=1000, period=1, verbose=False):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.threshold = threadhold
        self.period = period
        self.verbose = verbose
        self.rate = 44100
        self.chunk = 1024
        
    def run(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk)

        print("Listening for baby cry...")

        while True:
            try:
                max_rms = 0
                for _ in range(0, int(self.rate / self.chunk * self.period)):
                    data = stream.read(self.chunk)
                    rms = audioop.rms(data, 2)
                    max_rms = max(max_rms, rms)
                
                if self.verbose:
                    print("RMS:", max_rms)

                if max_rms > self.threshold:
                    print("Baby cry detected!")
                    self.send_message("Baby is crying!")
            except Exception as e:
                stream.stop_stream()
                stream.close()
                audio.terminate()
                raise e
        
    def infinity_run(self):
        while True:
            try:
                self.run()
            except Exception as e:
                import time
                print(e)
                time.sleep(5)
                continue
  
    def send_message(self, text):
        bot = telegram.Bot(token=self.bot_token)
        asyncio.run(bot.sendMessage(chat_id=self.chat_id, text=text))
