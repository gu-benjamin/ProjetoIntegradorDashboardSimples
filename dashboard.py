# pip install dash
# pip install pandas
# pip install openpyxl

# Estrutura
# Layout -> Tudo que vai ser visualizado
# Callbacks -> Funcionalidades que você terá do dash

from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel('Vendas.xlsx')
# Esta linha lê o arquivo Excel e armazena os dados em uma variável chamada df

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

opcoes = list(df['ID Loja'].unique())
# Esta linha cria uma lista contendo todos os valores unicos da coluna "ID Loja"

opcoes.append("Todas as Lojas")
# Esta linha adiciona a string "Todas as Lojas" ao final da lista de opcoes

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com faturamento de todos os produtos separados por loja'),
    dcc.Dropdown(opcoes, value='Todas as lojas', id='lista_lojas'),
    
    dcc.Graph(
        id='grafico_quantidade_produto',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_produto', 'figure'),
    Input('lista_lojas', 'value')
)

def update_output(value):
    if value == 'Todas as Lojas':
        fig = px.bar(df, x='Produto', y='Quantidade', color='ID Loja', barmode='group')
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x='Produto', y='Quantidade', color='ID Loja', barmode='group')
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)