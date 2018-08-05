# ##### BEGIN MIT LICENSE BLOCK #####
# MIT License
# 
# Copyright (c) 2018 Insma Software
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ##### END MIT LICENSE BLOCK #####

# ----------------------------------------------------------
# Author: Maciej Klemarczyk (mklemarczyk)
# ----------------------------------------------------------

# --------------------------------------------------------------------
# Circle profile vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_circle_profile():
    veritces = [(1.0, 0.0, 0.0)]
    edges = []
    return edges, vertices

# --------------------------------------------------------------------
# Plate vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_plate_profile():
    veritces = [(0.0765, 0.0000, 0.0000),(0.0969, 0.0000, 0.0200),(0.0106, -0.0000, 0.0096),(0.0872, 0.0000, 0.0130),(0.0958, 0.0000, 0.0192),(0.0750, 0.0000, 0.0000),(0.0750, 0.0000, 0.0014),(0.0076, 0.0000, 0.0014),(0.0766, 0.0000, 0.0013),(0.0968, 0.0000, 0.0190),(0.0820, 0.0000, 0.0096),(0.0739, 0.0000, 0.0014)]
    edges = [(8,0),(10,3),(1,4),(4,3),(0,5),(5,6),(6,11),(9,8),(1,9),(2,10),(11,7)]
    return edges, vertices

# --------------------------------------------------------------------
# Dinner plate vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_dinner_plate_profile():
    veritces = [(0.0103, -0.0000, 0.0030),(0.0103, -0.0000, 0.0060),(0.1250, -0.0000, 0.0200),(0.0902, -0.0000, 0.0030),(0.1221, -0.0000, 0.0200),(0.1250, -0.0000, 0.0180),(0.0949, -0.0000, 0.0060),(0.0943, -0.0000, 0.0000),(0.0963, -0.0000, 0.0000),(0.0903, -0.0000, 0.0060),(0.0927, -0.0000, 0.0030)]
    edges = [(10,3),(4,2),(3,0),(6,4),(2,5),(8,7),(5,8),(1,9),(7,10),(9,6)]
    return edges, vertices

# --------------------------------------------------------------------
# Deep plate vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_deep_plate_profile():
    vertices = [(0.0086, -0.0000, 0.0045),(0.0086, -0.0000, 0.0090),(0.1050, -0.0000, 0.0300),(0.0758, -0.0000, 0.0045),(0.1026, -0.0000, 0.0300),(0.1050, -0.0000, 0.0270),(0.0797, -0.0000, 0.0090),(0.0792, -0.0000, 0.0000),(0.0809, -0.0000, 0.0000),(0.0758, -0.0000, 0.0090),(0.0779, -0.0000, 0.0045)]
    edges = [(10,3),(4,2),(3,0),(6,4),(2,5),(8,7),(5,8),(1,9),(7,10),(9,6)]
    return edges, vertices

# --------------------------------------------------------------------
# Side plate vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_side_plate_profile():
    veritces = [(0.0076, -0.0000, 0.0025),(0.0076, -0.0000, 0.0051),(0.0925, -0.0000, 0.0170),(0.0668, -0.0000, 0.0025),(0.0904, -0.0000, 0.0170),(0.0925, -0.0000, 0.0153),(0.0702, -0.0000, 0.0051),(0.0698, -0.0000, 0.0000),(0.0713, -0.0000, 0.0000),(0.0668, -0.0000, 0.0051),(0.0686, -0.0000, 0.0025)]
    edges = [(10,3),(4,2),(3,0),(6,4),(2,5),(8,7),(5,8),(1,9),(7,10),(9,6)]
    return edges, vertices

