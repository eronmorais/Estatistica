'''
Dados Numéricos:
1. A Moda
1. A Mediana
1. A média
1. Os Quartis
1. Os 10% maiores
1. Os 5 % Menores
1. O valor máximo
1. O valor mínimo
Dados de Texto
1. A frequência absoluta
1. A frequência relativa
1. A Moda
1. Qual o tipo de Moda?
1. O valor máximo (ordem alfabética)
1. O valor mínimo (ordem alfabética)
'''

import pandas as pd

df = pd.read_csv('Exercicio_estatistica.csv', decimal=',')
print(df)

#Moda
print(f'''
Moda:
1. Nome:{df['Nome'].mode()[0]}
2. Idade:{df['Idade'].mode()[0]}
3. Filhos:{df['Filhos'].mode()[0]}
4. Estado:{df['Estado'].mode()[0]}
5. Altura:{df['Altura'].mode()[0]}
6. Formação:{df['Formação'].mode()[0]}
'''
)

#Mediana
print(f'''
Mediana:
1. Idade:{df['Idade'].median()}
2. Filhos:{df['Filhos'].median()}
3. Altura:{df['Altura'].median()}
'''
)

#Media
print(f'''
Media:
1. Idade:{df['Idade'].mean()}
2. Filhos:{df['Filhos'].mean()}
3. Altura:{df['Altura'].mean()}
'''
)

#Quartis
print(f'''
Quartis:
1. Idade:{df['Idade'].quantile([.25, .5, .75])}
2. Filhos:{df['Filhos'].quantile([.25, .5, .75])}
3. Altura:{df['Altura'].quantile([.25, .5, .75])}
'''
)


#Os 10% maiores
print(f'''
10% maiores:
1. Idade:{df['Idade'].quantile(q=0.9)}
2. Filhos:{df['Filhos'].quantile(q=0.9)}
3. Altura:{df['Altura'].quantile(q=0.9)}
'''
)
#Os 5 % Menores
print(f'''
5% menores:
1. Idade:{df['Idade'].quantile(q=0.05)}
2. Filhos:{df['Filhos'].quantile(q=0.05)}
3. Altura:{df['Altura'].quantile(q=0.05)}
'''
)

#O valor máximo
print(f'''
Valor máximo:
1. Idade:{df['Idade'].max()}
2. Filhos:{df['Filhos'].max()}
3. Altura:{df['Altura'].max()}
'''
)

#O valor mínimo
print(f'''
Valor minimo:
1. Idade:{df['Idade'].min()}
2. Filhos:{df['Filhos'].min()}
3. Altura:{df['Altura'].min()}
'''
)

#Dados de texto

texto = [
    'Nome',
    'Estado',
    'Formação'
]

def tipo_moda(serie):
    qtd = len(serie.mode()) #.shape
    if qtd == 0:
        return 'Sem Moda'
    elif qtd == 1:
        return 'Unimodal'
    elif qtd == 2:
        return 'Bimodal'
    elif qtd > 2:
        return 'Multimodal'
    else:
        return 'Valor inválido'

for col in texto:
    df[col] = df[col].str.lower() # passa tudo para minúsculo
    df[col] = df[col].str.strip() # remove espaços em branco no começo ou final
    print()
    print(col)
    print(f'Frequência Absoluta: ')
    print(f'{df[col].value_counts()}')
    print()
    print(f'Frequência Relativa: ')
    print(f'{df[col].value_counts(normalize=True)}')
    print()
    print(f'Moda: {df[col].mode()[0]}')
    print(f'Mínimo: {df[col].min()}')
    print(f'Máximo: {df[col].max()}')
    print(f'Tipo de Moda: {tipo_moda(df[col])}')

print(df[texto].describe())
