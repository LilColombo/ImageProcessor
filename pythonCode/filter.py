def linearSpatialFilter_smoothen(img_map):
    import numpy as np

#     filter architecture
#       [1][2][1]    \
#       [2][4][2]    => (1/16)x 
#       [1][2][1]    /

    dimensions = img_map.shape
    height = dimensions[0]
    width = dimensions[1]
    constants = ((1/16),(2/16),(4/16))
    filter = np.array([[constants[0], constants[1], constants[0]],
                       [constants[1], constants[2], constants[1]],
                       [constants[0], constants[1], constants[0]]])
    img_map_smooth = np.copy(img_map)
    for j in range(1,height-1): #remember: (y,x)
        for i in range(1,width-1):
            filteredSum = 0     

            uvGlobal = [ [i-1,i,i+1] , [j-1, j, j+1]  ]
            for v in range(3):
                for u in range(3):
                    x = uvGlobal[0][u]
                    y = uvGlobal[1][v]
                              # for u,v -> filtered_map[t,s (t,s = 0->2)] = uv[t,s = (0->2) ] * img_map[v,u]
                    filteredSum += filter[v,u] * img_map[y,x]   

        img_map_smooth[j,i] = filteredSum                                     #filtered_map [t,s] = u[] * img_map[j-1,i-1] 
        #take filteredsum and put it into img_map_smooth[j,i]
    return img_map_smooth


                    