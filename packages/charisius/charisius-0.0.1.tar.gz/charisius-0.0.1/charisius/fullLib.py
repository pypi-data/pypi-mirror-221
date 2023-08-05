# coding: utf-8
###
 # @file fullLib.py
 # @author Serhan YILMAZ, John Stephan <srhnylmz14@gmail.com> <john.stephan@epfl.ch>
 #
 # @section LICENSE
 #
 # Copyright © 2023 École Polytechnique Fédérale de Lausanne (EPFL).
 # All rights reserved.
 #
###


import torch, random, math
from itertools import combinations

# SY: Below functions are the own work of Serhan YILMAZ. I, Serhan YILMAZ, at the time, was a Summer intern at DCL Lab, EPFL.

## SY: for geometric_median
def smoothed_weiszfeld_optimized(vectors, nu=0.1, T=3):
    n = len(vectors)
    z = torch.zeros_like(vectors[0])
    alphas = torch.tensor([1 / n] * n).to(vectors[0].device)
    
    vectors = torch.stack(vectors)
    
    for _ in range(T):
        distances = torch.norm(z - vectors, dim=-1)
        distances[distances != distances] = 0  # SY: Replace NaN values with 0
        
        betas = alphas / torch.clamp(distances, min=nu)
        betas[distances == float('inf')] = 0  # SY: Replace infinite values with 0

        z = torch.sum(betas[:, None] * vectors, dim=0) / betas.sum()
        
    return z



## SY: for krum and multikrum
def compute_distances(vectors):
    # SY: Compute all pairwise distances between vectors in a list

    if type(vectors) != torch.Tensor:
        vectors = torch.stack(vectors)
    distances = torch.cdist(vectors, vectors)

    # SY: set non-finite values to inf
    distances[~torch.isfinite(distances)] = float('inf')

    return distances

## SY: for krum
def get_vector_best_score(vectors, nb_byz, distances):
    # SY: Get the vector with the smallest score.
    if type(vectors) != torch.Tensor:
        vectors = torch.stack(vectors)
    n_vectors = vectors.size(0)
    min_score = torch.tensor(float('inf'))

    for worker_id in range(n_vectors):
        # SY: Create a mask for selecting all vectors except the current one
        mask = torch.ones(n_vectors, dtype=torch.bool)
        mask[worker_id] = 0

        # SY: Select all distances to the current vector
        distances_to_vector = distances[worker_id, mask]

        # SY: Square and sort the distances
        distances_squared_to_vector = distances_to_vector.pow(2).sort()[0]

        # SY: Compute the score
        score = distances_squared_to_vector[:n_vectors - nb_byz - 1].sum()

        # SY: Update min score and min index
        if score < min_score:
            min_score, min_index = score, worker_id

    # SY: Return the vector with smallest score
    return vectors[min_index]

## SY: for multikrum
def get_vector_scores(vectors, nb_byz, distances):
    if type(vectors) != torch.Tensor:
        vectors = torch.stack(vectors)
    n_vectors = vectors.size(0)

    scores = []
    for worker_id in range(n_vectors):
        # SY: Create a mask for selecting all vectors except the current one
        mask = torch.ones(n_vectors, dtype=torch.bool)
        mask[worker_id] = 0

        # SY: Select all distances to the current vector
        distances_to_vector = distances[worker_id, mask]

        # SY: Square and sort the distances
        distances_squared_to_vector = distances_to_vector.pow(2).sort()[0]

        # SY: Compute the score
        score = distances_squared_to_vector[:n_vectors - nb_byz - 1].sum()

        # SY: Save the score and worker id
        scores.append((score.item(), worker_id))

    # SY: Sort the scores in increasing order
    scores.sort(key=lambda x: x[0])

    return scores


def average_nearest_neighbors(vectors, f):
    distances = compute_distances(vectors)
    _, indices = torch.sort(distances, dim=1)

    # SY: Return the average of the n-f closest vectors to each vector
    closest_vectors = vectors[indices[:, :(vectors.size(0) - f)]]
    return closest_vectors.mean(dim=1)


