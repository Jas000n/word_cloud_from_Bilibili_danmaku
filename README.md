# word_cloud_danmaku
use you-get and regular expression create word cloud for bilibili video

## To analyse what is discussed when watching this video
![](example.jpg)
## Installation
    git clone https://github.com/Jas000n/word_cloud_danmaku.git
    cd word_cloud_danmaku
    pip install -r requirements.txt
## Usage
    usage: main.py [-h]
               [-bgc BGC | -width WIDTH | -height HEIGHT | -max_font MAX_FONT | -max_word MAX_WORD | -min_font MIN_FONT | -color_state COLOR_STATE | -save_path SAVE_PATH]
               url

    analysing what is discussed when watching this video

    positional arguments:
        url                   url of the bilibili video

    optional arguments:
        -h, --help            show this help message and exit
        -bgc BGC              background color of the word cloud
        -width WIDTH          width of word cloud
        -height HEIGHT        height of the word cloud
        -max_font MAX_FONT    max font size
        -max_word MAX_WORD    max word in word cloud
        -min_font MIN_FONT    min font size
        -color_state COLOR_STATE    random color state
        -save_path SAVE_PATH  save generated image to path
    
    Plus, you can ban the words you wish not appear in the word cloud by adding them in ./stop_words.txt

## Example
    python main.py https://www.bilibili.com/video/BV1Tk4y1z7XV/?spm_id_from=333.337.search-card.all.click&vd_source=fb5bd6bc0dd83e5d85c6addb034de1db
you should get the danmaku word cloud picture of a cute cat video
