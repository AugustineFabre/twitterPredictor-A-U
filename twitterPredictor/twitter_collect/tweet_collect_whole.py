def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        Keywords=open(file_path.keywords_candidate_num_candidate.txt)
        Hashtag=open(file_path.hastag_candidate_num_candidate.txt)
        liste=Keywords.spilt("\n")+Hashtag.split("\n") # liste contient les mots clés et les hashtag du candidat demandé
        return liste
    except IOError:
        return " Dossier vide"

def pytest():
    if len(get_candidate_queries(0,candidatedata)==16:
        return " La fonction est bien executée"
     else:
        return "echec"