def compute_closest_vectors_and_mean(vectors, nb_byz):
    # SY: Convert vectors from a list of 1D tensors to a 2D tensor
    vectors = torch.stack(vectors)
    
    pivot_vector = vectors[-1]
    
    # SY: Calculate distances using vectorized operations
    distances = torch.norm(vectors - pivot_vector, dim=1)
    
    # SY: Get the indices of the smallest n-f distances
    _, indices = torch.topk(distances, k=len(vectors) - nb_byz, largest=False)
    
    # SY: Use advanced indexing to select the closest vectors and compute their mean
    mean_closest_vectors = vectors[indices].mean(dim=0)
    
    return mean_closest_vectors


# SY: Below functions are inherited from misc.py, work of John Stephan:

#JS: Compute the subset of (n-f) gradients of minimum diameter 
def compute_min_diameter_subset(vectors, nb_byz):
    #JS: compute all pairwise distances
    distances = compute_distances(vectors)
    min_diameter = math.inf

    n = len(vectors)
    #JS: Get all subsets of size n - f
    all_subsets = list(combinations(range(n), n - nb_byz))
    for subset in all_subsets:
        subset_diameter = 0
        
        #JS: Compute diameter of subset
        for i, vector1 in enumerate(subset):
            for vector2 in subset[i+1:]:
                distance = distances.get((vector1, vector2), 0)
                subset_diameter = distance if distance > subset_diameter else subset_diameter
        
        #JS: Update min diameter (if needed)
        if min_diameter > subset_diameter:
            min_diameter = subset_diameter
            min_subset = subset

    return min_subset


#JS: Compute the subset (indices of vectors) of (n-f) vectors of minimum variance 
def compute_min_variance_subset(vectors, nb_byz):
    #JS: compute all pairwise distances
    distances = compute_distances(vectors)

    n = len(vectors)
    #JS: Get all subsets of size n - f
    all_subsets = list(combinations(range(n), n - nb_byz))
    min_variance = math.inf

    for subset in all_subsets:
        current_variance = 0
        #JS: Compute diameter of subset
        for i, vector1 in enumerate(subset):
            for vector2 in subset[i+1:]:
                distance = distances.get((vector1, vector2), 0)
                current_variance += distance**2
        
        if min_variance > current_variance:
            min_variance = current_variance
            min_subset = subset

    return min_subset


# SY: Old, not optimized functions - these functions were not considered in the optimization task as they are already optimized in PyTorch.
# SY: They are the work of John Stephan.


def average(_, vectors):
    return torch.stack(vectors).mean(dim=0)


def trmean(aggregator, vectors):
    if aggregator.nb_byz == 0:
        return torch.stack(vectors).mean(dim=0)
    return torch.stack(vectors).sort(dim=0).values[aggregator.nb_byz:-aggregator.nb_byz].mean(dim=0)


def median(_, vectors):
    return torch.stack(vectors).quantile(q=0.5, dim=0)
    #return torch.stack(vectors).median(dim=0)[0]


