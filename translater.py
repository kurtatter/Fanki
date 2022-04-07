from googletrans import Translator
import requests

# translate_file = open('translate1page.txt', 'w')
# translator = Translator()
url = 'https://translate.google.ru/translate_a/single?client=webapp&sl=auto&tl=en&hl=ru&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&dt=gt&otf=2&ssel=0&tsel=0&xid=45662847&kc=1&tk=656516.836633&q=dies%20ist%20ein%20test'

# with open('page1words.txt') as file:
#     for word in file:
#         blob = translator.translate(word.strip(), src='en', dest='ru')
#         translate_file.write(blob + '\n')
#
# translate_file.close()
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}
print(requests.get(url).text)
