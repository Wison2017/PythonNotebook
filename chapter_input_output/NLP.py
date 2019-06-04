import re
SIZE = 100
def parse_to_word_list(text, last_word, word_list):
    text = re.sub(r'[^\w]', ' ', text)
    text = text.lower()
    cur_word_list = text.split(' ')
    cur_word_list, last_word = cur_word_list[:-1], cur_word_list[-1]
    word_list += filter(None, cur_word_list)
    return last_word

def solve():
    with open('file', 'r') as fin:
        word_list, last_word = [], ''
        while True:
            text = fin.read(SIZE)
            if not text:
                break
            last_word = parse_to_word_list(text, last_word, word_list)
        word_freq = {}
        for word in word_list:
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1
        sorted_word_freq = sorted(word_freq.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_word_freq
