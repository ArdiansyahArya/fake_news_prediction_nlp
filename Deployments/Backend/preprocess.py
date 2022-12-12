# Import libraries

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stopwd = list(set(stopwords.words('english')))
stopwd.append('u')
stopwd.append('s')
stopwd

def text_proses(text):
  # Mengubah text ke Lowercase agar semua data seragam
  text = text.lower()
  
  # Menghilangkan @/Mention karena pada berita palsu ada mention akun twitter
  text = re.sub("@[A-Za-z0-9_]+", " ", text)
  
  # Menghilangkan #/Hashtag untuk mengantisipasi karena berita palsu mengambil dari twitter
  text = re.sub("#[A-Za-z0-9_]+", " ", text)
  
  # Menghilangkan \n untuk antisipasi
  text = re.sub(r"\\n", " ",text)
  
  # Menghilangkan Whitespace untuk antisipasi
  text = text.strip()

  # Menghilangkan Link dikarenakan berita palsu terdapat link ke artikel lain
  text = re.sub(r"http\S+", " ", text)
  text = re.sub(r"www.\S+", " ", text)

  # Menghilangkan yang Bukan Huruf seperti Emoji, Simbol Matematika (seperti μ), dst untuk antisipasi
  text = re.sub("[^A-Za-z\s']", " ", text)

  # Melakukan Tokenisasi
  tokens = word_tokenize(text)

  # Menghilangkan Stopwords
  text = ' '.join([word for word in tokens if word not in stopwd])
  
  wordnet = WordNetLemmatizer()
  text = wordnet.lemmatize(text)
  

  return text