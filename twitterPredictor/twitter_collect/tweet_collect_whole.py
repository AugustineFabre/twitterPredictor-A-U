import os
print(os.path.abspath(os.curdir))


#def get_candidate_queries(num_candidate, file_path):

def get_candidate_queries():
    final_0 = []
    final_1 = []
    try:
        with open("../CandidateData/hashtag_candidate_0.txt", "r") as hashtag:
            for line in hashtag.readlines():
                line = line.strip('\n')
                final_0.append(line)

        with open("../CandidateData/keywords_candidate_0.txt", "r") as keywords:
            for line1 in keywords.readlines():
                line1 = line1.strip('\n')
                final_0.append(line1)

        for element in final_0:
            print(element)

        with open("../CandidateData/hashtag_candidate_1.txt", "r") as hashtag:
            for line in hashtag.readlines():
                line = line.strip('\n')
                final_1.append(line)

        with open("../CandidateData/keywords_candidate_1.txt", "r") as keywords:
            for line1 in keywords.readlines():
                line1 = line1.strip('\n')
                final_1.append(line1)

        for element in final_1:
            print(element)

    except IOError:
        print('No such file or path')

    return [final_0,final_1]



a = get_candidate_queries()
print (a)