from aip import AipSpeech


def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()

app_id = ''
app_key = ''
secret_key = ''


client = AipSpeech(app_id, app_key, secret_key)

r = client.asr(get_file_content('test.pcm'), 'pcm', 16000, {'dev_pid': 1536})
print(r)
