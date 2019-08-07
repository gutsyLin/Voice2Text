
from aip import AipSpeech

from record_tool import record_pcm1600

app_id = ''
app_key = ''
secret_key = ''


client = AipSpeech(app_id, app_key, secret_key)

r = client.asr(record_pcm1600(), 'pcm', 16000, {'dev_pid': 1536})
print(r)

