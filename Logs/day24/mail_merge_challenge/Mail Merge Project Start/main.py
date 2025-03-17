PLACEHOLDER = "[name]"


with open(r"D:\0000\100 days\Logs\day24\mail_merge_challenge\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:

    names = names_file.readlines()

print(names)



with open(r"D:\0000\100 days\Logs\day24\mail_merge_challenge\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()


    for name in names :
      stripped_name = name.strip()
      new_letter =  letter_contents.replace(PLACEHOLDER , stripped_name)
      print(new_letter)

      with open(f"Logs\day24\mail_merge_challenge\Mail Merge Project Start\Output\ReadyToSend\letter_for_send{stripped_name}.txt",mode="w") as completed_letter:
         completed_letter.write(new_letter)
        
         


