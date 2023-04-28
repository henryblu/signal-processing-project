
def noise_reduction(fourier_transform, threadshold_level):
    '''this function performs a noise reduction on a given fourier transform depended 
    on the given threashold. It dosnt work yet

    Args:
        fourier_transform (np.array): the fourier transform to be noise reduced 
        threadshold_level (int): the level of the threadshold

    '''
    N = len(fourier_transform)
    for k in range(N):
        if abs(fourier_transform[k]) < threadshold_level:
            fourier_transform[k] = 0
    return fourier_transform