# --------------------------------------------------------------------
# Bowl vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_bowl_profile():
    vertices = [(0.0077, -0.0000, 0.0000),(0.0056, -0.0000, 0.0050),(0.0700, -0.0000, 0.0750),(0.0686, -0.0000, 0.0750),(0.0359, -0.0000, 0.0019),(0.0350, -0.0000, 0.0000),(0.0329, -0.0000, 0.0050),(0.0338, -0.0000, 0.0068),(0.0691, -0.0000, 0.0732),(0.0668, -0.0000, 0.0716),(0.0311, -0.0000, 0.0050),(0.0332, -0.0000, 0.0000)]
    edges = [(4,5),(3,2),(9,3),(8,4),(5,11),(10,6),(6,7),(2,8),(7,9),(1,10),(11,0)]
    return edges, vertices

# --------------------------------------------------------------------
# Cup1 vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_cup1_profile():
    vertices = [(0.0228, 0.0000, 0.0000),(0.0289, 0.0000, 0.0700),(0.0253, 0.0000, 0.0000),(0.0289, 0.0000, 0.0689),(0.0295, 0.0000, 0.0239),(0.0300, 0.0000, 0.0550),(0.0228, 0.0000, 0.0010),(0.0240, 0.0000, 0.0000),(0.0032, 0.0000, 0.0010),(0.0283, 0.0000, 0.0700),(0.0255, 0.0000, 0.0088),(0.0044, 0.0000, 0.0088),(0.0283, 0.0000, 0.0323),(0.0274, 0.0000, 0.0674),(0.0248, 0.0000, 0.0088),(0.0238, 0.0000, 0.0088),(0.0205, 0.0000, 0.0010)]
    edges = [(7,0),(4,2),(1,3),(5,4),(3,5),(0,6),(2,7),(6,16),(9,1),(13,9),(14,10),(10,12),(12,13),(15,14),(11,15),(16,8)]
    return edges, vertices

# --------------------------------------------------------------------
# Cup2 vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_cup2_profile():
    vertices = [(0.0075, -0.0000, 0.0000),(0.0427, -0.0000, 0.0800),(0.0450, -0.0000, 0.0800),(0.0427, -0.0000, 0.0800),(0.0427, -0.0000, 0.0800),(0.0098, -0.0000, 0.0060),(0.0427, -0.0000, 0.0060),(0.0427, -0.0000, 0.0100),(0.0450, -0.0000, 0.0020),(0.0450, -0.0000, 0.0760),(0.0427, -0.0000, 0.0760),(0.0450, -0.0000, 0.0000),(0.0432, -0.0000, 0.0000),(0.0404, -0.0000, 0.0060)]
    edges = [(8,11),(1,2),(3,1),(4,3),(10,4),(13,6),(6,7),(9,8),(2,9),(7,10),(11,12),(12,0),(5,13)]
    return edges, vertices

# --------------------------------------------------------------------
# Glass vertices (unit = 1)
# --------------------------------------------------------------------
def meshlib_glass_profile():
    vertices = [(0.0036, -0.0000, 0.0000),(0.0237, -0.0000, 0.0800),(0.0250, -0.0000, 0.0800),(0.0237, -0.0000, 0.0800),(0.0237, -0.0000, 0.0800),(0.0072, -0.0000, 0.0060),(0.0237, -0.0000, 0.0060),(0.0237, -0.0000, 0.0100),(0.0250, -0.0000, 0.0020),(0.0250, -0.0000, 0.0760),(0.0237, -0.0000, 0.0760),(0.0250, -0.0000, 0.0000),(0.0225, -0.0000, 0.0060),(0.0240, -0.0000, 0.0000)]
    edges = [(8,11),(1,2),(3,1),(4,3),(10,4),(13,6),(6,7),(9,8),(2,9),(7,10),(11,12),(12,0),(5,13)]
    return edges, vertices

