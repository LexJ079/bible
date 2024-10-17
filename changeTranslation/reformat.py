# Mapping of book abbreviations to full names and short abbreviations
book_mapping = {
    'GEN': ('Genesis', 'Gn'),
    'EXO': ('Exodus', 'Ex'),
    'LEV': ('Leveticus', 'Lv'),
    'NUM': ('Numbers', 'Nm,'),
    'DEU': ('Deutoronomy', 'Dt'),
    'JOS': ('Joshua', 'Jos'),
    'JDG': ('Judges', 'Jdg'),
    'RUT': ('Ruth', 'Ru'),
    '1SA': ('1 Kingdoms', '1Kg'),
    '2SA': ('2 Kingdoms', '2Kg'),
    '1KI': ('3 Kingdoms', '3Kg'),
    '2KI': ('4 Kingdoms', '4Kg'),
    '1CH': ('1 Chronicles', '1Ch'),
    '2CH': ('2 Chronicles', '2Ch'),
    '1ES': ('1 Ezra', '1Ez'),
    'EZR': ('2 Ezra', '2Ez'),
    'NEH': ('Nehemia', 'Neh'),
    'TOB': ('Tobit', 'Tb'),
    'JDT': ('Judith', 'Jdt'),
    'EST': ('Esther', 'Est'),
    '1MA': ('1 Maccabees', '1Mc'),
    '2MA': ('2 Maccabees', '2Mc'),
    '3MA': ('3 Maccabees', '3Mc'),
    'PSA': ('Psalms', 'Ps'),
    'JOB': ('Job', 'Job'),
    'PRO': ('Proverbs', 'Pr'),
    'ECC': ('Ecclesiates', 'Ecc'),
    'SOL': ('Song of Songs', 'SS'),
    'WIS': ('Wisdom of Solomon', 'WSol'),
    'SIR': ('Wisdom of Siriach', 'WSir'),
    'HOS': ('Hosea', 'Hos'),
    'AMO': ('Amos', 'Am'),
    'MIC': ('Micah', 'Mic'),
    'JOE': ('Joel', 'Joel'),
    'OBA': ('Obadiah', 'Ob'),
    'JON': ('Jonah', 'Jon'),
    'NAH': ('Nahum', 'Nah'),
    'HAB': ('Habakkuk', 'Hab'),
    'ZEP': ('Zephaniah', 'Zep'),
    'HAG': ('Haggai', 'Hag'),
    'ZEC': ('Zecheriah', 'Zec'),
    'MAL': ('Malachai', 'Mal'),
    'ISA': ('Isaiah', 'Is'),
    'JER': ('Jeremiah', 'Jer'),
    'BAR': ('Baruch', 'Bar'),
    'LAM': ('Lamentations of Jeremiah', 'Lam'),
    'EPJ': ('Epistle of Jeremiah', 'EJer'),
    'EZE': ('Ezekiel', 'Ezk'),
    'DAN': ('Daniel', 'Dan'),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    # Add other books as necessary
}

def reformat_line(line):
    # Split line into its parts
    parts = line.split(" ", 2)  # Split into book_abbreviation, chapter:verse, and the verse text
    book_abbreviation = parts[0]
    chapter_verse = parts[1]
    verse_text = parts[2]
    
    # Extract chapter and verse from chapter_verse
    chapter, verse = chapter_verse.split(":")
    
    # Get the full book name and abbreviation
    full_book_name, short_abbreviation = book_mapping[book_abbreviation]
    
    # Format the line in the desired output format
    formatted_line = f"{full_book_name}\t{short_abbreviation}\t{chapter}\t{chapter}\t{verse}\t{verse_text}"
    return formatted_line

# Read the new translation file and write the reformatted output
with open('new_translation.txt', 'r') as new_file, open('reformatted_translation.txt', 'w') as old_format_file:
    for line in new_file:
        formatted_line = reformat_line(line.strip())
        old_format_file.write(formatted_line + "\n")

print("Reformatting complete!")

