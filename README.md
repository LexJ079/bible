# bible

Terminal powered Bible

Forked from (https://github.com/LukeSmithxyz/kjv), with the Apocrypha. This uses the Brenton's English Septuagint 2012 Edition for the old testament, And the Byzantine Text for the new testament. These translations are in the public domain.


## Usage

    usage: ./bible [flags] [reference...]

      -l      list books
      -W      no line wrap
      -h      show help

      Reference types:
          <Book>
              Individual book
          <Book>:<Chapter>
              Individual chapter of a book
          <Book>:<Chapter>:<Verse>[,<Verse>]...
              Individual verse(s) of a specific chapter of a book
          <Book>:<Chapter>-<Chapter>
              Range of chapters in a book
          <Book>:<Chapter>:<Verse>-<Verse>
              Range of verses in a book chapter
          <Book>:<Chapter>:<Verse>-<Chapter>:<Verse>
              Range of chapters and verses in a book

          /<Search>
              All verses that match a pattern
          <Book>/<Search>
              All verses in a book that match a pattern
          <Book>:<Chapter>/<Search>
              All verses in a chapter of a book that match a pattern

## Build

bible can be built by cloning the repository and then running make:

    git clone https://github.com/LexJ079/bible.git
    cd bible
    sudo make install

## License

Public domain
