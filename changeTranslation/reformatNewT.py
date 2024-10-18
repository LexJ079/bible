# Mapping of book abbreviations to full names, short abbreviations, and book numbers
book_mapping = {
    'MAT': ('Matthew', 'Mt', 51),
    'MAR': ('Mark', 'Mk', 52),
    'LUK': ('Luke', 'Lk', 53),
    'JOH': ('John', 'Jn', 54),
    'ACT': ('Acts', 'Acts', 55),
    'ROM': ('Romans', 'Rom', 56),
    '1CO': ('1 Corinthians', '1Co', 57),
    '2CO': ('2 Corinthians', '2Co', 58),
    'GAL': ('Galatians', 'Gal', 59),
    'EPH': ('Ephesians', 'Eph', 60),
    'PHI': ('Philipians', 'Php', 61),
    'COL': ('Colossians', 'Col', 62),
    '1TH': ('1 Thessalonians', '1Th', 63),
    '2TH': ('2 Thessalonians', '2Th', 64),
    '1TI': ('1 Timothy', '1Ti', 65),
    '2TI': ('2 Timothy', '2Ti', 66),
    'TIT': ('Titus', 'Tts', 67),
    'PHM': ('Philemon', 'Phm', 68),
    'HEB': ('Hebrews', 'Heb', 69),
    'JAM': ('James', 'Jam', 70),
    '1PE': ('1 Peter', '1Pt', 71),
    '2PE': ('2 Peter', '2Pt', 72),
    '1JO': ('1 John', '1Jn', 73),
    '2JO': ('2 John', '2Jn', 74),
    '3JO': ('3 John', '3Jn', 75),
    'JUD': ('Jude', 'Jude', 76),
    'REV': ('Revelation', 'Rev', 77),
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
with open('NewT.txt', 'r') as new_file, open('reformatted_NewTtranslation.txt', 'w') as old_format_file:
    for line in new_file:
        formatted_line = reformat_line(line.strip())
        if formatted_line:
            old_format_file.write(formatted_line + "\n")

print("Reformatting complete!")

