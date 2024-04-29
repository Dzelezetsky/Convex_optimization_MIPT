import numpy as np
n = 10
K = 6
gamma = 1.0
mu = np.array([ 0.     , 0.01401, 0.03426, 0.07843, 0.06536,-0.0342 , 0.03325,-0.0053 ,
 -0.00361, 0.01437])
Sigma_1 = np.array([[ 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     ,
   0.     , 0.     ],
 [ 0.     , 0.09551, 0.0349 , 0.06526, 0.02499, 0.08272, 0.0574 , 0.0279 ,
   0.06016, 0.02578],
 [ 0.     , 0.0349 , 0.10862, 0.05107, 0.04959, 0.08917, 0.03489, 0.03575,
   0.05086, 0.04512],
 [ 0.     , 0.06526, 0.05107, 0.08159, 0.04136, 0.06879, 0.05743, 0.03721,
   0.05037, 0.03557],
 [ 0.     , 0.02499, 0.04959, 0.04136, 0.05882, 0.05781, 0.03069, 0.02881,
   0.04037, 0.04467],
 [ 0.     , 0.08272, 0.08917, 0.06879, 0.05781, 0.11844, 0.05441, 0.03745,
   0.07088, 0.05695],
 [ 0.     , 0.0574 , 0.03489, 0.05743, 0.03069, 0.05441, 0.06421, 0.0201 ,
   0.05843, 0.02407],
 [ 0.     , 0.0279 , 0.03575, 0.03721, 0.02881, 0.03745, 0.0201 , 0.04035,
   0.03334, 0.01554],
 [ 0.     , 0.06016, 0.05086, 0.05037, 0.04037, 0.07088, 0.05843, 0.03334,
   0.07538, 0.02431],
 [ 0.     , 0.02578, 0.04512, 0.03557, 0.04467, 0.05695, 0.02407, 0.01554,
   0.02431, 0.04693]])
Sigma_2 = np.array([[ 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     ,
   0.     , 0.     ],
 [ 0.     , 0.09527, 0.04324, 0.06411, 0.03937, 0.08697, 0.0531 , 0.02343,
   0.04872, 0.03118],
 [ 0.     , 0.04324, 0.10897, 0.05601, 0.0504 , 0.07851, 0.02892, 0.05001,
   0.05234, 0.03949],
 [ 0.     , 0.06411, 0.05601, 0.08566, 0.04111, 0.07517, 0.05672, 0.04489,
   0.04828, 0.02699],
 [ 0.     , 0.03937, 0.0504 , 0.04111, 0.0629 , 0.06144, 0.03637, 0.01778,
   0.03433, 0.03934],
 [ 0.     , 0.08697, 0.07851, 0.07517, 0.06144, 0.11296, 0.04474, 0.04238,
   0.0637 , 0.04279],
 [ 0.     , 0.0531 , 0.02892, 0.05672, 0.03637, 0.04474, 0.06381, 0.02148,
   0.04539, 0.02673],
 [ 0.     , 0.02343, 0.05001, 0.04489, 0.01778, 0.04238, 0.02148, 0.04386,
   0.02824, 0.02502],
 [ 0.     , 0.04872, 0.05234, 0.04828, 0.03433, 0.0637 , 0.04539, 0.02824,
   0.07299, 0.01923],
 [ 0.     , 0.03118, 0.03949, 0.02699, 0.03934, 0.04279, 0.02673, 0.02502,
   0.01923, 0.0441 ]])
Sigma_3 = np.array([[ 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     ,
   0.     , 0.     ],
 [ 0.     , 0.09758, 0.036  , 0.05946, 0.03143, 0.08617, 0.05603, 0.02755,
   0.04373, 0.03548],
 [ 0.     , 0.036  , 0.11032, 0.07466, 0.04976, 0.06889, 0.04397, 0.0413 ,
   0.0693 , 0.05059],
 [ 0.     , 0.05946, 0.07466, 0.08391, 0.04429, 0.06875, 0.05999, 0.03834,
   0.05702, 0.03957],
 [ 0.     , 0.03143, 0.04976, 0.04429, 0.0628 , 0.0601 , 0.04081, 0.02044,
   0.0435 , 0.03797],
 [ 0.     , 0.08617, 0.06889, 0.06875, 0.0601 , 0.11514, 0.05033, 0.03409,
   0.05194, 0.05301],
 [ 0.     , 0.05603, 0.04397, 0.05999, 0.04081, 0.05033, 0.0634 , 0.03646,
   0.055  , 0.03016],
 [ 0.     , 0.02755, 0.0413 , 0.03834, 0.02044, 0.03409, 0.03646, 0.04068,
   0.03718, 0.02399],
 [ 0.     , 0.04373, 0.0693 , 0.05702, 0.0435 , 0.05194, 0.055  , 0.03718,
   0.07564, 0.02574],
 [ 0.     , 0.03548, 0.05059, 0.03957, 0.03797, 0.05301, 0.03016, 0.02399,
   0.02574, 0.04612]])
