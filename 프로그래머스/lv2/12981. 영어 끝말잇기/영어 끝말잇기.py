def solution(n, words):
    used = [words[0]]
    players = {}
    players[0] = [ words[0] ]
    # player 1: 0, 5, ...
    # player 2: 1, 6, ...
    start = words[0][-1]
    for i in range(1, len(words)):
        word = words[i]
        if word[0]==start and word not in used and len(word)>1:
            # continue
            used.append(word)
            if i%n in players:
                players[i%n].append(word)
            else:
                players[i%n] = [ word ]
            start = word[-1]
        else:
            # 탈락
            if i%n in players:
                return [i%n+1, len(players[i%n])+1]
            else:
                return [i%n+1, 1]

    return [0, 0]