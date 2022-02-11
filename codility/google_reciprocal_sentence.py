# I Love Lance & Janice
# =====================

# You've caught two of your fellow minions passing coded notes back and forth - while they're on duty, no less! Worse, you're pretty sure it's not job-related - they're both huge fans of the space soap opera "Lance & Janice". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it'll put you that much closer to a promotion. 

# Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word "vmxibkgrlm", when decoded, would become "encryption".

# Write a function called answer(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about "Lance & Janice" instead of doing their jobs.


# Inputs:
#     (string) s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
# Output:
#     (string) "did you see last night's episode?"

# Inputs:
#     (string) s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
# Output:
#     (string) "Yeah! I can't believe Lance lost his job at the colony!!"



def solution(x):
    norm = [i for i in range(97, 123)]
    rev = [j for j in range(122, 96, -1)]
    ls = {norm[n]: rev[n] for n in range(len(norm))}
    dec = []
    for c in x:
        if ls.has_key(ord(c)):
            dec.append(chr(ls[ord(c)]))
        else:
            dec.append(c)
    return ''.join(dec)

