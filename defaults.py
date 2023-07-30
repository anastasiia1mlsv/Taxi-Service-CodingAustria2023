# +
NODES = ['Bahnhof Bruck Fusch',
         'Maishofen',
         'Großberghof',
         'ÖTK - Statzerhaus', 
         'Hinterthal', 
         'Saalbach-Hinterglemm']

EDGES = [{'Nodes': ['Bahnhof Bruck Fusch', 'Maishofen'], 'Distance': 12},
         {'Nodes': ['Bahnhof Bruck Fusch', 'Großberghof'], 'Distance': 9},
         {'Nodes': ['Großberghof', 'ÖTK - Statzerhaus'], 'Distance': 42},
         {'Nodes': ['Bahnhof Bruck Fusch', 'ÖTK - Statzerhaus'], 'Distance': 48},
         {'Nodes': ['Maishofen', 'Hinterthal'], 'Distance': 24},
         {'Nodes': ['Maishofen', 'Saalbach-Hinterglemm'], 'Distance': 15},
         {'Nodes': ['Maishofen', 'ÖTK - Statzerhaus'], 'Distance': 55},
         {'Nodes': ['Hinterthal', 'ÖTK - Statzerhaus'], 'Distance': 41}]

PASSANGERS = [{'Name': 'John', 'Start': 'Bahnhof Bruck Fusch', 'Target': 'Maishofen'},
              {'Name': 'Lukas', 'Start': 'Bahnhof Bruck Fusch', 'Target': 'Großberghof'},
              {'Name': 'Sandra', 'Start': 'Bahnhof Bruck Fusch', 'Target': 'ÖTK - Statzerhaus'},
              {'Name': 'Anton', 'Start': 'Bahnhof Bruck Fusch', 'Target': 'Hinterthal'},
              {'Name': 'Lisa', 'Start': 'Bahnhof Bruck Fusch', 'Target': 'Saalbach-Hinterglemm'}]
