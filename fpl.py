import requests
import pandas as pd
import numpy as np

import pandas as pd

prem_table = pd.read_html('https://www.bbc.co.uk/sport/football/premier-league/table')
prem_table = prem_table[0]

prem_table = prem_table.drop(['Unnamed: 1'], axis=1)
prem_table.rename(columns={'Unnamed: 0':'Position'}, inplace=True)
prem_table.drop(prem_table.tail(1).index, inplace=True)
prem_table = prem_table[['Position', 'Team', 'P', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts']]
print(len("Crystal Palace"))

# url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

# r = requests.get(url)
# json = r.json()

# elements_df = pd.DataFrame(json['elements'])
# elements_type = pd.DataFrame(json['element_types'])
# teams_df = pd.DataFrame(json['teams'])
# teams_df = teams_df[['name', 'code', 'draw', 'form', 'id', 'loss', 'played', 'points',
#        'position', 'short_name', 'strength', 'team_division', 'unavailable',
#        'win', 'strength_overall_home', 'strength_overall_away',
#        'strength_attack_home', 'strength_attack_away', 'strength_defence_home',
#        'strength_defence_away', 'pulse_id']]


# # slim_elements_df = elements_df[['second_name','team','element_type','selected_by_percent',
# #     'now_cost','minutes','transfers_in','value_season','total_points']]
# # slim_elements_df['position'] = slim_elements_df.element_type.map(elements_type.set_index('id').singular_name)
# # slim_elements_df['team'] =  slim_elements_df.team.map(teams_df.set_index('id').name)
# # slim_elements_df['value'] = slim_elements_df.value_season.astype(float)

# # slim_elements_df = slim_elements_df.loc[slim_elements_df.value > 0]
# # pivot = slim_elements_df.pivot_table(index='position',values='value',aggfunc=np.mean).reset_index()
# # team_pivot = slim_elements_df.pivot_table(index='team',values='value',aggfunc=np.mean).reset_index()
# # team_pivot.sort_values('value',ascending=False)
# print(teams_df.loc[teams_df['name'] == 'Chelsea']['draw'])