# --------------------------------------------------------------------
# Deep plate vertices
# --------------------------------------------------------------------
def meshlib_deep_plate_vertices():
    return [(-0.0000, 0.0086, 0.0045),(-0.0000, 0.0086, 0.0090),(0.0033, 0.0080, 0.0045),(0.0033, 0.0080, 0.0090),(0.0061, 0.0061, 0.0045),(0.0061, 0.0061, 0.0090),(0.0080, 0.0033, 0.0045),(0.0080, 0.0033, 0.0090),(0.0086, -0.0000, 0.0045),(0.0086, -0.0000, 0.0090),(0.0080, -0.0033, 0.0045),(0.0080, -0.0033, 0.0090),(0.0061, -0.0061, 0.0045),(0.0061, -0.0061, 0.0090),(0.0033, -0.0080, 0.0045),(0.0033, -0.0080, 0.0090),(-0.0000, -0.0086, 0.0045),(-0.0000, -0.0086, 0.0090),(-0.0033, -0.0080, 0.0045),(-0.0033, -0.0080, 0.0090),(-0.0061, -0.0061, 0.0045),(-0.0061, -0.0061, 0.0090),(-0.0080, -0.0033, 0.0045),(-0.0080, -0.0033, 0.0090),(-0.0086, -0.0000, 0.0045),(-0.0086, -0.0000, 0.0090),(-0.0080, 0.0033, 0.0045),(-0.0080, 0.0033, 0.0090),(-0.0061, 0.0061, 0.0045),(-0.0061, 0.0061, 0.0090),(-0.0033, 0.0080, 0.0045),(-0.0033, 0.0080, 0.0090),(0.0402, 0.0970, 0.0300),(-0.0000, 0.1050, 0.0300),(0.0742, 0.0742, 0.0300),(0.0970, 0.0402, 0.0300),(0.1050, -0.0000, 0.0300),(0.0970, -0.0402, 0.0300),(0.0742, -0.0742, 0.0300),(0.0402, -0.0970, 0.0300),(0.0000, -0.1050, 0.0300),(-0.0402, -0.0970, 0.0300),(-0.0742, -0.0742, 0.0300),(-0.0970, -0.0402, 0.0300),(-0.1050, 0.0000, 0.0300),(-0.0970, 0.0402, 0.0300),(-0.0742, 0.0742, 0.0300),(-0.0402, 0.0970, 0.0300),(-0.0000, 0.0758, 0.0045),(-0.0290, 0.0700, 0.0045),(-0.0536, 0.0536, 0.0045),(-0.0700, 0.0290, 0.0045),(-0.0758, -0.0000, 0.0045),(-0.0700, -0.0290, 0.0045),(-0.0536, -0.0536, 0.0045),(-0.0290, -0.0700, 0.0045),(-0.0000, -0.0758, 0.0045),(0.0290, -0.0700, 0.0045),(0.0536, -0.0536, 0.0045),(0.0700, -0.0290, 0.0045),(0.0758, -0.0000, 0.0045),(0.0700, 0.0290, 0.0045),(0.0536, 0.0536, 0.0045),(0.0290, 0.0700, 0.0045),(0.0290, 0.0700, 0.0090),(0.0290, -0.0700, 0.0090),(-0.0290, -0.0700, 0.0090),(-0.0536, -0.0536, 0.0090),(-0.0700, 0.0290, 0.0090),(-0.0536, 0.0536, 0.0090),(-0.0290, 0.0700, 0.0090),(0.0393, 0.0948, 0.0300),(0.0725, 0.0725, 0.0300),(0.0948, 0.0393, 0.0300),(0.1026, -0.0000, 0.0300),(0.0948, -0.0393, 0.0300),(0.0725, -0.0725, 0.0300),(0.0393, -0.0948, 0.0300),(0.0000, -0.1026, 0.0300),(-0.0393, -0.0948, 0.0300),(-0.0725, -0.0725, 0.0300),(-0.0948, -0.0393, 0.0300),(-0.1026, 0.0000, 0.0300),(-0.0948, 0.0393, 0.0300),(-0.0725, 0.0725, 0.0300),(-0.0393, 0.0948, 0.0300),(-0.0000, 0.1026, 0.0300),(-0.0000, 0.1050, 0.0270),(0.0402, 0.0970, 0.0270),(0.0742, 0.0742, 0.0270),(0.0970, 0.0402, 0.0270),(0.1050, -0.0000, 0.0270),(0.0970, -0.0402, 0.0270),(0.0742, -0.0742, 0.0270),(0.0402, -0.0970, 0.0270),(0.0000, -0.1050, 0.0270),(-0.0402, -0.0970, 0.0270),(-0.0742, -0.0742, 0.0270),(-0.0970, -0.0402, 0.0270),(-0.1050, 0.0000, 0.0270),(-0.0970, 0.0402, 0.0270),(-0.0742, 0.0742, 0.0270),(-0.0402, 0.0970, 0.0270),(-0.0000, 0.0797, 0.0090),(0.0305, 0.0736, 0.0090),(0.0564, 0.0564, 0.0090),(0.0736, 0.0305, 0.0090),(0.0797, -0.0000, 0.0090),(0.0736, -0.0305, 0.0090),(0.0564, -0.0564, 0.0090),(0.0305, -0.0736, 0.0090),(-0.0000, -0.0797, 0.0090),(-0.0305, -0.0736, 0.0090),(-0.0564, -0.0564, 0.0090),(-0.0736, -0.0305, 0.0090),(-0.0797, 0.0000, 0.0090),(-0.0736, 0.0305, 0.0090),(-0.0564, 0.0564, 0.0090),(-0.0305, 0.0736, 0.0090),(0.0303, 0.0732, 0.0000),(-0.0000, 0.0792, 0.0000),(0.0560, 0.0560, 0.0000),(0.0732, 0.0303, 0.0000),(0.0792, -0.0000, 0.0000),(0.0732, -0.0303, 0.0000),(0.0560, -0.0560, 0.0000),(0.0303, -0.0732, 0.0000),(-0.0000, -0.0792, 0.0000),(-0.0303, -0.0732, 0.0000),(-0.0560, -0.0560, 0.0000),(-0.0732, -0.0303, 0.0000),(-0.0792, 0.0000, 0.0000),(-0.0732, 0.0303, 0.0000),(-0.0560, 0.0560, 0.0000),(-0.0303, 0.0732, 0.0000),(-0.0000, 0.0809, 0.0000),(0.0310, 0.0748, 0.0000),(0.0572, 0.0572, 0.0000),(0.0748, 0.0310, 0.0000),(0.0809, -0.0000, 0.0000),(0.0748, -0.0310, 0.0000),(0.0572, -0.0572, 0.0000),(0.0310, -0.0748, 0.0000),(-0.0000, -0.0809, 0.0000),(-0.0310, -0.0748, 0.0000),(-0.0572, -0.0572, 0.0000),(-0.0748, -0.0310, 0.0000),(-0.0809, 0.0000, 0.0000),(-0.0748, 0.0310, 0.0000),(-0.0572, 0.0572, 0.0000),(-0.0310, 0.0748, 0.0000),(-0.0000, 0.0758, 0.0090),(0.0536, 0.0536, 0.0090),(0.0700, 0.0290, 0.0090),(0.0758, -0.0000, 0.0090),(0.0700, -0.0290, 0.0090),(0.0536, -0.0536, 0.0090),(-0.0000, -0.0758, 0.0090),(-0.0700, -0.0290, 0.0090),(-0.0758, -0.0000, 0.0090),(-0.0298, 0.0719, 0.0045),(-0.0551, 0.0551, 0.0045),(-0.0719, 0.0298, 0.0045),(-0.0779, -0.0000, 0.0045),(-0.0719, -0.0298, 0.0045),(-0.0551, -0.0551, 0.0045),(-0.0298, -0.0719, 0.0045),(-0.0000, -0.0779, 0.0045),(0.0298, -0.0719, 0.0045),(0.0551, -0.0551, 0.0045),(0.0719, -0.0298, 0.0045),(0.0779, -0.0000, 0.0045),(0.0719, 0.0298, 0.0045),(0.0551, 0.0551, 0.0045),(0.0298, 0.0719, 0.0045),(-0.0000, 0.0779, 0.0045)]

