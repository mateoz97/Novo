
class structureData:

    def __init__(self):
        self.path = {'ab':r'C:\Users\mateo\Documents\NovoAuto\NovoAuto\Input\AB.xlsx',
                     're':r'C:\Users\mateo\Documents\NovoAuto\NovoAuto\Input\RE.xlsx',
                     'qu':r'C:\Users\mateo\Documents\NovoAuto\NovoAuto\Input\QUOTA.xlsx'}
                     
        self.pathN8 = {'ab':r'C:\Users\mateo\Documents\NovoAuto\NovoAuto\Input\N8AB.csv',
                       're':r'C:\Users\mateo\Documents\NovoAuto\NovoAuto\Input\N8RE2.csv'}
        
        self.sheet = {'ab':'NovoSeven_AB_Original',
                      're':'NovoSeven_RE2_Original'}


        self.tipo = {'ab':'AB',
                     're':'RE2'}
        
        self.year = {'ab': {'22' : slice(37,49),
                            '23' : slice(50,62),
                            '24' : slice(63,75),
                            '25' : slice(76,88),
                            '26' : slice(88,100),
                            '27' : slice(100,112)},
                     're': {'22' : slice(40,52),
                            '23' : slice(53,65),
                            '24' : slice(66,78),
                            '25' : slice(79,91),
                            '26' : slice(92,104),
                            '27' : slice(105,117)},
                     'qu': {'22' : slice(40,52),
                            '23' : slice(53,65),
                            '24' : slice(66,78),
                            '25' : slice(79,91),
                            '26' : slice(92,104),
                            '27' : slice(105,117)}}
        
        self.yearN8 = {'22' : slice(16,28),
                       '23' : slice(29,41),
                       '24' : slice(42,54),
                       '25' : slice(56,68),
                       '26' : slice(92,104)}
        
        self.rangeCustoms = {'ab':{'start_act': 222,
                                   'start_des': 575,
                                   'end_act': 580,
                                   'end_des': 603,
                                   'use_type': slice(223,232)},
                             're':{'start_act': 246,
                                   'start_des': 589,
                                   'end_act': 588,
                                   'end_des': 616,
                                   'use_type': slice(247,256)},
                             'qu':{'start_act': 246,
                                   'start_des': 580,
                                   'end_act': 587,
                                   'end_des': 616,
                                   'use_type': slice(247,256)}}
        
        self.rangeCustomsN8 = {'start_act': 126,
                               'end_act':157}
