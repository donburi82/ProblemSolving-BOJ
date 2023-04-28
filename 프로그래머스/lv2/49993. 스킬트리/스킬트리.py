def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        s = "".join([c for c in skill_tree if c in skill])
        if s==skill[:len(s)]:
            count += 1
    return count