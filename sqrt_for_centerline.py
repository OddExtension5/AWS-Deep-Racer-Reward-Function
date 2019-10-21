import math

def reward_function(params):
    
    '''
    Using sqaure root for the center line
    
    '''
    
    track_width = params['track_width']
    
    distance_from_center = params['distance_from_center']
    
    reward = 1 - math.sqrt(distance_from_center / (track_width/2))
    
    if reward < 0:
        reward = 0
    
    return float(reward)
