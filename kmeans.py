import numpy as np

def converged(minimum, centroids):
    return ( set( [ tuple(a) for a in minimum ] ) == set( [ tuple(a) for a in centroids ] ) )


def cluster_points(X, minimum):
    clusters  = {}
    for x in X:
        best_key = min( [ ( i[0], np.linalg.norm( x - minimum[ i[0] ] ) ) \
                    for i in enumerate( minimum ) ], key=lambda t:t[1] )[0]
        try:
            clusters[best_key].append(x)
        except KeyError:
            clusters[best_key] = [x]
    return clusters

 
def reevaluate_centers(minimum, clusters):
    new_minimum = []
    keys = sorted(clusters.keys())
    for k in keys:
        new_minimum.append(np.mean(clusters[k], axis = 0))
    return new_minimum

 
def find_centers(X, K):
    centroids = random.sample(X, K)
    minimum = random.sample(X, K)
    while not converged(minimum, centroids):
        centroids = minimum
        
        clusters = cluster_points(X, minimum)

        minimum = reevaluate_centers(centroids, clusters)
    return(minimum, clusters)