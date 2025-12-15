import random

random.seed(30)

def indel_sites(sequence, indel_store=None, max_indels=20):
    if indel_store is None:
        indel_store = {}

    counter_indels = 0
    original_seq = sequence
    offset = 0  # net length change so far, used to track mutated coordinates

    events = []  # temporary list of coordinate 

    while counter_indels < max_indels:
        if len(original_seq) == 0:
            raise Exception("Sorry, sequence is too short")

        j = random.randint(10, 20)
        if j >= len(original_seq):
            continue

        i = random.randint(0, len(original_seq) - j)

        if original_seq[i] in ('G', 'T'):
            original_segment = original_seq[i]
            post_mod_segment = ''.join(random.choices('ACTG', k=j))
        else:
            original_segment = original_seq[i:i+j]
            post_mod_segment = ""

        events.append((i, original_segment, post_mod_segment))
        counter_indels += 1

    # Sort by original coordinate so offset is accumulated correctly
    events.sort(key=lambda x: x[0])

    new_seq = original_seq
    offset = 0

    # 2. Apply indels in original order and record *mutated* coordinates
    for i, original_segment, post_mod_segment in events:
        # length change
        delta = len(post_mod_segment) - len(str(original_segment))

        # position in current mutated string
        mut_i = i + offset

        # apply to new_seq
        j = len(original_segment)
        new_seq = new_seq[:mut_i] + post_mod_segment + new_seq[mut_i + j:]

        # store under mutated coordinate
        indel_store[mut_i] = (original_segment, post_mod_segment)

        # update offset for downstream sites
        offset += delta

    return new_seq, indel_store