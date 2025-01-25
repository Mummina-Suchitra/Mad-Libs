def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input
noun1 = get_input("noun")
adjective1 = get_input("adjective")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f""" 
Once up on a time there was a {adjective1}{noun1} who loved to {verb1} all day long.
One day, {noun2} walked into the room and caught the {noun1} in the act.b

{noun2}: "What are you doing?"
{noun1}: "I'm just {verb1}ing, what's the bigdeal?"
{noun2}: "well, it's not every day that you see a {noun1}{verb1}ing, in the middle of the day."
{noun1}: "I guess you're right, maybe i should take a break."
{noun2}: "That's probably a good idea,why don't we go {verb2} instead?"
{noun1}: "sure,that sounds like fun!"
and so, {noun2} and the {noun1} went off to {verb2} and had a great time"""

print(story)

