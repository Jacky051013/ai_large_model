import math
import numpy as np
import pandas as pd

from rag_content import RagContent


def calculate_rank(q_vector, a_vector_list):
    arr_q = np.array(q_vector)
    arr_q_col = arr_q.reshape(arr_q.size, 1)
    arr_a = np.array(a_vector_list)
    arr_sum_dot = np.dot(arr_a, arr_q)
    len_mod_q = np.linalg.norm(arr_q)
    len_mod_a = np.linalg.norm(arr_a, axis=1)
    denominator = len_mod_q * len_mod_a
    denominator[denominator == 0] = 1e-10
    cos_similarities = arr_sum_dot / denominator

    sorted_indices = np.argsort(cos_similarities)[::-1]
    top5_indices = sorted_indices[:5].tolist()
    top5_scores = cos_similarities[sorted_indices[:5]].tolist()

    return top5_indices, top5_scores


def calculate_ragcontent_rank(query_vec: list, rag_contents: list[RagContent]):
    doc_vectors = [rc.vec for rc in rag_contents]
    top5_indices, top5_scores = calculate_rank(query_vec, doc_vectors)
    top5_rag_contents = []
    for idx, score in zip(top5_indices, top5_scores):
        rag_contents[idx].vec_score = score
        top5_rag_contents.append(rag_contents[idx])

    return top5_rag_contents

# q_2d = [1, 2]
# a_list_2d = [[1.1, 2.1], [0.9, 1.9], [3, 4]]
# top5_2d, score_2d = calculate_rank(q_2d, a_list_2d)
# print("2维向量测试结果：", score_2d)




#     calculated_vector = []
#     for a_vector in a_vector_list:
#         cos_sum = 0
#         len_mod_q = 0
#         len_mod_a = 0
#         for i in range(0, len(a_vector)):
#             cos_sum += q_vector[i] * a_vector[i]
#             len_mod_q += q_vector[i]**2
#             len_mod_a += a_vector[i]**2
#         magnitude_q = math.sqrt(len_mod_q)
#         magnitude_a = math.sqrt(len_mod_a)
#         cos_theta = cos_sum / (magnitude_q*magnitude_a)
#         angle_rad = math.acos(cos_theta)
#         angle_deg = math.degrees(angle_rad)
#         calculated_vector.append(angle_deg)
#
#     rank = sorted(calculated_vector)
#     final_list = []
#     for j in range(min(5, len(rank))):
#         final_list.append(rank[j])
#
#     return final_list
#
# print(calculate_rank([-1,1],[[-0.5,0.5],[0.02, -0.02]]))
