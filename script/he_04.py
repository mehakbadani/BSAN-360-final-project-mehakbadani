# %% [markdown]
# # Hands-on Exercise 4: Conditionals & Loops
# 
# In this exercise, you will practice using **If statements**, **For loops**, and **While loops**.
# 
# **Important:** 
# * Follow the instructions in the `README.md` file carefully.
# * Do not change the variable names provided in the starter code (e.g., `ages`, `age_messages`, `count_people`), as the autograder relies on them.
# * **Note on `pass`:** The keyword `pass` in the starter code is just a placeholder to prevent errors before you add your code. You can delete it when you write your solution.

# %%
# Part 1: If Statements

# --- PRE-DEFINED MESSAGES ---
# Use these variables in your functions to avoid typos!
msg_old = "You're old!"
msg_not_old = "You're not that old."
msg_young = "You're so young!"
msg_middle = "You're not getting any younger."

# 1. Create a list called 'ages' with the specific numbers mentioned in the instructions

ages = [25, 48, 56, 50, 16]


# %%
# 2. Write the function 'old'
def oldOrNot(age):
    if age > 50:
        print(msg_old)
        return msg_old
    else:
        print(msg_not_old)
        return msg_not_old

old(ages[1])
old(ages[2])
old(ages[3])

# 3. Test the function with numbers from the list
def oldOrNot(age):
    if age > 50:
        print(msg_old)
        return msg_old
    else:
        print(msg_not_old)
        return msg_not_old

# Test oldOrNot
oldOrNot(ages[1])
oldOrNot(ages[2])
oldOrNot(ages[3])


# %%
# 4. Write the function 'oldOrNot'
def youngOrOld(age):
    if age < 30:
        print(msg_young)
        return msg_young
    elif age > 50:
        print(msg_old)
        return msg_old
    else:
        print(msg_middle)
        return msg_middle
        
# Test youngOrOld
youngOrOld(ages[1])
youngOrOld(ages[2])
youngOrOld(ages[3])

# 5. Test the function
def youngOrOld(age):
    if age < 30:
        print(msg_young)
        return msg_young
    elif age > 50:
        print(msg_old)
        return msg_old
    else:
        print(msg_middle)
        return msg_middle

youngOrOld(ages[1])
youngOrOld(ages[2])
youngOrOld(ages[3])


# %%
# 6. Write the function 'youngOrOld'
def youngOrOld(age):
    # Hint: Use msg_young, msg_old, and msg_middle
    # (Write your code here and remove 'pass')
 oldOrNot(ages[1])
oldOrNot(ages[2])
oldOrNot(ages[3])

# 7. Test the function
def youngOrOld(age):
    if age < 30:
        print(msg_young)
        return msg_young
    elif age > 50:
        print(msg_old)
        return msg_old
    else:
        print(msg_middle)
        return msg_middle

youngOrOld(ages[1])
youngOrOld(ages[2])
youngOrOld(ages[3])


# %%
# Part 2: For Loops

# Initialize the list to store results
age_messages = []

# Write your loop here to populate 'age_messages'
for age in ages:
    result = youngOrOld(age)
    age_messages.append(result)



# %%
# Part 3: While Loops

# 1. Loop that prints ages until a teenager is found
i = 0

while ages[i] >= 20:
    print(ages[i])
    i += 1



# 2. Loop that counts the people (save the count in 'count_people')
count_people = 0
count_people = 0
i = 0

while ages[i] >= 20:
    count_people += 1
    i += 1



# Print the final count
print(count_people)


