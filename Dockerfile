FROM python
WORKDIR  /cloud
COPY . /cloud
RUN pip install numpy nltk
RUN python -m nltk.downloader stopwords punkt
ENV NLTK_DATA=/usr/local/share/nltk_data
RUN python -m nltk.downloader stopwords punkt
COPY paragraphs.txt /cloud/paragraphs.txt
CMD ["python3","Pythoncode.py"]