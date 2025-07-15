from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguegamefinder, playercareerstats
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import datetime

from pandas import DataFrame

def mainDashboard():

    # def get_temporada_atual():
    #     return f"{datetime.datetime.now().year}-1" if datetime.datetime.now().month < 6 else f"{datetime.datetime.now().year}-2"

    # ano_corrente = get_temporada_atual()

    def get_logo_nba():
        return "https://cdn.nba.com/logos/leagues/logo-nba.svg"

    def get_logo_time(id_time):
        return f"https://cdn.nba.com/logos/nba/{id_time}/global/L/logo.svg"


    logo_nba = get_logo_nba()
    st.image(logo_nba, width=100)
    st.title("Dashboard NBA")

    # Extraindo dados da api
    times = teams.get_teams()
    jogadores = players.get_players()
    # gamefinder = leaguegamefinder.LeagueGameFinder(season=ano_corrente)

    # DataFrames
    df_times = pd.DataFrame(times)
    df_jogadores = pd.DataFrame(jogadores)
    df_games = leaguegamefinder.LeagueGameFinder().get_data_frames()[0]

    # Auxiliadores
    # temp_regular = df_games[df_games['season_type'] == 'Regular']

    # Sidebar para filtros
    st.sidebar.header("Filtros")
    time_selecionado = st.sidebar.selectbox(
        "Selecione o time",
        df_times['full_name'].values)

    temporada_selecionada = st.sidebar.selectbox(
        "Selecione a temporada",
        ['Regular', 'Playoffs', 'Pré-temporada'],
    )

    # Principal
    logo_time = get_logo_time(df_times['id'])
    st.header(f"Análise do {time_selecionado}")
    st.image(logo_time, width=200)


    # Criando abas
    tab1, tab2, tab3 = st.tabs([
        '📊 Visão geral',
        '🏀 Estatísticas',
        'Gráficos',
        ]
    )

    # Conteúdo das abas
    with tab1:
        tabs_1 = st.tabs(['Jogador'])
        with tabs_1[0]:
            list_jogadores = df_jogadores[df_jogadores[''] == time_selecionado]






if __name__ == "__main__":
    mainDashboard()