Sigma_4 = np.array([[ 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     ,
   0.     , 0.     ],
 [ 0.     , 0.09257, 0.05796, 0.06027, 0.02972, 0.07934, 0.04614, 0.03909,
   0.04214, 0.04069],
 [ 0.     , 0.05796, 0.11237, 0.07639, 0.06354, 0.07092, 0.05474, 0.05455,
   0.04729, 0.05416],
 [ 0.     , 0.06027, 0.07639, 0.08818, 0.04459, 0.07078, 0.06168, 0.03892,
   0.05792, 0.02804],
 [ 0.     , 0.02972, 0.06354, 0.04459, 0.05821, 0.04937, 0.03315, 0.02327,
   0.03579, 0.04053],
 [ 0.     , 0.07934, 0.07092, 0.07078, 0.04937, 0.11239, 0.04701, 0.04395,
   0.05605, 0.05801],
 [ 0.     , 0.04614, 0.05474, 0.06168, 0.03315, 0.04701, 0.06062, 0.02048,
   0.03839, 0.02321],
 [ 0.     , 0.03909, 0.05455, 0.03892, 0.02327, 0.04395, 0.02048, 0.0407 ,
   0.03774, 0.03034],
 [ 0.     , 0.04214, 0.04729, 0.05792, 0.03579, 0.05605, 0.03839, 0.03774,
   0.07333, 0.03067],
 [ 0.     , 0.04069, 0.05416, 0.02804, 0.04053, 0.05801, 0.02321, 0.03034,
   0.03067, 0.04903]])
Sigma_5 = np.array([[ 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     ,
   0.     , 0.     ],
 [ 0.     , 0.09782, 0.03566, 0.07154, 0.02311, 0.08306, 0.04749, 0.02112,
   0.0424 , 0.03644],
 [ 0.     , 0.03566, 0.10871, 0.07059, 0.06327, 0.07008, 0.05601, 0.03631,
   0.04979, 0.03542],
 [ 0.     , 0.07154, 0.07059, 0.08676, 0.03368, 0.07664, 0.04439, 0.03324,
   0.04954, 0.04171],
 [ 0.     , 0.02311, 0.06327, 0.03368, 0.06425, 0.06407, 0.03624, 0.02072,
   0.03599, 0.03501],
 [ 0.     , 0.08306, 0.07008, 0.07664, 0.06407, 0.12031, 0.05653, 0.04843,
   0.07035, 0.0477 ],
 [ 0.     , 0.04749, 0.05601, 0.04439, 0.03624, 0.05653, 0.06048, 0.02421,
   0.04491, 0.03085],
 [ 0.     , 0.02112, 0.03631, 0.03324, 0.02072, 0.04843, 0.02421, 0.04139,
   0.03155, 0.01375],
 [ 0.     , 0.0424 , 0.04979, 0.04954, 0.03599, 0.07035, 0.04491, 0.03155,
   0.07377, 0.02758],
 [ 0.     , 0.03644, 0.03542, 0.04171, 0.03501, 0.0477 , 0.03085, 0.01375,
   0.02758, 0.04266]])
Sigma_6 = np.array([[ 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     , 0.     ,
   0.     , 0.     ],
 [ 0.     , 0.09255, 0.04784, 0.06448, 0.03509, 0.0763 , 0.04992, 0.02928,
   0.0457 , 0.03255],
 [ 0.     , 0.04784, 0.1073 , 0.06532, 0.06136, 0.08782, 0.04596, 0.04693,
   0.05876, 0.04758],
 [ 0.     , 0.06448, 0.06532, 0.08067, 0.04062, 0.07364, 0.05039, 0.03586,
   0.06005, 0.03123],
 [ 0.     , 0.03509, 0.06136, 0.04062, 0.05804, 0.05872, 0.03194, 0.02341,
   0.04013, 0.03734],
 [ 0.     , 0.0763 , 0.08782, 0.07364, 0.05872, 0.10969, 0.05726, 0.04673,
   0.05876, 0.0505 ],
 [ 0.     , 0.04992, 0.04596, 0.05039, 0.03194, 0.05726, 0.06021, 0.02738,
   0.04926, 0.02845],
 [ 0.     , 0.02928, 0.04693, 0.03586, 0.02341, 0.04673, 0.02738, 0.0397 ,
   0.02841, 0.02057],
 [ 0.     , 0.0457 , 0.05876, 0.06005, 0.04013, 0.05876, 0.04926, 0.02841,
   0.07194, 0.0291 ],
 [ 0.     , 0.03255, 0.04758, 0.03123, 0.03734, 0.0505 , 0.02845, 0.02057,
   0.0291 , 0.04176]])