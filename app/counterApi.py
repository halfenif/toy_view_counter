# Load .env
from env import Settings
config = Settings()

from os.path import join
import svgwrite


from dbApi import sql_get_count_by_uuid

def get_counter_by_uuid(uuid: str, Referer: str):
    countNumber = sql_get_count_by_uuid(uuid, Referer)
    
    if countNumber:
        countStr = f'Read Count : [{countNumber}]'
    else:
        countStr = 'Read Count Fail!'
    
    if config.IS_DEBUG:
        datafolder = 'data/svgfile'
    else:
        datafolder = '/app/data/svgfile'

    filename =  join(datafolder, f'{uuid}.svg')
    dwg = svgwrite.Drawing(filename, (150,20))
    dwg.add(dwg.text(countStr, insert=(0, 13), fill='black'))
    dwg.add(dwg.rect(insert=(0, 0), 
                     size=('300px','300px'), 
                     fill='yellow', 
                     fill_opacity=0.4,
                    #  stroke=svgwrite.rgb(255, 0, 0, '%'),  # Red stroke
                    #  stroke_width=5,
                    #  stroke_opacity=0.6
                     ))
    dwg.save()    
    
    return filename    
