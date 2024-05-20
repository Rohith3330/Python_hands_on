def read_notes():
  try:
    with open("notes.txt", "r") as notes_file:
      contents = notes_file.read()
      if contents:
        print(contents)
      else:
        print("No notes found.")
  except FileNotFoundError:
    print("The notes file does not exist yet.")

def write_note():
  """Prompts user for a new note and writes it to the file."""
  new_note = input("Enter your note: ")
  try:
    with open("notes.txt", "w") as notes_file:
      notes_file.write(new_note+'\n')
      print("Note written successfully.")
  except FileNotFoundError:
    print("An error occurred while writing the note.")

def append_note():
  """Prompts user for a note and appends it to the end of the file."""
  note_to_append = input("Enter a note to append: ")
  try:
    with open("notes.txt", "a") as notes_file:
      notes_file.write(note_to_append + "\n") 
      print("Note appended successfully.")
  except FileNotFoundError:
    print("An error occurred while appending the note.")

def main():
  """Main function to handle user input and call corresponding functions."""
  while True:
    print("\n1. Read Notes")
    print("2. Write a New Note")
    print("3. Append a Note")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      read_notes()
    elif choice == '2':
      write_note()
    elif choice == '3':
      append_note()
    elif choice == '4':
      print("Exiting the application.")
      break
    else:
      print("Incorrect input. Please choose a valid option.")

if __name__ == "__main__":
  main()
