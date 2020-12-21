# adding names to the guest list
guest_list = ["beethoven" , "mozart" , "albinoni"]
print (f"You, {guest_list[0].title()}, are herewith invited to dinner at 20H.")
print (f"You, {guest_list[1].title()}, are herewith invited to dinner at 20H.")
print (f"You, {guest_list[2].title()}, are herewith invited to dinner at 20H.")
print (f"{guest_list[2].title()} cannot make it for the dinner this evening.")

guest_unable = guest_list[2]
print (guest_unable)

guest_list.remove(guest_unable)
print (guest_list)

guest_list.insert(2, "scarlatti")
print (guest_list)
print (f"You, {guest_list[2].title()}, are herewith invited to dinner at 20H")

# using insert to add names to the guest list at various indices on the list
print (f"Dear, {guest_list}, I have managed to find a bigger table!")
guest_list.insert(0, "Dimitri")
guest_list.insert(2, "haydn")
guest_list.append("Ravel")
print (guest_list)

print (
  f"Dear, {guest_list}, \n\tit is unfortunate, but the dinner table will not arrive for two weeks \n\tand I just have space for two people."
  )

# using .pop to take off names from the list
guest_taken_off_1 = guest_list.pop(4)
print (f"Dear, {guest_taken_off_1.title()}, please do not come to dinner")

guest_taken_off_2 = guest_list.pop()
print (f"Dear {guest_taken_off_2} please do not come to the party.")

print (guest_list)

# using .pop to make use of the variable in a print call
guest_taken_off_3 = guest_list.pop()
print (f"I am sorry {guest_taken_off_3.title()}, but you will not be able to attend.")
print (guest_list)
guest_taken_off_4 = guest_list.pop()
print (guest_list)

# using del to take off the remainder of names from the list
del guest_list[1]
print (guest_list)
del guest_list [0]
print (guest_list)