# --------------------------------------------------------------------
# Deep plate faces
# --------------------------------------------------------------------
def meshlib_deep_plate_faces():
    return [(87,33,32,88),(88,32,34,89),(89,34,35,90),(90,35,36,91),(91,36,37,92),(92,37,38,93),(93,38,39,94),(94,39,40,95),(95,40,41,96),(96,41,42,97),(97,42,43,98),(98,43,44,99),(99,44,45,100),(100,45,46,101),(3,1,31,29,27,25,23,21,19,17,15,13,11,9,7,5),(101,46,47,102),(102,47,33,87),(0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30),(86,71,32,33),(71,72,34,32),(72,73,35,34),(73,74,36,35),(74,75,37,36),(75,76,38,37),(76,77,39,38),(77,78,40,39),(78,79,41,40),(79,80,42,41),(80,81,43,42),(81,82,44,43),(82,83,45,44),(83,84,46,45),(84,85,47,46),(85,86,33,47),(50,49,30,28),(51,50,28,26),(52,51,26,24),(53,52,24,22),(54,53,22,20),(55,54,20,18),(56,55,18,16),(57,56,16,14),(58,57,14,12),(59,58,12,10),(60,59,10,8),(61,60,8,6),(62,61,6,4),(63,62,4,2),(48,175,174,63),(118,103,86,85),(117,118,85,84),(116,117,84,83),(115,116,83,82),(114,115,82,81),(113,114,81,80),(112,113,80,79),(111,112,79,78),(110,111,78,77),(109,110,77,76),(108,109,76,75),(107,108,75,74),(106,107,74,73),(105,106,73,72),(104,105,72,71),(103,104,71,86),(160,175,48,49),(135,150,102,87),(150,149,101,102),(149,148,100,101),(148,147,99,100),(147,146,98,99),(146,145,97,98),(145,144,96,97),(144,143,95,96),(143,142,94,95),(142,141,93,94),(141,140,92,93),(140,139,91,92),(139,138,90,91),(138,137,89,90),(137,136,88,89),(151,64,104,103),(64,152,105,104),(152,153,106,105),(153,154,107,106),(154,155,108,107),(155,156,109,108),(156,65,110,109),(65,157,111,110),(157,66,112,111),(66,67,113,112),(67,158,114,113),(158,159,115,114),(159,68,116,115),(68,69,117,116),(69,70,118,117),(70,151,103,118),(175,160,134,120),(160,161,133,134),(161,162,132,133),(162,163,131,132),(163,164,130,131),(164,165,129,130),(165,166,128,129),(166,167,127,128),(167,168,126,127),(168,169,125,126),(169,170,124,125),(170,171,123,124),(171,172,122,123),(172,173,121,122),(173,174,119,121),(174,175,120,119),(136,135,87,88),(119,120,135,136),(121,119,136,137),(122,121,137,138),(123,122,138,139),(124,123,139,140),(125,124,140,141),(126,125,141,142),(127,126,142,143),(128,127,143,144),(129,128,144,145),(130,129,145,146),(131,130,146,147),(132,131,147,148),(133,132,148,149),(134,133,149,150),(120,134,150,135),(1,3,64,151),(3,5,152,64),(5,7,153,152),(7,9,154,153),(9,11,155,154),(11,13,156,155),(13,15,65,156),(15,17,157,65),(17,19,66,157),(19,21,67,66),(21,23,158,67),(23,25,159,158),(25,27,68,159),(27,29,69,68),(29,31,70,69),(31,1,151,70),(0,48,63,2),(174,173,62,63),(173,172,61,62),(172,171,60,61),(171,170,59,60),(170,169,58,59),(169,168,57,58),(168,167,56,57),(167,166,55,56),(166,165,54,55),(165,164,53,54),(164,163,52,53),(163,162,51,52),(162,161,50,51),(161,160,49,50),(49,48,0,30)]
