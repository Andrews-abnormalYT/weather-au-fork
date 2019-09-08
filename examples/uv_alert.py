from weather import uv_index

obs = uv_index.UvIndex('Vic')
print(obs.acknowedgment)

for area in obs.area():

    aac = area['aac']                                  
    description = area['description']
    print(f'{aac} {description}')

# VIC_PT042 Melbourne
print(obs.uv_alert('VIC_PT042'))
