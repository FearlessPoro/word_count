import sys
import re


def wc():
    word_flag = 0
    line_flag = 0
    character_flag = 0
    empty_flag = 1
    character_count = 0
    word_count = 0
    line_count = 0
    previous_character = "x"

    if len(sys.argv) == 2:
        word_flag = 1
        start_index = 1
    elif len(sys.argv) > 2:
        flag_string = sys.argv[1]
        if re.match(r'^-.*', flag_string):
            if re.match(r'^-[mlw]{1,3}$', flag_string):
                if re.match(r'^-.*m.*', flag_string):
                    character_flag = 1
                if re.match(r'^-.*l.*', flag_string):
                    line_flag = 1
                if re.match(r'^-.*w.*', flag_string):
                    word_flag = 1
                start_index = 2
            else:
                print("invalid flags, quiting program")
                print("hint: use -[flags], where [flags] is any combination of 1 to 3 letters from this set: [m,l,w]")
                return
        else:
            start_index = 1
            word_flag = 1

    else:
        print("need a file as a first command line argument, or flags then files")
        return
    for i in range(start_index, len(sys.argv)):
        file_name = sys.argv[i]
        try:
            f = open(file_name)
        except IOError:
            print("Invalid file name:", file_name, "at argument:", i)
            return
        line = f.readline()
        while line:
            line_count += 1
            for character in line:
                if empty_flag and not character.isspace():
                    empty_flag = 0
                    word_count = 1
                character_count += 1
                if not character.isspace() and previous_character.isspace():
                    word_count += 1
                previous_character = character
            line = f.readline()

    print("summary of all files:")
    if character_flag:
        print("# of characters:", character_count)
    if word_flag:
        print("# of words:", word_count)
    if line_flag:
        print("# of lines:", line_count)


wc()
