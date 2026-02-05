# User is able to write out a journal entry, which is written to a .txt file
# with the date and time that the entry was written at the top of each.

# Ask user what they would like to do.
# Options: New, View Old

# New allows user to write out an entry

import datetime

still_writing = True
print('Write a journal entry:' + "\n")
new_journal_title = input("What do you want to title this journal?")
new_journal_content = ""
while still_writing:
    next_line = input()
    if next_line == "done":
        still_writing = False
    else:
        new_journal_content += "\n" + next_line

f = open('journal.txt', "a")
f.write(
    new_journal_title + " - " + str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")) + "\n" +
    new_journal_content + "\n\n=======================\n\n"
)
f.close()
