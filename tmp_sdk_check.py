from google import genai
import inspect
from google.genai import types
print('google.genai imported')
print('types.LiveConnectConfig:', hasattr(types, 'LiveConnectConfig'))
print('types.VoiceConfig:', hasattr(types, 'VoiceConfig'))
print('types.SpeechConfig:', hasattr(types, 'SpeechConfig'))
print('genai.Client:', hasattr(genai, 'Client'))
print('Client init sig:', inspect.signature(genai.Client))
