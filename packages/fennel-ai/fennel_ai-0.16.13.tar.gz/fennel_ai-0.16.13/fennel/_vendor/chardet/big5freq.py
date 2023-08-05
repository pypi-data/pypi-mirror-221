######################## BEGIN LICENSE BLOCK ########################
# The Original Code is Mozilla Communicator client code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 1998
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Mark Pilgrim - port to Python
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################

# Big5 frequency table
# by Taiwan's Mandarin Promotion Council
# <http://www.edu.tw:81/mandr/>
#
# 128  --> 0.42261
# 256  --> 0.57851
# 512  --> 0.74851
# 1024 --> 0.89384
# 2048 --> 0.97583
#
# Ideal Distribution Ratio = 0.74851/(1-0.74851) =2.98
# Random Distribution Ration = 512/(5401-512)=0.105
#
# Typical Distribution Ratio about 25% of Ideal one, still much higher than RDR

BIG5_TYPICAL_DISTRIBUTION_RATIO = 0.75

# Char to FreqOrder table
BIG5_TABLE_SIZE = 5376
# fmt: off
BIG5_CHAR_TO_FREQ_ORDER = (
   1,1801,1506, 255,1431, 198,   9,  82,   6,5008, 177, 202,3681,1256,2821, 110, #   16
3814,  33,3274, 261,  76,  44,2114,  16,2946,2187,1176, 659,3971,  26,3451,2653, #   32
1198,3972,3350,4202, 410,2215, 302, 590, 361,1964,   8, 204,  58,4510,5009,1932, #   48
  63,5010,5011, 317,1614,  75, 222, 159,4203,2417,1480,5012,3555,3091, 224,2822, #   64
3682,   3,  10,3973,1471,  29,2787,1135,2866,1940, 873, 130,3275,1123, 312,5013, #   80
4511,2052, 507, 252, 682,5014, 142,1915, 124, 206,2947,  34,3556,3204,  64, 604, #   96
5015,2501,1977,1978, 155,1991, 645, 641,1606,5016,3452, 337,  72, 406,5017,  80, #  112
 630, 238,3205,1509, 263, 939,1092,2654, 756,1440,1094,3453, 449,  69,2987, 591, #  128
 179,2096, 471, 115,2035,1844,  60,  50,2988, 134, 806,1869, 734,2036,3454, 180, #  144
 995,1607, 156, 537,2907, 688,5018, 319,1305, 779,2145, 514,2379, 298,4512, 359, #  160
2502,  90,2716,1338, 663,  11, 906,1099,2553,  20,2441, 182, 532,1716,5019, 732, #  176
1376,4204,1311,1420,3206,  25,2317,1056, 113, 399, 382,1950, 242,3455,2474, 529, #  192
3276, 475,1447,3683,5020, 117,  21, 656, 810,1297,2300,2334,3557,5021, 126,4205, #  208
 706, 456, 150, 613,4513,  71,1118,2037,4206, 145,3092,  85, 835, 486,2115,1246, #  224
1426, 428, 727,1285,1015, 800, 106, 623, 303,1281,5022,2128,2359, 347,3815, 221, #  240
3558,3135,5023,1956,1153,4207,  83, 296,1199,3093, 192, 624,  93,5024, 822,1898, #  256
2823,3136, 795,2065, 991,1554,1542,1592,  27,  43,2867, 859, 139,1456, 860,4514, #  272
 437, 712,3974, 164,2397,3137, 695, 211,3037,2097, 195,3975,1608,3559,3560,3684, #  288
3976, 234, 811,2989,2098,3977,2233,1441,3561,1615,2380, 668,2077,1638, 305, 228, #  304
1664,4515, 467, 415,5025, 262,2099,1593, 239, 108, 300, 200,1033, 512,1247,2078, #  320
5026,5027,2176,3207,3685,2682, 593, 845,1062,3277,  88,1723,2038,3978,1951, 212, #  336
 266, 152, 149, 468,1899,4208,4516,  77, 187,5028,3038,  37,   5,2990,5029,3979, #  352
5030,5031,  39,2524,4517,2908,3208,2079,  55, 148,  74,4518, 545, 483,1474,1029, #  368
1665, 217,1870,1531,3138,1104,2655,4209,  24, 172,3562, 900,3980,3563,3564,4519, #  384
  32,1408,2824,1312, 329, 487,2360,2251,2717, 784,2683,   4,3039,3351,1427,1789, #  400
 188, 109, 499,5032,3686,1717,1790, 888,1217,3040,4520,5033,3565,5034,3352,1520, #  416
3687,3981, 196,1034, 775,5035,5036, 929,1816, 249, 439,  38,5037,1063,5038, 794, #  432
3982,1435,2301,  46, 178,3278,2066,5039,2381,5040, 214,1709,4521, 804,  35, 707, #  448
 324,3688,1601,2554, 140, 459,4210,5041,5042,1365, 839, 272, 978,2262,2580,3456, #  464
2129,1363,3689,1423, 697, 100,3094,  48,  70,1231, 495,3139,2196,5043,1294,5044, #  480
2080, 462, 586,1042,3279, 853, 256, 988, 185,2382,3457,1698, 434,1084,5045,3458, #  496
 314,2625,2788,4522,2335,2336, 569,2285, 637,1817,2525, 757,1162,1879,1616,3459, #  512
 287,1577,2116, 768,4523,1671,2868,3566,2526,1321,3816, 909,2418,5046,4211, 933, #  528
3817,4212,2053,2361,1222,4524, 765,2419,1322, 786,4525,5047,1920,1462,1677,2909, #  544
1699,5048,4526,1424,2442,3140,3690,2600,3353,1775,1941,3460,3983,4213, 309,1369, #  560
1130,2825, 364,2234,1653,1299,3984,3567,3985,3986,2656, 525,1085,3041, 902,2001, #  576
1475, 964,4527, 421,1845,1415,1057,2286, 940,1364,3141, 376,4528,4529,1381,   7, #  592
2527, 983,2383, 336,1710,2684,1846, 321,3461, 559,1131,3042,2752,1809,1132,1313, #  608
 265,1481,1858,5049, 352,1203,2826,3280, 167,1089, 420,2827, 776, 792,1724,3568, #  624
4214,2443,3281,5050,4215,5051, 446, 229, 333,2753, 901,3818,1200,1557,4530,2657, #  640
1921, 395,2754,2685,3819,4216,1836, 125, 916,3209,2626,4531,5052,5053,3820,5054, #  656
5055,5056,4532,3142,3691,1133,2555,1757,3462,1510,2318,1409,3569,5057,2146, 438, #  672
2601,2910,2384,3354,1068, 958,3043, 461, 311,2869,2686,4217,1916,3210,4218,1979, #  688
 383, 750,2755,2627,4219, 274, 539, 385,1278,1442,5058,1154,1965, 384, 561, 210, #  704
  98,1295,2556,3570,5059,1711,2420,1482,3463,3987,2911,1257, 129,5060,3821, 642, #  720
 523,2789,2790,2658,5061, 141,2235,1333,  68, 176, 441, 876, 907,4220, 603,2602, #  736
 710, 171,3464, 404, 549,  18,3143,2398,1410,3692,1666,5062,3571,4533,2912,4534, #  752
5063,2991, 368,5064, 146, 366,  99, 871,3693,1543, 748, 807,1586,1185,  22,2263, #  768
 379,3822,3211,5065,3212, 505,1942,2628,1992,1382,2319,5066, 380,2362, 218, 702, #  784
1818,1248,3465,3044,3572,3355,3282,5067,2992,3694, 930,3283,3823,5068,  59,5069, #  800
 585, 601,4221, 497,3466,1112,1314,4535,1802,5070,1223,1472,2177,5071, 749,1837, #  816
 690,1900,3824,1773,3988,1476, 429,1043,1791,2236,2117, 917,4222, 447,1086,1629, #  832
5072, 556,5073,5074,2021,1654, 844,1090, 105, 550, 966,1758,2828,1008,1783, 686, #  848
1095,5075,2287, 793,1602,5076,3573,2603,4536,4223,2948,2302,4537,3825, 980,2503, #  864
 544, 353, 527,4538, 908,2687,2913,5077, 381,2629,1943,1348,5078,1341,1252, 560, #  880
3095,5079,3467,2870,5080,2054, 973, 886,2081, 143,4539,5081,5082, 157,3989, 496, #  896
4224,  57, 840, 540,2039,4540,4541,3468,2118,1445, 970,2264,1748,1966,2082,4225, #  912
3144,1234,1776,3284,2829,3695, 773,1206,2130,1066,2040,1326,3990,1738,1725,4226, #  928
 279,3145,  51,1544,2604, 423,1578,2131,2067, 173,4542,1880,5083,5084,1583, 264, #  944
 610,3696,4543,2444, 280, 154,5085,5086,5087,1739, 338,1282,3096, 693,2871,1411, #  960
1074,3826,2445,5088,4544,5089,5090,1240, 952,2399,5091,2914,1538,2688, 685,1483, #  976
4227,2475,1436, 953,4228,2055,4545, 671,2400,  79,4229,2446,3285, 608, 567,2689, #  992
3469,4230,4231,1691, 393,1261,1792,2401,5092,4546,5093,5094,5095,5096,1383,1672, # 1008
3827,3213,1464, 522,1119, 661,1150, 216, 675,4547,3991,1432,3574, 609,4548,2690, # 1024
2402,5097,5098,5099,4232,3045,   0,5100,2476, 315, 231,2447, 301,3356,4549,2385, # 1040
5101, 233,4233,3697,1819,4550,4551,5102,  96,1777,1315,2083,5103, 257,5104,1810, # 1056
3698,2718,1139,1820,4234,2022,1124,2164,2791,1778,2659,5105,3097, 363,1655,3214, # 1072
5106,2993,5107,5108,5109,3992,1567,3993, 718, 103,3215, 849,1443, 341,3357,2949, # 1088
1484,5110,1712, 127,  67, 339,4235,2403, 679,1412, 821,5111,5112, 834, 738, 351, # 1104
2994,2147, 846, 235,1497,1881, 418,1993,3828,2719, 186,1100,2148,2756,3575,1545, # 1120
1355,2950,2872,1377, 583,3994,4236,2581,2995,5113,1298,3699,1078,2557,3700,2363, # 1136
  78,3829,3830, 267,1289,2100,2002,1594,4237, 348, 369,1274,2197,2178,1838,4552, # 1152
1821,2830,3701,2757,2288,2003,4553,2951,2758, 144,3358, 882,4554,3995,2759,3470, # 1168
4555,2915,5114,4238,1726, 320,5115,3996,3046, 788,2996,5116,2831,1774,1327,2873, # 1184
3997,2832,5117,1306,4556,2004,1700,3831,3576,2364,2660, 787,2023, 506, 824,3702, # 1200
 534, 323,4557,1044,3359,2024,1901, 946,3471,5118,1779,1500,1678,5119,1882,4558, # 1216
 165, 243,4559,3703,2528, 123, 683,4239, 764,4560,  36,3998,1793, 589,2916, 816, # 1232
 626,1667,3047,2237,1639,1555,1622,3832,3999,5120,4000,2874,1370,1228,1933, 891, # 1248
2084,2917, 304,4240,5121, 292,2997,2720,3577, 691,2101,4241,1115,4561, 118, 662, # 1264
5122, 611,1156, 854,2386,1316,2875,   2, 386, 515,2918,5123,5124,3286, 868,2238, # 1280
1486, 855,2661, 785,2216,3048,5125,1040,3216,3578,5126,3146, 448,5127,1525,5128, # 1296
2165,4562,5129,3833,5130,4242,2833,3579,3147, 503, 818,4001,3148,1568, 814, 676, # 1312
1444, 306,1749,5131,3834,1416,1030, 197,1428, 805,2834,1501,4563,5132,5133,5134, # 1328
1994,5135,4564,5136,5137,2198,  13,2792,3704,2998,3149,1229,1917,5138,3835,2132, # 1344
5139,4243,4565,2404,3580,5140,2217,1511,1727,1120,5141,5142, 646,3836,2448, 307, # 1360
5143,5144,1595,3217,5145,5146,5147,3705,1113,1356,4002,1465,2529,2530,5148, 519, # 1376
5149, 128,2133,  92,2289,1980,5150,4003,1512, 342,3150,2199,5151,2793,2218,1981, # 1392
3360,4244, 290,1656,1317, 789, 827,2365,5152,3837,4566, 562, 581,4004,5153, 401, # 1408
4567,2252,  94,4568,5154,1399,2794,5155,1463,2025,4569,3218,1944,5156, 828,1105, # 1424
4245,1262,1394,5157,4246, 605,4570,5158,1784,2876,5159,2835, 819,2102, 578,2200, # 1440
2952,5160,1502, 436,3287,4247,3288,2836,4005,2919,3472,3473,5161,2721,2320,5162, # 1456
5163,2337,2068,  23,4571, 193, 826,3838,2103, 699,1630,4248,3098, 390,1794,1064, # 1472
3581,5164,1579,3099,3100,1400,5165,4249,1839,1640,2877,5166,4572,4573, 137,4250, # 1488
 598,3101,1967, 780, 104, 974,2953,5167, 278, 899, 253, 402, 572, 504, 493,1339, # 1504
5168,4006,1275,4574,2582,2558,5169,3706,3049,3102,2253, 565,1334,2722, 863,  41, # 1520
5170,5171,4575,5172,1657,2338,  19, 463,2760,4251, 606,5173,2999,3289,1087,2085, # 1536
1323,2662,3000,5174,1631,1623,1750,4252,2691,5175,2878, 791,2723,2663,2339, 232, # 1552
2421,5176,3001,1498,5177,2664,2630, 755,1366,3707,3290,3151,2026,1609, 119,1918, # 1568
3474, 862,1026,4253,5178,4007,3839,4576,4008,4577,2265,1952,2477,5179,1125, 817, # 1584
4254,4255,4009,1513,1766,2041,1487,4256,3050,3291,2837,3840,3152,5180,5181,1507, # 1600
5182,2692, 733,  40,1632,1106,2879, 345,4257, 841,2531, 230,4578,3002,1847,3292, # 1616
3475,5183,1263, 986,3476,5184, 735, 879, 254,1137, 857, 622,1300,1180,1388,1562, # 1632
4010,4011,2954, 967,2761,2665,1349, 592,2134,1692,3361,3003,1995,4258,1679,4012, # 1648
1902,2188,5185, 739,3708,2724,1296,1290,5186,4259,2201,2202,1922,1563,2605,2559, # 1664
1871,2762,3004,5187, 435,5188, 343,1108, 596,  17,1751,4579,2239,3477,3709,5189, # 1680
4580, 294,3582,2955,1693, 477, 979, 281,2042,3583, 643,2043,3710,2631,2795,2266, # 1696
1031,2340,2135,2303,3584,4581, 367,1249,2560,5190,3585,5191,4582,1283,3362,2005, # 1712
 240,1762,3363,4583,4584, 836,1069,3153, 474,5192,2149,2532, 268,3586,5193,3219, # 1728
1521,1284,5194,1658,1546,4260,5195,3587,3588,5196,4261,3364,2693,1685,4262, 961, # 1744
1673,2632, 190,2006,2203,3841,4585,4586,5197, 570,2504,3711,1490,5198,4587,2633, # 1760
3293,1957,4588, 584,1514, 396,1045,1945,5199,4589,1968,2449,5200,5201,4590,4013, # 1776
 619,5202,3154,3294, 215,2007,2796,2561,3220,4591,3221,4592, 763,4263,3842,4593, # 1792
5203,5204,1958,1767,2956,3365,3712,1174, 452,1477,4594,3366,3155,5205,2838,1253, # 1808
2387,2189,1091,2290,4264, 492,5206, 638,1169,1825,2136,1752,4014, 648, 926,1021, # 1824
1324,4595, 520,4596, 997, 847,1007, 892,4597,3843,2267,1872,3713,2405,1785,4598, # 1840
1953,2957,3103,3222,1728,4265,2044,3714,4599,2008,1701,3156,1551,  30,2268,4266, # 1856
5207,2027,4600,3589,5208, 501,5209,4267, 594,3478,2166,1822,3590,3479,3591,3223, # 1872
 829,2839,4268,5210,1680,3157,1225,4269,5211,3295,4601,4270,3158,2341,5212,4602, # 1888
4271,5213,4015,4016,5214,1848,2388,2606,3367,5215,4603, 374,4017, 652,4272,4273, # 1904
 375,1140, 798,5216,5217,5218,2366,4604,2269, 546,1659, 138,3051,2450,4605,5219, # 1920
2254, 612,1849, 910, 796,3844,1740,1371, 825,3845,3846,5220,2920,2562,5221, 692, # 1936
 444,3052,2634, 801,4606,4274,5222,1491, 244,1053,3053,4275,4276, 340,5223,4018, # 1952
1041,3005, 293,1168,  87,1357,5224,1539, 959,5225,2240, 721, 694,4277,3847, 219, # 1968
1478, 644,1417,3368,2666,1413,1401,1335,1389,4019,5226,5227,3006,2367,3159,1826, # 1984
 730,1515, 184,2840,  66,4607,5228,1660,2958, 246,3369, 378,1457, 226,3480, 975, # 2000
4020,2959,1264,3592, 674, 696,5229, 163,5230,1141,2422,2167, 713,3593,3370,4608, # 2016
4021,5231,5232,1186,  15,5233,1079,1070,5234,1522,3224,3594, 276,1050,2725, 758, # 2032
1126, 653,2960,3296,5235,2342, 889,3595,4022,3104,3007, 903,1250,4609,4023,3481, # 2048
3596,1342,1681,1718, 766,3297, 286,  89,2961,3715,5236,1713,5237,2607,3371,3008, # 2064
5238,2962,2219,3225,2880,5239,4610,2505,2533, 181, 387,1075,4024, 731,2190,3372, # 2080
5240,3298, 310, 313,3482,2304, 770,4278,  54,3054, 189,4611,3105,3848,4025,5241, # 2096
1230,1617,1850, 355,3597,4279,4612,3373, 111,4280,3716,1350,3160,3483,3055,4281, # 2112
2150,3299,3598,5242,2797,4026,4027,3009, 722,2009,5243,1071, 247,1207,2343,2478, # 2128
1378,4613,2010, 864,1437,1214,4614, 373,3849,1142,2220, 667,4615, 442,2763,2563, # 2144
3850,4028,1969,4282,3300,1840, 837, 170,1107, 934,1336,1883,5244,5245,2119,4283, # 2160
2841, 743,1569,5246,4616,4284, 582,2389,1418,3484,5247,1803,5248, 357,1395,1729, # 2176
3717,3301,2423,1564,2241,5249,3106,3851,1633,4617,1114,2086,4285,1532,5250, 482, # 2192
2451,4618,5251,5252,1492, 833,1466,5253,2726,3599,1641,2842,5254,1526,1272,3718, # 2208
4286,1686,1795, 416,2564,1903,1954,1804,5255,3852,2798,3853,1159,2321,5256,2881, # 2224
4619,1610,1584,3056,2424,2764, 443,3302,1163,3161,5257,5258,4029,5259,4287,2506, # 2240
3057,4620,4030,3162,2104,1647,3600,2011,1873,4288,5260,4289, 431,3485,5261, 250, # 2256
  97,  81,4290,5262,1648,1851,1558, 160, 848,5263, 866, 740,1694,5264,2204,2843, # 2272
3226,4291,4621,3719,1687, 950,2479, 426, 469,3227,3720,3721,4031,5265,5266,1188, # 2288
 424,1996, 861,3601,4292,3854,2205,2694, 168,1235,3602,4293,5267,2087,1674,4622, # 2304
3374,3303, 220,2565,1009,5268,3855, 670,3010, 332,1208, 717,5269,5270,3603,2452, # 2320
4032,3375,5271, 513,5272,1209,2882,3376,3163,4623,1080,5273,5274,5275,5276,2534, # 2336
3722,3604, 815,1587,4033,4034,5277,3605,3486,3856,1254,4624,1328,3058,1390,4035, # 2352
1741,4036,3857,4037,5278, 236,3858,2453,3304,5279,5280,3723,3859,1273,3860,4625, # 2368
5281, 308,5282,4626, 245,4627,1852,2480,1307,2583, 430, 715,2137,2454,5283, 270, # 2384
 199,2883,4038,5284,3606,2727,1753, 761,1754, 725,1661,1841,4628,3487,3724,5285, # 2400
5286, 587,  14,3305, 227,2608, 326, 480,2270, 943,2765,3607, 291, 650,1884,5287, # 2416
1702,1226, 102,1547,  62,3488, 904,4629,3489,1164,4294,5288,5289,1224,1548,2766, # 2432
 391, 498,1493,5290,1386,1419,5291,2056,1177,4630, 813, 880,1081,2368, 566,1145, # 2448
4631,2291,1001,1035,2566,2609,2242, 394,1286,5292,5293,2069,5294,  86,1494,1730, # 2464
4039, 491,1588, 745, 897,2963, 843,3377,4040,2767,2884,3306,1768, 998,2221,2070, # 2480
 397,1827,1195,1970,3725,3011,3378, 284,5295,3861,2507,2138,2120,1904,5296,4041, # 2496
2151,4042,4295,1036,3490,1905, 114,2567,4296, 209,1527,5297,5298,2964,2844,2635, # 2512
2390,2728,3164, 812,2568,5299,3307,5300,1559, 737,1885,3726,1210, 885,  28,2695, # 2528
3608,3862,5301,4297,1004,1780,4632,5302, 346,1982,2222,2696,4633,3863,1742, 797, # 2544
1642,4043,1934,1072,1384,2152, 896,4044,3308,3727,3228,2885,3609,5303,2569,1959, # 2560
4634,2455,1786,5304,5305,5306,4045,4298,1005,1308,3728,4299,2729,4635,4636,1528, # 2576
2610, 161,1178,4300,1983, 987,4637,1101,4301, 631,4046,1157,3229,2425,1343,1241, # 2592
1016,2243,2570, 372, 877,2344,2508,1160, 555,1935, 911,4047,5307, 466,1170, 169, # 2608
1051,2921,2697,3729,2481,3012,1182,2012,2571,1251,2636,5308, 992,2345,3491,1540, # 2624
2730,1201,2071,2406,1997,2482,5309,4638, 528,1923,2191,1503,1874,1570,2369,3379, # 2640
3309,5310, 557,1073,5311,1828,3492,2088,2271,3165,3059,3107, 767,3108,2799,4639, # 2656
1006,4302,4640,2346,1267,2179,3730,3230, 778,4048,3231,2731,1597,2667,5312,4641, # 2672
5313,3493,5314,5315,5316,3310,2698,1433,3311, 131,  95,1504,4049, 723,4303,3166, # 2688
1842,3610,2768,2192,4050,2028,2105,3731,5317,3013,4051,1218,5318,3380,3232,4052, # 2704
4304,2584, 248,1634,3864, 912,5319,2845,3732,3060,3865, 654,  53,5320,3014,5321, # 2720
1688,4642, 777,3494,1032,4053,1425,5322, 191, 820,2121,2846, 971,4643, 931,3233, # 2736
 135, 664, 783,3866,1998, 772,2922,1936,4054,3867,4644,2923,3234, 282,2732, 640, # 2752
1372,3495,1127, 922, 325,3381,5323,5324, 711,2045,5325,5326,4055,2223,2800,1937, # 2768
4056,3382,2224,2255,3868,2305,5327,4645,3869,1258,3312,4057,3235,2139,2965,4058, # 2784
4059,5328,2225, 258,3236,4646, 101,1227,5329,3313,1755,5330,1391,3314,5331,2924, # 2800
2057, 893,5332,5333,5334,1402,4305,2347,5335,5336,3237,3611,5337,5338, 878,1325, # 2816
1781,2801,4647, 259,1385,2585, 744,1183,2272,4648,5339,4060,2509,5340, 684,1024, # 2832
4306,5341, 472,3612,3496,1165,3315,4061,4062, 322,2153, 881, 455,1695,1152,1340, # 2848
 660, 554,2154,4649,1058,4650,4307, 830,1065,3383,4063,4651,1924,5342,1703,1919, # 2864
5343, 932,2273, 122,5344,4652, 947, 677,5345,3870,2637, 297,1906,1925,2274,4653, # 2880
2322,3316,5346,5347,4308,5348,4309,  84,4310, 112, 989,5349, 547,1059,4064, 701, # 2896
3613,1019,5350,4311,5351,3497, 942, 639, 457,2306,2456, 993,2966, 407, 851, 494, # 2912
4654,3384, 927,5352,1237,5353,2426,3385, 573,4312, 680, 921,2925,1279,1875, 285, # 2928
 790,1448,1984, 719,2168,5354,5355,4655,4065,4066,1649,5356,1541, 563,5357,1077, # 2944
5358,3386,3061,3498, 511,3015,4067,4068,3733,4069,1268,2572,3387,3238,4656,4657, # 2960
5359, 535,1048,1276,1189,2926,2029,3167,1438,1373,2847,2967,1134,2013,5360,4313, # 2976
1238,2586,3109,1259,5361, 700,5362,2968,3168,3734,4314,5363,4315,1146,1876,1907, # 2992
4658,2611,4070, 781,2427, 132,1589, 203, 147, 273,2802,2407, 898,1787,2155,4071, # 3008
4072,5364,3871,2803,5365,5366,4659,4660,5367,3239,5368,1635,3872, 965,5369,1805, # 3024
2699,1516,3614,1121,1082,1329,3317,4073,1449,3873,  65,1128,2848,2927,2769,1590, # 3040
3874,5370,5371,  12,2668,  45, 976,2587,3169,4661, 517,2535,1013,1037,3240,5372, # 3056
3875,2849,5373,3876,5374,3499,5375,2612, 614,1999,2323,3877,3110,2733,2638,5376, # 3072
2588,4316, 599,1269,5377,1811,3735,5378,2700,3111, 759,1060, 489,1806,3388,3318, # 3088
1358,5379,5380,2391,1387,1215,2639,2256, 490,5381,5382,4317,1759,2392,2348,5383, # 3104
4662,3878,1908,4074,2640,1807,3241,4663,3500,3319,2770,2349, 874,5384,5385,3501, # 3120
3736,1859,  91,2928,3737,3062,3879,4664,5386,3170,4075,2669,5387,3502,1202,1403, # 3136
3880,2969,2536,1517,2510,4665,3503,2511,5388,4666,5389,2701,1886,1495,1731,4076, # 3152
2370,4667,5390,2030,5391,5392,4077,2702,1216, 237,2589,4318,2324,4078,3881,4668, # 3168
4669,2703,3615,3504, 445,4670,5393,5394,5395,5396,2771,  61,4079,3738,1823,4080, # 3184
5397, 687,2046, 935, 925, 405,2670, 703,1096,1860,2734,4671,4081,1877,1367,2704, # 3200
3389, 918,2106,1782,2483, 334,3320,1611,1093,4672, 564,3171,3505,3739,3390, 945, # 3216
2641,2058,4673,5398,1926, 872,4319,5399,3506,2705,3112, 349,4320,3740,4082,4674, # 3232
3882,4321,3741,2156,4083,4675,4676,4322,4677,2408,2047, 782,4084, 400, 251,4323, # 3248
1624,5400,5401, 277,3742, 299,1265, 476,1191,3883,2122,4324,4325,1109, 205,5402, # 3264
2590,1000,2157,3616,1861,5403,5404,5405,4678,5406,4679,2573, 107,2484,2158,4085, # 3280
3507,3172,5407,1533, 541,1301, 158, 753,4326,2886,3617,5408,1696, 370,1088,4327, # 3296
4680,3618, 579, 327, 440, 162,2244, 269,1938,1374,3508, 968,3063,  56,1396,3113, # 3312
2107,3321,3391,5409,1927,2159,4681,3016,5410,3619,5411,5412,3743,4682,2485,5413, # 3328
2804,5414,1650,4683,5415,2613,5416,5417,4086,2671,3392,1149,3393,4087,3884,4088, # 3344
5418,1076,  49,5419, 951,3242,3322,3323, 450,2850, 920,5420,1812,2805,2371,4328, # 3360
1909,1138,2372,3885,3509,5421,3243,4684,1910,1147,1518,2428,4685,3886,5422,4686, # 3376
2393,2614, 260,1796,3244,5423,5424,3887,3324, 708,5425,3620,1704,5426,3621,1351, # 3392
1618,3394,3017,1887, 944,4329,3395,4330,3064,3396,4331,5427,3744, 422, 413,1714, # 3408
3325, 500,2059,2350,4332,2486,5428,1344,1911, 954,5429,1668,5430,5431,4089,2409, # 3424
4333,3622,3888,4334,5432,2307,1318,2512,3114, 133,3115,2887,4687, 629,  31,2851, # 3440
2706,3889,4688, 850, 949,4689,4090,2970,1732,2089,4335,1496,1853,5433,4091, 620, # 3456
3245, 981,1242,3745,3397,1619,3746,1643,3326,2140,2457,1971,1719,3510,2169,5434, # 3472
3246,5435,5436,3398,1829,5437,1277,4690,1565,2048,5438,1636,3623,3116,5439, 869, # 3488
2852, 655,3890,3891,3117,4092,3018,3892,1310,3624,4691,5440,5441,5442,1733, 558, # 3504
4692,3747, 335,1549,3065,1756,4336,3748,1946,3511,1830,1291,1192, 470,2735,2108, # 3520
2806, 913,1054,4093,5443,1027,5444,3066,4094,4693, 982,2672,3399,3173,3512,3247, # 3536
3248,1947,2807,5445, 571,4694,5446,1831,5447,3625,2591,1523,2429,5448,2090, 984, # 3552
4695,3749,1960,5449,3750, 852, 923,2808,3513,3751, 969,1519, 999,2049,2325,1705, # 3568
5450,3118, 615,1662, 151, 597,4095,2410,2326,1049, 275,4696,3752,4337, 568,3753, # 3584
3626,2487,4338,3754,5451,2430,2275, 409,3249,5452,1566,2888,3514,1002, 769,2853, # 3600
 194,2091,3174,3755,2226,3327,4339, 628,1505,5453,5454,1763,2180,3019,4096, 521, # 3616
1161,2592,1788,2206,2411,4697,4097,1625,4340,4341, 412,  42,3119, 464,5455,2642, # 3632
4698,3400,1760,1571,2889,3515,2537,1219,2207,3893,2643,2141,2373,4699,4700,3328, # 3648
1651,3401,3627,5456,5457,3628,2488,3516,5458,3756,5459,5460,2276,2092, 460,5461, # 3664
4701,5462,3020, 962, 588,3629, 289,3250,2644,1116,  52,5463,3067,1797,5464,5465, # 3680
5466,1467,5467,1598,1143,3757,4342,1985,1734,1067,4702,1280,3402, 465,4703,1572, # 3696
 510,5468,1928,2245,1813,1644,3630,5469,4704,3758,5470,5471,2673,1573,1534,5472, # 3712
5473, 536,1808,1761,3517,3894,3175,2645,5474,5475,5476,4705,3518,2929,1912,2809, # 3728
5477,3329,1122, 377,3251,5478, 360,5479,5480,4343,1529, 551,5481,2060,3759,1769, # 3744
2431,5482,2930,4344,3330,3120,2327,2109,2031,4706,1404, 136,1468,1479, 672,1171, # 3760
3252,2308, 271,3176,5483,2772,5484,2050, 678,2736, 865,1948,4707,5485,2014,4098, # 3776
2971,5486,2737,2227,1397,3068,3760,4708,4709,1735,2931,3403,3631,5487,3895, 509, # 3792
2854,2458,2890,3896,5488,5489,3177,3178,4710,4345,2538,4711,2309,1166,1010, 552, # 3808
 681,1888,5490,5491,2972,2973,4099,1287,1596,1862,3179, 358, 453, 736, 175, 478, # 3824
1117, 905,1167,1097,5492,1854,1530,5493,1706,5494,2181,3519,2292,3761,3520,3632, # 3840
4346,2093,4347,5495,3404,1193,2489,4348,1458,2193,2208,1863,1889,1421,3331,2932, # 3856
3069,2182,3521, 595,2123,5496,4100,5497,5498,4349,1707,2646, 223,3762,1359, 751, # 3872
3121, 183,3522,5499,2810,3021, 419,2374, 633, 704,3897,2394, 241,5500,5501,5502, # 3888
 838,3022,3763,2277,2773,2459,3898,1939,2051,4101,1309,3122,2246,1181,5503,1136, # 3904
2209,3899,2375,1446,4350,2310,4712,5504,5505,4351,1055,2615, 484,3764,5506,4102, # 3920
 625,4352,2278,3405,1499,4353,4103,5507,4104,4354,3253,2279,2280,3523,5508,5509, # 3936
2774, 808,2616,3765,3406,4105,4355,3123,2539, 526,3407,3900,4356, 955,5510,1620, # 3952
4357,2647,2432,5511,1429,3766,1669,1832, 994, 928,5512,3633,1260,5513,5514,5515, # 3968
1949,2293, 741,2933,1626,4358,2738,2460, 867,1184, 362,3408,1392,5516,5517,4106, # 3984
4359,1770,1736,3254,2934,4713,4714,1929,2707,1459,1158,5518,3070,3409,2891,1292, # 4000
1930,2513,2855,3767,1986,1187,2072,2015,2617,4360,5519,2574,2514,2170,3768,2490, # 4016
3332,5520,3769,4715,5521,5522, 666,1003,3023,1022,3634,4361,5523,4716,1814,2257, # 4032
 574,3901,1603, 295,1535, 705,3902,4362, 283, 858, 417,5524,5525,3255,4717,4718, # 4048
3071,1220,1890,1046,2281,2461,4107,1393,1599, 689,2575, 388,4363,5526,2491, 802, # 4064
5527,2811,3903,2061,1405,2258,5528,4719,3904,2110,1052,1345,3256,1585,5529, 809, # 4080
5530,5531,5532, 575,2739,3524, 956,1552,1469,1144,2328,5533,2329,1560,2462,3635, # 4096
3257,4108, 616,2210,4364,3180,2183,2294,5534,1833,5535,3525,4720,5536,1319,3770, # 4112
3771,1211,3636,1023,3258,1293,2812,5537,5538,5539,3905, 607,2311,3906, 762,2892, # 4128
1439,4365,1360,4721,1485,3072,5540,4722,1038,4366,1450,2062,2648,4367,1379,4723, # 4144
2593,5541,5542,4368,1352,1414,2330,2935,1172,5543,5544,3907,3908,4724,1798,1451, # 4160
5545,5546,5547,5548,2936,4109,4110,2492,2351, 411,4111,4112,3637,3333,3124,4725, # 4176
1561,2674,1452,4113,1375,5549,5550,  47,2974, 316,5551,1406,1591,2937,3181,5552, # 4192
1025,2142,3125,3182, 354,2740, 884,2228,4369,2412, 508,3772, 726,3638, 996,2433, # 4208
3639, 729,5553, 392,2194,1453,4114,4726,3773,5554,5555,2463,3640,2618,1675,2813, # 4224
 919,2352,2975,2353,1270,4727,4115,  73,5556,5557, 647,5558,3259,2856,2259,1550, # 4240
1346,3024,5559,1332, 883,3526,5560,5561,5562,5563,3334,2775,5564,1212, 831,1347, # 4256
4370,4728,2331,3909,1864,3073, 720,3910,4729,4730,3911,5565,4371,5566,5567,4731, # 4272
5568,5569,1799,4732,3774,2619,4733,3641,1645,2376,4734,5570,2938, 669,2211,2675, # 4288
2434,5571,2893,5572,5573,1028,3260,5574,4372,2413,5575,2260,1353,5576,5577,4735, # 4304
3183, 518,5578,4116,5579,4373,1961,5580,2143,4374,5581,5582,3025,2354,2355,3912, # 4320
 516,1834,1454,4117,2708,4375,4736,2229,2620,1972,1129,3642,5583,2776,5584,2976, # 4336
1422, 577,1470,3026,1524,3410,5585,5586, 432,4376,3074,3527,5587,2594,1455,2515, # 4352
2230,1973,1175,5588,1020,2741,4118,3528,4737,5589,2742,5590,1743,1361,3075,3529, # 4368
2649,4119,4377,4738,2295, 895, 924,4378,2171, 331,2247,3076, 166,1627,3077,1098, # 4384
5591,1232,2894,2231,3411,4739, 657, 403,1196,2377, 542,3775,3412,1600,4379,3530, # 4400
5592,4740,2777,3261, 576, 530,1362,4741,4742,2540,2676,3776,4120,5593, 842,3913, # 4416
5594,2814,2032,1014,4121, 213,2709,3413, 665, 621,4380,5595,3777,2939,2435,5596, # 4432
2436,3335,3643,3414,4743,4381,2541,4382,4744,3644,1682,4383,3531,1380,5597, 724, # 4448
2282, 600,1670,5598,1337,1233,4745,3126,2248,5599,1621,4746,5600, 651,4384,5601, # 4464
1612,4385,2621,5602,2857,5603,2743,2312,3078,5604, 716,2464,3079, 174,1255,2710, # 4480
4122,3645, 548,1320,1398, 728,4123,1574,5605,1891,1197,3080,4124,5606,3081,3082, # 4496
3778,3646,3779, 747,5607, 635,4386,4747,5608,5609,5610,4387,5611,5612,4748,5613, # 4512
3415,4749,2437, 451,5614,3780,2542,2073,4388,2744,4389,4125,5615,1764,4750,5616, # 4528
4390, 350,4751,2283,2395,2493,5617,4391,4126,2249,1434,4127, 488,4752, 458,4392, # 4544
4128,3781, 771,1330,2396,3914,2576,3184,2160,2414,1553,2677,3185,4393,5618,2494, # 4560
2895,2622,1720,2711,4394,3416,4753,5619,2543,4395,5620,3262,4396,2778,5621,2016, # 4576
2745,5622,1155,1017,3782,3915,5623,3336,2313, 201,1865,4397,1430,5624,4129,5625, # 4592
5626,5627,5628,5629,4398,1604,5630, 414,1866, 371,2595,4754,4755,3532,2017,3127, # 4608
4756,1708, 960,4399, 887, 389,2172,1536,1663,1721,5631,2232,4130,2356,2940,1580, # 4624
5632,5633,1744,4757,2544,4758,4759,5634,4760,5635,2074,5636,4761,3647,3417,2896, # 4640
4400,5637,4401,2650,3418,2815, 673,2712,2465, 709,3533,4131,3648,4402,5638,1148, # 4656
 502, 634,5639,5640,1204,4762,3649,1575,4763,2623,3783,5641,3784,3128, 948,3263, # 4672
 121,1745,3916,1110,5642,4403,3083,2516,3027,4132,3785,1151,1771,3917,1488,4133, # 4688
1987,5643,2438,3534,5644,5645,2094,5646,4404,3918,1213,1407,2816, 531,2746,2545, # 4704
3264,1011,1537,4764,2779,4405,3129,1061,5647,3786,3787,1867,2897,5648,2018, 120, # 4720
4406,4407,2063,3650,3265,2314,3919,2678,3419,1955,4765,4134,5649,3535,1047,2713, # 4736
1266,5650,1368,4766,2858, 649,3420,3920,2546,2747,1102,2859,2679,5651,5652,2000, # 4752
5653,1111,3651,2977,5654,2495,3921,3652,2817,1855,3421,3788,5655,5656,3422,2415, # 4768
2898,3337,3266,3653,5657,2577,5658,3654,2818,4135,1460, 856,5659,3655,5660,2899, # 4784
2978,5661,2900,3922,5662,4408, 632,2517, 875,3923,1697,3924,2296,5663,5664,4767, # 4800
3028,1239, 580,4768,4409,5665, 914, 936,2075,1190,4136,1039,2124,5666,5667,5668, # 4816
5669,3423,1473,5670,1354,4410,3925,4769,2173,3084,4137, 915,3338,4411,4412,3339, # 4832
1605,1835,5671,2748, 398,3656,4413,3926,4138, 328,1913,2860,4139,3927,1331,4414, # 4848
3029, 937,4415,5672,3657,4140,4141,3424,2161,4770,3425, 524, 742, 538,3085,1012, # 4864
5673,5674,3928,2466,5675, 658,1103, 225,3929,5676,5677,4771,5678,4772,5679,3267, # 4880
1243,5680,4142, 963,2250,4773,5681,2714,3658,3186,5682,5683,2596,2332,5684,4774, # 4896
5685,5686,5687,3536, 957,3426,2547,2033,1931,2941,2467, 870,2019,3659,1746,2780, # 4912
2781,2439,2468,5688,3930,5689,3789,3130,3790,3537,3427,3791,5690,1179,3086,5691, # 4928
3187,2378,4416,3792,2548,3188,3131,2749,4143,5692,3428,1556,2549,2297, 977,2901, # 4944
2034,4144,1205,3429,5693,1765,3430,3189,2125,1271, 714,1689,4775,3538,5694,2333, # 4960
3931, 533,4417,3660,2184, 617,5695,2469,3340,3539,2315,5696,5697,3190,5698,5699, # 4976
3932,1988, 618, 427,2651,3540,3431,5700,5701,1244,1690,5702,2819,4418,4776,5703, # 4992
3541,4777,5704,2284,1576, 473,3661,4419,3432, 972,5705,3662,5706,3087,5707,5708, # 5008
4778,4779,5709,3793,4145,4146,5710, 153,4780, 356,5711,1892,2902,4420,2144, 408, # 5024
 803,2357,5712,3933,5713,4421,1646,2578,2518,4781,4782,3934,5714,3935,4422,5715, # 5040
2416,3433, 752,5716,5717,1962,3341,2979,5718, 746,3030,2470,4783,4423,3794, 698, # 5056
4784,1893,4424,3663,2550,4785,3664,3936,5719,3191,3434,5720,1824,1302,4147,2715, # 5072
3937,1974,4425,5721,4426,3192, 823,1303,1288,1236,2861,3542,4148,3435, 774,3938, # 5088
5722,1581,4786,1304,2862,3939,4787,5723,2440,2162,1083,3268,4427,4149,4428, 344, # 5104
1173, 288,2316, 454,1683,5724,5725,1461,4788,4150,2597,5726,5727,4789, 985, 894, # 5120
5728,3436,3193,5729,1914,2942,3795,1989,5730,2111,1975,5731,4151,5732,2579,1194, # 5136
 425,5733,4790,3194,1245,3796,4429,5734,5735,2863,5736, 636,4791,1856,3940, 760, # 5152
1800,5737,4430,2212,1508,4792,4152,1894,1684,2298,5738,5739,4793,4431,4432,2213, # 5168
 479,5740,5741, 832,5742,4153,2496,5743,2980,2497,3797, 990,3132, 627,1815,2652, # 5184
4433,1582,4434,2126,2112,3543,4794,5744, 799,4435,3195,5745,4795,2113,1737,3031, # 5200
1018, 543, 754,4436,3342,1676,4796,4797,4154,4798,1489,5746,3544,5747,2624,2903, # 5216
4155,5748,5749,2981,5750,5751,5752,5753,3196,4799,4800,2185,1722,5754,3269,3270, # 5232
1843,3665,1715, 481, 365,1976,1857,5755,5756,1963,2498,4801,5757,2127,3666,3271, # 5248
 433,1895,2064,2076,5758, 602,2750,5759,5760,5761,5762,5763,3032,1628,3437,5764, # 5264
3197,4802,4156,2904,4803,2519,5765,2551,2782,5766,5767,5768,3343,4804,2905,5769, # 5280
4805,5770,2864,4806,4807,1221,2982,4157,2520,5771,5772,5773,1868,1990,5774,5775, # 5296
5776,1896,5777,5778,4808,1897,4158, 318,5779,2095,4159,4437,5780,5781, 485,5782, # 5312
 938,3941, 553,2680, 116,5783,3942,3667,5784,3545,2681,2783,3438,3344,2820,5785, # 5328
3668,2943,4160,1747,2944,2983,5786,5787, 207,5788,4809,5789,4810,2521,5790,3033, # 5344
 890,3669,3943,5791,1878,3798,3439,5792,2186,2358,3440,1652,5793,5794,5795, 941, # 5360
2299, 208,3546,4161,2020, 330,4438,3944,2906,2499,3799,4439,4811,5796,5797,5798, # 5376
)
# fmt: on
