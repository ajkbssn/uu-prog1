
import time

# A poem by Edgar Allan Poe

poem = """It was many and many a year ago,
   In a kingdom by the sea,
That a maiden there lived whom you may know
   By the name of Annabel Lee;
And this maiden she lived with no other thought
   Than to love and be loved by me.

I was a child and she was a child,
   In this kingdom by the sea,
But we loved with a love that was more than love—
   I and my Annabel Lee—
With a love that the wingèd seraphs of Heaven
   Coveted her and me.

And this was the reason that, long ago,
   In this kingdom by the sea,
A wind blew out of a cloud, chilling
   My beautiful Annabel Lee;
So that her highborn kinsmen came
   And bore her away from me,
To shut her up in a sepulchre
   In this kingdom by the sea.

The angels, not half so happy in Heaven,
   Went envying her and me—
Yes!—that was the reason (as all men know,
   In this kingdom by the sea)
That the wind came out of the cloud by night,
   Chilling and killing my Annabel Lee.

But our love it was stronger by far than the love
   Of those who were older than we—
   Of many far wiser than we—
And neither the angels in Heaven above
   Nor the demons down under the sea
Can ever dissever my soul from the soul
   Of the beautiful Annabel Lee;

For the moon never beams, without bringing me dreams
   Of the beautiful Annabel Lee;
And the stars never rise, but I feel the bright eyes
   Of the beautiful Annabel Lee;
And so, all the night-tide, I lie down by the side
   Of my darling—my darling—my life and my bride,
   In her sepulchre there by the sea—
   In her tomb by the sounding sea."""

def get_and_clean_lines(p):
    # Extract all lines into separate strings
    lines = p.split('\n')

    # Remove all beginning and trailing white-space
    lines = [line.strip() for line in lines if len(line.strip()) > 0]

    return lines

def part1():

    print(f'Length of poem in characters: {len(poem)}')

    # Split up the poem:

    list_of_lines = get_and_clean_lines(poem)

    # Put it back into one string

    poem_single_string = ' '.join(list_of_lines) # ', '.join(['a', 'b', 'c']) -> 'a, b, c'

    print(poem_single_string)

    time.sleep(5)

    # how many occurrences of annabel lee?

    name_count = poem_single_string.count('Annabel Lee')

    print(f'Annabel Lee occurred {name_count} times.')

    sea_count = poem_single_string.count('sea')

    print(f'sea occurred {sea_count} times.')

    time.sleep(5)

def mark_lines_with_word(list_of_lines, word, found_marker, not_found_marker):
    for i in range(len(list_of_lines)):
        # We could use find, or index with error handling, but since we don't care about where it is...
        line_num_string = f'[{i+1:02d}]'

        if word in list_of_lines[i]:
            list_of_lines[i] = line_num_string + found_marker + list_of_lines[i]
        else:
            list_of_lines[i] = line_num_string + not_found_marker + list_of_lines[i]

def part2():
    # Split up the poem:

    list_of_lines = get_and_clean_lines(poem)
    
    list_of_lines_marked = list_of_lines.copy()

    mark_lines_with_word(list_of_lines_marked, 'Annabel Lee', '*****', '     ')

    for line in list_of_lines_marked:
        print(line)
        time.sleep(0.3)
#marked_poem = '\n'.join(list_of_lines_marked)

#print(marked_poem)

def part3():
    def count_verses(p):
        lines = p.split('\n')
        print(lines)
        
        empty_line_count = 1
    
        for i in range(len(lines)):
            if len(lines[i].strip()) == 0:
                empty_line_count += 1
        return empty_line_count

    print(f'Verse count is {count_verses(poem)}.')


#print(poem)
#part1()
#part2()
part3()
