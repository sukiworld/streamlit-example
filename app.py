#%%
import streamlit as st
from utils.utils import read_json, download_df, plot_candle
from utils.utils_fdr import get_comp_info, get_stock_data
import pandas as pd
import json 
import requests
import numpy as np
import warnings
from PIL import Image
import time
import altair as alt
import plotly.express as px

warnings.filterwarnings("ignore", category=FutureWarning)

#%%
()

menu_items = {
    'Get help' : 'https://github.com/sukiworld/pretotype_nftpjt',
    'Report a bug' : 'https://github.com/sukiworld/pretotype_nftpjt/issues',
    'About' : '''
    ## opensea nft project
    Download stock price data in US, South Korean stock market
    '''
}

# data = load_data(10)
st.set_page_config(
    page_title="NFT Project Comparison",
    page_icon="💛",
    layout="centered",
)


st.title('🧪 Welcome to NFTBank DS Labs')
st.subheader("🕵🏻 Search for NFT projects and Check their trend")
st.text('plz ping us in the discord if you have any questions')
st.markdown(
    """<a style='display: block; text-align: center;' href="https://discord.gg/by85HJ7J92">Let's go to NFTBank Discord!</a>
    """,
    unsafe_allow_html=True,
)
# data_load_state = st.text('Loading data...')
# data_load_state.text("Done! (using st.cache)")
st.text(' \n \n \n \n ')
st.text(' \n \n \n \n ')

st.subheader("1. Find an official collection name in here ")
st.image('https://github.com/sukiworld/pretotype_nftpjt/blob/master/example_pic.png?raw=true')
st.markdown("<div align= 'center'> ▲ this is an example image </div>", unsafe_allow_html=True)
st.markdown(
    """<a style='display: block; text-align: center;' href="https://opensea.io/"> Opensea link</a>
    """,
    unsafe_allow_html=True,
)
st.text(' \n \n \n \n ')
st.text(' \n \n \n \n ')

st.subheader("2. Type the collection name in the box")
# user_input = st.text_input("⚠️ opensea official collection name only!", 'doodles-official')
user_input = st.text_input("⚠️ opensea official collection name only! Check the example collection below", 'doodles-official, playboyrabbitars, boredapeyachtclub')

@st.cache(allow_output_mutation=True)
def load_data(user_input):
    final_df = pd.DataFrame()
    user_input = user_input.replace(" ", "")
    split_word = user_input.split(',')
    res = len(split_word)
    for i in range(res):
        final_df["collection"] = user_input
        url = "https://api.opensea.io/api/v1/collection/"+split_word[i]+"/stats"
        r = requests.get(url) 
        j = json.loads(r.text)
        df =  pd.json_normalize(j)
        final_df = final_df.append(df)
    return final_df, split_word

data, split_word = load_data(user_input)
data["collection"] = split_word

with st.spinner('Take a deep breath and feel happy'):
    time.sleep(5)
st.success('Done!')

st.text(' \n \n \n \n ')
st.text(' \n \n \n \n ')
st.text(' \n \n \n \n ')
st.text(' \n \n \n \n ')
# st.dataframe(data)

cc = data[['collection','stats.total_volume']]
st.text('📊 Total volume for each project')
fig = px.bar(cc, x='collection', y='stats.total_volume')
st.plotly_chart(fig, use_container_width=True)


st.text('💛 Volume for each project')

change_col = ['collection'] + data.filter(like='volume').columns.tolist()
change_df = data[change_col]
st.dataframe(change_df)

st.text('💛 Volume change rate for each project')
change_col = ['collection'] + data.filter(like='change').columns.tolist()
change_df = data[change_col]
st.dataframe(change_df)



# st.bar_chart(data = data[['collection','stats.one_day_change']], x = data["collection"], y = data["stats.one_day_change"])





# chart = (
#     alt.Chart(cc)
#     .mark_bar()
#     .encode(
#         x=alt.X("stats.one_day_change"),
#         y=alt.Y("collection"),
#         # color=alt.Color("variable", type="nominal", title=""),
#         # order=alt.Order("variable", sort="descending"),
#     )
# )

# st.altair_chart(chart, use_container_width=True)


# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)

#%%
# @st.cache(suppress_st_warning=True, show_spinner=False)
# def load_comp_list():
#     stock_const = read_json('resource/stock_list.json')
#     return stock_const


# def get_target_comp_info(comp_info_all: dict):
#     # split view into 2 columns
#     col1, col2 = st.columns([3, 3])

#     # first col for selecting target country
#     country = col1.radio("Select country", comp_info_all.keys())

#     # second col for selecting target stock market
#     market = col2.radio("Select market", comp_info_all[country].keys())

#     # select company name from dropdown select box
#     company = st.selectbox('Select company', comp_info_all[country][market].keys())
#     comp_info = comp_info_all[country][market][company]

#     return comp_info



# def main():
#     st.title("NFT Collections Stats")
#     # stock_list = load_comp_list()

#     # comp_info = get_target_comp_info(stock_list)
#     # num_month = st.slider('Select months', 1, 36, step=3)
    
#     try:
#         # data = get_stock_data(comp_info, days = num_month*30)
#         data = final_df.copy()

#     except ValueError:
#         # st.warning("Company '{}' information currently not avaliable".format(comp_info['Symbol']))        
    
#     else:
        
#         # st.markdown("**Stock data ({} months) : {} ({})**".format(num_month, comp_info['Name'], comp_info['Symbol']))
#         # plot_candle(data)
#         # filename = 'stockprice_{}_{}_{}m'.format(comp_info['Symbol'], comp_info['Name'], num_month)
#         # st.dataframe(data)
#         # download_df(data, filename)


# if __name__ == "__main__":
#     st.set_page_config(menu_items=menu_items)
#     main()