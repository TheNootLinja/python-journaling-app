# User is able to write out a journal entry, which is written to a .txt file
# with the date and time that the entry was written at the top of each.

# Ask user what they would like to do.
# Options: New, View Old

# New allows user to write out an entry
print('Write a journal entry:' + "\n")
new_journal_title = input("What do you want to title this journal?")
new_journal_content = input()

f = open('journal.txt', "a")
f.write(
    new_journal_title + " - 02/05/2026 @ 12:26" + "\n" +
    new_journal_content + "\n\n"
)
f.close()
