message='i want to order chinese from  mainland china and pizza from domminos'
entity_name='restaurant'
structured_value=None
fallback_value=None
bot_message=None

from ner_v1.chatbot.entity_detection import get_text
output = get_text(message=message, entity_name=entity_name, structured_value=structured_value, fallback_value=fallback_value, bot_message=bot_message)
print output

message = 'my contact number is 9049961794'
entity_name = 'phone_number'
structured_value = None
fallback_value = None
bot_message = None
from ner_v1.chatbot.entity_detection import get_phone_number
output = get_phone_number(message=message,entity_name=entity_name,                   structured_value=structured_value,fallback_value=fallback_value,bot_message=bot_message)
print output
