def solution(genres, plays):
    answer = []
    music_genres=dict()
    genres_plays=dict()
    for i in range(len(genres)):
        if music_genres.get(genres[i]):
            genres_plays[genres[i]]+=plays[i]
            music_genres[genres[i]].append((i,plays[i]))
        else:
            genres_plays[genres[i]]=plays[i]
            music_genres[genres[i]]=[(i,plays[i])]
                                           
    plays_genres=dict()
    for gp in genres_plays.keys():
        plays_genres[genres_plays[gp]]=gp
    
    play_count=list(plays_genres.keys())
    play_count.sort(key=lambda x:-x)
    for pc in play_count:
        target_genres=music_genres[plays_genres[pc]]
        target_genres.sort(key=lambda x:-x[1])
        if len(target_genres)>1:
            for i in range(2):
                answer.append(target_genres[i][0])
        else:
            answer.append(target_genres[0][0])
    return answer