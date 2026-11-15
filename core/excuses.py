import random

from distro import name

SUBJECTS = ["My cat", "My wifi", "My landlord", "The group chat"]
ACTIONS = {
    "chill": ["lowkey ghosted me", "was acting sus"],
    "dramatic": ["literally fumbled the whole morning", "went full NPC mode"],
    "unhinged": ["got possessed by a rizz demon", "ate my alarm, no cap"],
}
ENDINGS = ["so I'm cooked fr.", "it's giving chaos.", "ngl I'm not okay."]

used = {}  # user_id -> alasan yang sudah dipakai

def make_excuse(userid, chaos=1):
    level = ["chill", "dramatic", "unhinged"][min(chaos, 2)]
    for _ in range(20):
        e = f"{random.choice(SUBJECTS)} {random.choice(ACTIONS[level])}, {random.choice(ENDINGS)}"
        if e not in used.setdefault(userid, set()):
            used[userid].add(e)
            return e
    return "I'm out of excuses, no cap."

if name == "main":
    print(make_excuse(user_id=1, chaos=2))