def pseudo_multi_krum(aggregator, vectors): ## SY: default pmk - not to be optimized, this is fine for now. later, optimization should be seeked with CUDA or C++

    k = len(vectors) - aggregator.nb_byz
    k_vectors = list()

    #JS: dictionary to hold pairwise distances
    distances = dict()
    indices = range(len(vectors))

    #JS: Run Pseudo Krum k times, and store result in list then average
    for _ in range(k):
        #JS: choose (f+1) vectors at random, and compute their pseudo-scores
        random_indices = random.sample(indices, aggregator.nb_byz + 1)
        #JS: compute the pseudo-scores of only these random vectors
        #JS: a pseudo-score is the same as a normal score, but computed only over a random set of (n-f) neighbors
        min_score = min_index = None

        for index in random_indices:
            #JS: vectors[index] is one of the candidates to be outputted by pseudo-Krum
            random_neighbors = random.sample(indices, k)
            score = 0
            for neighbor in random_neighbors:

                #JS: if index = neighbour, distance = 0 and score is unchanged
                if index == neighbor:
                    continue

                #JS: fetch the distance between vector and neighbor from dictionary (if found)
                #otherwise calculate it and store it in dictionary
                key = (min(index, neighbor), max(index, neighbor))

                if key in distances:
                    dist = distances[key]
                else:
                    dist = vectors[index].sub(vectors[neighbor]).norm().item()
                    distances[key] = dist

                score += dist**2

            if min_score is None or score < min_score:
                min_score = score
                min_index = index
        
        #JS: append the vector with the smallest score (among the considered f+1) to the list
        k_vectors.append(vectors[min_index])

    #JS: return the average of the k vectors
    result = torch.stack(k_vectors).mean(dim=0)

    return result


def minimum_diameter_averaging(aggregator, vectors):

    selected_subset = compute_min_diameter_subset(vectors, aggregator.nb_byz)
    selected_vectors = [vectors[j] for j in selected_subset]
    result = torch.stack(selected_vectors).mean(dim=0)
    
    return result

def minimum_variance_averaging(aggregator, vectors):

    selected_subset = compute_min_variance_subset(vectors, aggregator.nb_byz)
    selected_vectors = [vectors[j] for j in selected_subset]
    result = torch.stack(selected_vectors).mean(dim=0)

    return result


def meamed(aggregator, vectors): ## SY: default meamed, this cannot be optimized further with torch, as it's already using torch functions to the fullest. I've tried different implementations, but they're slower. A CUDA implementation shall be sought.

    vectors_stacked = torch.stack(vectors)
    median_vector = robust_aggregators["median"](aggregator, vectors)
    nb_workers, dimension = vectors_stacked.shape
    m = nb_workers - aggregator.nb_byz
    #JS: compute and aggregate (n-f) vectors closest to median (per dimension)
    bottom_indices = vectors_stacked.sub(median_vector).abs().topk(m, dim=0, largest=False, sorted=False).indices
    bottom_indices.mul_(dimension).add_(torch.arange(0, dimension, dtype=bottom_indices.dtype, device=bottom_indices.device))
    result = vectors_stacked.take(bottom_indices).mean(dim=0)

    return result


# SY: New functions - These are the functions that are greatly optimized with PyTorch. They show significant performance improvement ranging from 25% to 1100% faster function speed.
# SY: The computation in these functions are changed by PyTorch's own functions, the data type is also changed from mostly python dictionaries to 1D and 2D PyTorch tensors.
# SY: As the computation is now done with more efficient methods, more efficient algorithms and a more efficient data structure, the performance improvement is magnificent.
# SY: These functions are the work of mine, Serhan YILMAZ.


def geometric_median(_, vectors): ## SY: geometric median torch, fantastic optimization. Works great for both p2p and centralized. This is the default gm now.

    result = smoothed_weiszfeld_optimized(vectors) # SY: the function uses a smoothed weiszfeld algorithm, which is a gradient descent algorithm for geometric median

    return result


def krum(aggregator, vectors): ## SY: krum torch, fantastic optimization. Works great for both p2p and centralized. This is the default krum now.

    # SY: Compute all pairwise distances
    distances = compute_distances(vectors)
    # SY: return the vector with smallest score
    result = get_vector_best_score(vectors, aggregator.nb_byz, distances)

    return result

def multi_krum(aggregator, vectors): ## SY: multi_krum torch, fantastic optimization. Works great for both p2p and centralized. This is the default multi_krum now.

    k = len(vectors) - aggregator.nb_byz  # SY: k is the number of vectors to average in the end

    # SY: Compute all pairwise distances
    distances = compute_distances(vectors)

    # SY: Get scores of vectors, sorted in increasing order
    scores = get_vector_scores(vectors, aggregator.nb_byz, distances)

    # SY: Select the k vectors with the lowest scores
    best_vectors = [vectors[worker_id] for _, worker_id in scores[:k]]

    # SY: Return the average of the k vectors with lowest scores
    result = torch.stack(best_vectors).mean(dim=0)

    return result

