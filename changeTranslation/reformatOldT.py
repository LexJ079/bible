# Mapping of book abbreviations to full names, short abbreviations, and book numbers
book_mapping = {
    'GEN': ('Genesis', 'Gn', 1),
    'EXO': ('Exodus', 'Ex', 2),
    'LEV': ('Leviticus', 'Lv', 3),
    'NUM': ('Numbers', 'Nm', 4),
    'DEU': ('Deuteronomy', 'Dt', 5),
    'JOS': ('Joshua', 'Jos', 6),
    'JDG': ('Judges', 'Jdg', 7),
    'RUT': ('Ruth', 'Ru', 8),
    '1SA': ('1 Kingdoms', '1Kg', 9),
    '2SA': ('2 Kingdoms', '2Kg', 10),
    '1KI': ('3 Kingdoms', '3Kg', 11),
    '2KI': ('4 Kingdoms', '4Kg', 12),
    '1CH': ('1 Chronicles', '1Ch', 13),
    '2CH': ('2 Chronicles', '2Ch', 14),
    '1ES': ('1 Ezra', '1Ez', 15),
    'EZR': ('2 Ezra', '2Ez', 16),
    'NEH': ('Nehemiah', 'Neh', 17),
    'TOB': ('Tobit', 'Tb', 18),
    'JDT': ('Judith', 'Jdt', 19),
    'EST': ('Esther', 'Est', 20),
    '1MA': ('1 Maccabees', '1Mc', 21),
    '2MA': ('2 Maccabees', '2Mc', 22),
    '3MA': ('3 Maccabees', '3Mc', 23),
    '4MA': ('4 Maccabees', '4Mc', 24),  # Added 4 Maccabees
    'PSA': ('Psalms', 'Ps', 25),
    'JOB': ('Job', 'Job', 26),
    'PRO': ('Proverbs', 'Pr', 27),
    'ECC': ('Ecclesiastes', 'Ecc', 28),
    'SOL': ('Song of Songs', 'SS', 29),
    'WIS': ('Wisdom of Solomon', 'WSol', 30),
    'SIR': ('Wisdom of Sirach', 'WSir', 31),
    'HOS': ('Hosea', 'Hos', 32),
    'AMO': ('Amos', 'Am', 33),
    'MIC': ('Micah', 'Mic', 34),
    'JOE': ('Joel', 'Joel', 35),
    'OBA': ('Obadiah', 'Ob', 36),
    'JON': ('Jonah', 'Jon', 37),
    'NAH': ('Nahum', 'Nah', 38),
    'HAB': ('Habakkuk', 'Hab', 39),
    'ZEP': ('Zephaniah', 'Zep', 40),
    'HAG': ('Haggai', 'Hag', 41),
    'ZEC': ('Zechariah', 'Zec', 42),
    'MAL': ('Malachi', 'Mal', 43),
    'ISA': ('Isaiah', 'Is', 44),
    'JER': ('Jeremiah', 'Jer', 45),
    'BAR': ('Baruch', 'Bar', 46),
    'LAM': ('Lamentations of Jeremiah', 'Lam', 47),
    'EPJ': ('Epistle of Jeremiah', 'EJer', 48),
    'EZE': ('Ezekiel', 'Ezk', 49),
    'DAN': ('Daniel', 'Dan', 50),
    # Add other books as necessary
}

def reformat_line(line):
    # Split line into its parts
    parts = line.split(" ", 2)  # Split into book_abbreviation, chapter:verse, and the verse text

    # Check if the line is formatted correctly (has at least 3 parts)
    if len(parts) < 3:
        print(f"Skipping malformed line: {line}")
        return None

    book_abbreviation = parts[0]
    chapter_verse = parts[1]
    verse_text = parts[2]
    
    # Check if chapter_verse contains ':'
    if ':' not in chapter_verse:
        print(f"Skipping malformed chapter:verse: {chapter_verse}")
        return None

    # Extract chapter and verse from chapter_verse
    chapter, verse = chapter_verse.split(":")

    # Get the full book name, abbreviation, and book number, ensure the book abbreviation exists in the mapping
    if book_abbreviation not in book_mapping:
        print(f"Book abbreviation '{book_abbreviation}' not found in mapping.")
        return None

    full_book_name, short_abbreviation, book_number = book_mapping[book_abbreviation]

    # Format the line in the desired output format
    formatted_line = f"{full_book_name}\t{short_abbreviation}\t{book_number}\t{chapter}\t{verse}\t{verse_text}"
    return formatted_line

# Read the new translation file and write the reformatted output
with open('OldT.txt', 'r') as new_file, open('reformatted_translation.txt', 'w') as old_format_file:
    for line in new_file:
        formatted_line = reformat_line(line.strip())
        if formatted_line:
            old_format_file.write(formatted_line + "\n")

print("Reformatting complete!")

