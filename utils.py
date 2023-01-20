import re
s1 = 'terça das 21:00 às 23:00, semanal ; quinta das 18:00 às 21:00, quinzenal I'
s2 = 'quinta das 18:00 às 21:00, quinzenal II'

# concatena duas strings utilizando como separador ' ; ', conforme o padrão que a prograd segue
# pode ser usado em casos que há horários em células diferentes (teorico/pratico)
def ConcatCampos(s1, s2):
    return s1 + ' ; ' + s2

"""
recebe a string contendo informações sobre o horário das aulas e transforma em um dict
------------------------------------------------------------------------------------------------
input = 'terça das 21:00 às 23:00, semanal ; quinta das 18:00 às 21:00, quinzenal I'
output = {
    'aula1': 
        {'sDiaDaSemana': 'terça', 'sPeriodo': '21:00 às 23:00', 'sFrequencia': 'semanal'},
    'aula2': 
        {'sDiaDaSemana': 'quinta', 'sPeriodo': '18:00 às 21:00', 'sFrequencia': 'quinzenal I'},
    }
"""
def GetHorarioDict(sHorarios):
    tHorarios = sHorarios.split(' ; ')
    dRes = {}
    i = 1
    for Horario in tHorarios:
        aula = f"aula{i}"
        dRes[aula] = {}

        dRes[aula]['sDiaDaSemana'] = re.search('^(segunda|terça|quarta|quinta|sexta)', Horario).group()
        dRes[aula]['sPeriodo'] = re.search('([0-2][0-9]:00 às [0-2][0-9]:00)', Horario).group()
        dRes[aula]['sFrequencia'] = re.search('(semanal|quinzenal (II?))$', Horario).group()
        i += 1
    return dRes

print(GetHorarioDict(ConcatCampos(s1, s2)))