def nearest_neighbor_mixing(aggregator, vectors, numb_iter=1):

    vectors = torch.stack(vectors)
    for _ in range(numb_iter):
        # SY: Replace every vector by the average of its nearest neighbors
        vectors = average_nearest_neighbors(vectors, aggregator.nb_byz)
    result = robust_aggregators[aggregator.second_aggregator](aggregator, vectors)

    return result

def bucketing(aggregator, vectors): ##SY: No computational optimization, just memory optimization. Computational complexity remains O(n), the same.

    random.shuffle(vectors)
    number_buckets = math.ceil(len(vectors) / aggregator.bucket_size)
    avg_vectors = []

    for i in range(number_buckets):
        start_index = i * aggregator.bucket_size
        end_index = min((i + 1) * aggregator.bucket_size, len(vectors))
        bucket = vectors[start_index:end_index]
        avg_vector = torch.stack(bucket).mean(dim=0)
        avg_vectors.append(avg_vector)

    result = robust_aggregators[aggregator.second_aggregator](aggregator, avg_vectors)


    return result

def centered_clipping(aggregator, vectors, L_iter=3, clip_thresh=1): ## SY: centered clipping, fantastic optimization. Works great for both p2p and centralized. This is the default cc now.

    v = aggregator.prev_momentum
    sum_distance = torch.zeros_like(vectors[0]) # SY: pre-allocate the tensor for summing
    for _ in range(L_iter):
        sum_distance.zero_() # SY: clear the previous sum
        num_vectors = 0
        for vector in vectors:
            distance = vector.sub(v) # SY: compute distance
            distance_norm = distance.norm().item()
            if distance_norm > clip_thresh:
                distance.mul_(clip_thresh / distance_norm) # SY: clip the distance
            sum_distance.add_(distance) # SY: add to the sum
            num_vectors += 1
        avg_dist = sum_distance.div(num_vectors)
        v.add_(avg_dist)
		
    return v

def MoNNA(aggregator, vectors): ## SY: greatly optimized MoNNA, works great for both p2p and centralized. This is the default MoNNA now.

    # SY: Compute n-f closest vectors to the pivot vector (i.e., the vector of the honest worker in question)
    # SY: Return the average of closest_vectors
    result = compute_closest_vectors_and_mean(vectors, aggregator.nb_byz)

    return result



# SY: Dictionary mapping every aggregator to its corresponding function
robust_aggregators = {"average": average,
                      "trmean": trmean,
                      "median": median,
                      "geometric_median": geometric_median,
                      "krum": krum,
                      "multi_krum": multi_krum,
                      "nnm": nearest_neighbor_mixing,
                      "bucketing": bucketing,
                      "pmk": pseudo_multi_krum,
                      "cc": centered_clipping,
                      "mda": minimum_diameter_averaging,
                      "mva": minimum_variance_averaging,
                      "MoNNA": MoNNA,
                      "meamed": meamed}

class RobustAggregator(object):

    def __init__(self, aggregator_name, second_aggregator, bucket_size, nb_byz, model_size, device):
        self.aggregator_name = aggregator_name
        self.second_aggregator = second_aggregator
        self.bucket_size = bucket_size
        self.nb_byz = nb_byz
        #JS; previous value of aggregated momentum, used for example for CC
        self.prev_momentum = torch.zeros(model_size, device=device)

    def aggregate(self, vectors):
        aggregate_vector = robust_aggregators[self.aggregator_name](self, vectors)
        #JS: Update the value of the previous momentum (e.g., for Centered Clipping aggregator)
        self.prev_momentum = aggregate_vector
        return aggregate_vector
    