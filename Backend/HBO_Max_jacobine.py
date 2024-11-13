import pandas as pd 
from json import loads, dumps

def start():
    file_path = "HBO_Max.csv"
    df_hbo_max = pd.read_csv(file_path)
    df_hbo_max = df_hbo_max.head()
    result = df_hbo_max.to_json(orient = "records")
    parsed = loads(result)
    # print(df_hbo_max)

    mean_num_votes = df_hbo_max['imdbNumVotes'].mean()
    median_num_votes = df_hbo_max['imdbNumVotes'].median()
    std_num_votes = df_hbo_max['imdbNumVotes'].std()

    json_res_num_votes = {
            'mean_num_votes': mean_num_votes,
            'median_num_votes': median_num_votes,
            'std_num_votes': std_num_votes
        }
    mean_rating = df_hbo_max['imdbAverageRating'].mean()
    median_rating = df_hbo_max['imdbAverageRating'].median()
    std_rating = df_hbo_max['imdbAverageRating'].std()

    json_res_rating = {
            'mean_average_rating' : mean_rating,
            'median_average_rating' : median_rating,
            'std_average_rating' : std_rating
        }
    
    correlatie_rating_votes = df_hbo_max[["imdbAverageRating", "imdbNumVotes"]]
    correlatie = correlatie_rating_votes.corr()
    json_res_correlatie = {
        "correlatie_between_rating_votes": correlatie.to_json()
    }
    return parsed, json_res_num_votes, json_res_rating, json_res_correlatie
