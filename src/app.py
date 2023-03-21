from dash import Dash , html , dcc , Input , Output , State , no_update
import pandas as pd
import base64
# import seaborn as sns
from PIL import Image
import dash_bootstrap_components as dbc


date_data = pd.read_csv( "dates_data.csv" )

app = Dash( __name__ )
server = app.server
########## First Row : title , links, header, graph -- complete #############################
title = html.Div(
    html.Div( className="trend0" ,
              children=[

                  html.H2( 'Capstone Forecasting Dashboard' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,
                               'gridArea': "title"

                               } ,
                           id='dashTitle' ,
                           className="title"
                           ) ,

                  html.H3( 'Problem: High Customer turnover/Low Customer Retention' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,
                               'gridArea': "dashlinks"

                               } ,
                           id='dashlinks' ,
                           className="dashlinks"

                           ) ,
                  html.H5(
                      'Purpose: This is a mutli-class classification problem used to determine customer types based on the following criteria: escalations tickets count, call preptime, scheduled appointment time, unscheduled appointment time, and total number of accounts reconciled.  ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5_title"

                          }
                      ) ,
                  html.H5(
                      'Problem to Solve: Based on my experience as a Escalations representative, I believe there is an issue with customer cancellations.  My goals is to explore the data and try to understand customer behavior.  Assumption: customers are cancelling due to extended cleanup start times from purchase date. To prove this hypothesis, will need to show as date difference decreases, tenure should increase. Limitation: I do not have access to 2022 data. ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5B_title"

                          }
                      ) ,
                    #html.Iframe( src="assets/Presentation1.mp4" ,
                    #             style={"height": "100%", "width": "100%"} )
                  ] ,
              )
    )

crosstab_data_cancel = (date_data.groupby( ['cu_cancel_year' , 'cu_cancel_month'] , as_index=False )
                        .agg( cancel_rec_cnt=('cu_cancel_dt' , 'count')
                              ))

crosstab_data_purchase = (date_data.groupby( ['cu_purchase_year' , 'cu_purchase_month'] , as_index=False )
                          .agg( purchase_rec_cnt=('cu_purchase_dt' , 'count')
                                ))

df_join = crosstab_data_purchase

df_join_df = df_join.join( crosstab_data_cancel , lsuffix='_df1' , rsuffix='_df2' ).head()
# import plotly.express as px
import plotly.graph_objects as go

df_join_fig = go.Figure()
df_join_fig.add_trace(
    go.Bar( x=df_join_df.cu_cancel_year , y=df_join_df.cancel_rec_cnt , name='cancellations' )
    )
df_join_fig.add_trace(
    go.Bar( x=df_join_df.cu_purchase_year , y=df_join_df.purchase_rec_cnt , name='Purchases' )
    )

# df_join_fig.update_layout(height=400, width=550, title='Purchase and Cancellation Activity', yaxis_title="Total",
#                          xaxis_title="Date")

# df_join_fig.show()
df_join_fig = html.Div(
    dcc.Graph( figure=df_join_fig , id="df-join-fig" , style={'gridArea': "df_join_fig"} )

    )
##############################
import plotly.express as px

purchase_figure = px.bar( crosstab_data_purchase , x='cu_purchase_month' , y='purchase_rec_cnt' ,
                          color="cu_purchase_year" ,
                          barmode="group" , )

purchase_fig = html.Div(
    dcc.Graph( figure=purchase_figure , id="purchase_figure" , style={'gridArea': "purchase_fig"} )  #
    )
##############################
cancel_figure = px.bar( crosstab_data_cancel , x='cu_cancel_month' , y='cancel_rec_cnt' , color="cu_cancel_year" ,
                        barmode="group" , )

cancel_fig = html.Div(
    dcc.Graph( figure=cancel_figure , id="cancel_figure" , style={'gridArea': "cancel_fig"} )  #
    )
##############################

links = html.Div(
    html.Div(
        className="trend" ,
        children=[
            html.Br() , html.Br() , html.Br() ,
            html.A( 'Part_1_Proposal.md' ,
                    href="https://git.generalassemb.ly/mfrancis/unit-4-capstone/blob/main/Part_1_Proposal.md" ,
                    style={'gridArea': "link1"} ) , html.Br() ,
            html.A( 'Final_capstone_Part_I_Getting_the_Data.ipynb' ,
                    href="https://git.generalassemb.ly/mfrancis/marlainna-capstone-app/blob/main/Final_capstone_Part_I_Getting_the_Data.ipynb" ,
                    style={'gridArea': "link2"} ) , html.Br() ,
            html.A( 'Final_capstone_Part_II_Modeling.ipynb' ,
                    href="https://git.generalassemb.ly/mfrancis/marlainna-capstone-app/blob/main/Final_capstone_Part_II_Modeling.ipynb" ,
                    style={'gridArea': "link3"} ) , html.Br() ,
            html.A( 'Final_capstone_Part_III_PREP.ipynb' ,
                    href="https://git.generalassemb.ly/mfrancis/marlainna-capstone-app/blob/main/Final_capstone_Part_III_PREP.ipynb" ,
                    style={'gridArea': "link4"} ) , html.Br() ,
            html.A( 'Final_capstone_Part_IIII_Dashboard -Adding Dash and HTML Components' ,
                    href="https://git.generalassemb.ly/mfrancis/marlainna-capstone-app/blob/main/Final_capstone_Part_IIII_Dashboard_Final-Good%20ONLY_02_13.ipynb" ,
                    style={'gridArea': "link5"} ) , html.Br() ,
            html.A( 'Convert *.ipynb file from Part IIII to *.py file.  Editing file using PyCharm community Edition' ,
                    href="https://git.generalassemb.ly/mfrancis/convertPyFiles" ,
                    style={'gridArea': "link6"} ) , html.Br() ,
            html.A(
                'Capstone-Demo Repository- run local for testing.  Editing *.py file using PyCharm community Edition' ,
                href="https://git.generalassemb.ly/mfrancis/marlainna-capstone-app/blob/main/src/app.py" ,
                style={'gridArea': "link7"} ) , html.Br() ,
            html.A(
                'Capstone-Demo Repository- run on Render Server. Moved files to GitHub.  Deployed to Render. ' ,
                href="https://github.com/yourexodus/mfrancis_capstone/blob/main/src/app.py" ,
                style={'gridArea': "link8"} ) , html.Br() ,
            html.A( 'Resource link:  How to deploy using Render' ,
                    href="https://www.youtube.com/watch?v=XWJBJoV5ywwgit " ,
                    style={'gridArea': "link9"} )

            # dcc.Graph( figure=df_join_fig, id="df-join-fig", style={'gridArea': "df_join_fig"} ),
            # give a list of inner elements as the content
            ] ,
        )
    )
########## END OF:  First Row : title , links, header, graph -- complete #############################
shortvideo_item = html.Iframe( src="assets/recordshortVersion.mp4.mp4" ,
                                 style={"height": "800", "width": "800"} )

presentation_item = html.Iframe( src="assets/Presentation1.mp4" ,
                                 style={"height": "800", "width": "800"} )
############## begin correlation graph

################# end correlation graph ################################
my_data = pd.read_csv( "dashboard_data.csv" )
x = my_data.days_diff_purdt_custartdt
y = my_data['tenure']

# create the figure
fig_daydiff = go.Figure()
# add trace adn set mode
fig_daydiff.add_scatter( x=x , y=y , mode="markers" , marker={'color': "forestgreen" , "size": 5} )
# update the layout
fig_daydiff.update_layout( height=400 , width=650 ,
                           title="Capstone: Num Days Between Purchase_dt & CU_Start_Date vs Tenure" ,
                           yaxis_title="tenure" , xaxis_title="Diff: Purchase_dt & CU_Start_dt" )

##############





#########################
correlation_img = Image.open( "assets/CorrelationHeatmap_fig.png" )
correlation_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                            html.H5(
                            'The correlation heatmap illustrates there is a close relationship between variable in red and a more distant relationship between the variables in blue.'
                            'After examaming the heatmap, I identified the following best-performaing variables: rec-acct, non-appt, appt_ci, call-prep, days_diff_purch_custartdt' ,
                            style={
                                'backgroundColor': 'white' ,
                                'fontFamily': 'verdana' ,
                                # 'textAlign':'center',
                                'gridArea': "corr_header"

                                }
                            ) ,
                        html.Img( src=correlation_img , width=840 , height=800 ) ,
                        # using the pillow image variable

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="correlation_id"
    )
correlation_item.style = {'gridArea': "correlation_ga"}



##################

BoxPlot_img = Image.open("assets/BoxPlot_fig.png")
dataStatistics_img = Image.open("assets/dataStatistics.PNG")
purch_cancel_code_img = Image.open( "assets/UnderstandingTheData.png" )
purch_cancel_code_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                        html.H2( 'About the Data' ,
                                 style={
                                     'backgroundColor': 'tan' ,
                                     'fontFamily': 'verdana' ,
                                     'textAlign': 'center' ,
                                     'gridArea': "title"

                                     } ,
                                 id='purchase_Act_code_Title' ,
                                 className="purchase_Act_code_Title "
                                 ) ,
                        html.H5(
                            'This sample dataset has large variances in the data.  Due to limited data access, I am unable to retrieve more data' ,
                            style={
                                'backgroundColor': 'white' ,
                                'fontFamily': 'verdana' ,
                                # 'textAlign':'center',
                                'gridArea': "purchase_Act_code_header"

                                }
                            ) ,
                        html.Img( src=dataStatistics_img , width=600 , height=350 ) ,
                        html.Img( src=BoxPlot_img , width=600 , height=350 ) ,

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="purch_cancel_code_id"
    )
purch_cancel_code_item.style = {'gridArea': "purch_cancel_code_ga"}

###########################
Purchase_activity_desc = html.Div(
    html.Div( className="trend_1" ,
              children=[
                  html.H2( 'Missing Data' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,
                               'gridArea': "title"

                               } ,
                           id='purchase_ActivityTitle' ,
                           className="purchase_ActivityTitle "
                           ) ,
                            html.H5(
                            'Purchase/Cancellation Activity: I used a crosstab query to explore data coverage across multiple years.  I determined several months of data is missing within each year.  '
                            'As a result, this sample dataset is incomplete. Nonetheless, I have completed the capstone using this data '
                            'to demonstrate new skills and tackle a pressing issue relevant to the product I support in my current position.' ,
                            style={
                                'backgroundColor': 'white' ,
                                'fontFamily': 'verdana' ,
                                # 'textAlign':'center',
                                'gridArea': "purchase_Act_code_header"

                                }
                            ) ,
                        #
                        html.Img( src=purch_cancel_code_img , width=750 , height=900 ) ,
                        # using the pillow image variable

                  html.H5(
                      'Purchase Activity: Highest number of purchase was recorded February and March of 2021.  Since March of 2021, purchases have decreased.  ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5_title"

                          }
                      ) ,
                  dcc.Graph( figure=purchase_figure , id="purchase_figure_01" , style={'gridArea': "purchase_fig_01"} )
                  #

                  ,
                  html.H5(
                      'Cancellation Activity:Cancellations continued to increase from March with the exception of July reaching a peak month of canceallation in September of 2021. ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5B_title"

                          }
                      ) ,
                  dcc.Graph( figure=cancel_figure , id="cancel_figure_01" , style={'gridArea': "cancel_fig_01"} )  #
                  ,
                  html.H5(
                      'What is the reason for the cancellations?  Graph shows the shorter the number of days '
                      ' it takes to start cleanup, the longer the customer tenure. Will explore the data for other '
                      'possible reasons for cancellation' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5B_title"

                          }
                      ) ,

                  dcc.Graph( figure=fig_daydiff , id="fig_daydiff_01" , style={'gridArea': "fig_daydiff_01"} )  #

                  ] ,
              )
    )

##### TOP5 #####


top5_df = my_data.head()


def setIndex_to_col(df):
    df.reset_index( drop=True , inplace=True )
    df.index = df.index + 1
    df = df.reset_index()

    return df


top5_df = setIndex_to_col( top5_df )

##############################################
# change columns order
change_col_order = ['index' , 'cu_purchase_dt' , 'cu_start_dt' , 'cu_cancel_dt' ,
                    'days_diff_purdt_custartdt' , 'tenure' ,
                    'esc_ticket_cnt' , 'doc_mgmnt' , 'rec_acct' , 'non_appt_ci' , 'appt_ci' ,
                    'call_prep' , 'y_pred']

top5_df = top5_df[change_col_order]

top5_columns = [{"name": "index" , "id": "index" , "type": "numeric" , "format": {'specifier': ','}} ,
                {"name": "cu_purchase_dt" , "id": "cu_purchase_dt" , "type": "datetime"} ,
                {"name": "cu_start_dt" , "id": "cu_start_dt" , "type": "datetime"} ,
                {"name": "cu_cancel_dt" , "id": "cu_cancel_dt" , "type": "datetime"} ,

                ]

# iterate the remaining columns and append the information about each column
for name in top5_df[5:]:
    col_info = {
        "name": name ,
        "id": name ,
        "type": "numeric" ,
        "format": {'specifier': ','}}

    top5_columns.append( col_info )
top5_data = top5_df.sort_values( "index" , ascending=True ).to_dict( "records" )
# Create Dashtable using dictionary values in top5_data
from dash import dash_table

top5_table = dash_table.DataTable(
    id='top5-table' ,
    columns=top5_columns ,
    data=top5_data ,

    fixed_rows={"headers": True} ,
    active_cell={"row": 0 , "column": 0} ,
    sort_action="native" ,
    derived_virtual_data=top5_data ,
    style_table={
        "minHeight": "40vh" ,
        "height": "40vh" ,
        "overflowY": "scroll"
        } ,
    style_cell={
        "whitespace": "normal" ,
        "height": "auto" ,
        "fontFamily": 14

        } ,
    style_filter={'height': '50px'} ,
    style_header={
        "textAlign": "center" ,
        "fontSize": 14
        } ,
    style_data={
        "fontSize": 12
        } ,
    style_data_conditional=[
        {
            "if": {"column_id": "type_label"} ,
            "width": "120px" ,
            "textAlign": "left" ,
            # "textDecoration": "underline",
            "cursor": "pointer"
            } ,
        {  # every other row change back ground color
            "if": {"row_index": "odd"} ,
            "backgroundColor": "#fafbfb"
            }
        ] ,
    )
#################################
################################################
extract_feature_data = my_data.loc[: ,
                       ['tenure' , 'esc_ticket_cnt' , 'doc_mgmnt' , 'rec_acct' , 'non_appt_ci' , 'appt_ci' ,
                        'call_prep']].head()

extract_feature_df = setIndex_to_col( extract_feature_data )
extract_feature_columns = []
for name in extract_feature_df[3:]:
    mycol_info = {
        "name": name ,
        "id": name ,
        "type": "numeric" ,
        "format": {'specifier': ','}}

    extract_feature_columns.append( mycol_info )
extract_feature_data = extract_feature_df.sort_values( "index" , ascending=True ).to_dict( "records" )
extract_feature_table = dash_table.DataTable(
    id='extract_feature-table' ,
    columns=extract_feature_columns ,
    data=extract_feature_data ,

    fixed_rows={"headers": True} ,
    active_cell={"row": 0 , "column": 0} ,
    sort_action="native" ,
    derived_virtual_data=extract_feature_data ,
    style_table={
        "minHeight": "40vh" ,
        "height": "40vh" ,
        "overflowY": "scroll"
        } ,
    style_cell={
        "whitespace": "normal" ,
        "height": "auto" ,
        "fontFamily": 14

        } ,
    style_filter={'height': '50px'} ,
    style_header={
        "textAlign": "center" ,
        "fontSize": 14
        } ,
    style_data={
        "fontSize": 12
        } ,
    style_data_conditional=[
        {
            "if": {"column_id": "type_label"} ,
            "width": "120px" ,
            "textAlign": "left" ,
            # "textDecoration": "underline",
            "cursor": "pointer"
            } ,
        {  # every other row change back ground color
            "if": {"row_index": "odd"} ,
            "backgroundColor": "#fafbfb"
            }
        ] ,
    )
##################################
# set style as a dictionary
title7 = html.H3( 'Cleaned Data' ,
                  style={
                      'backgroundColor': 'tan' ,
                      'fontFamily': 'verdana' ,
                      'textAlign': 'center' ,

                      } ,
                  id='dashTitle7' ,
                  className="title7"
                  )

text7 = html.Textarea(
    "Notes:\nBasis of Prediction: Tenure\n\nPost EDA\nStep 1:Dropped Missing Values\nStep 2: Merged Files\nStep 3:Converted Data Type\nStep 4: Deleted Duplicates\n\nReference:Final_capstone_Part_I_Getting_the_Data"
    , style={
        'width': '100%' ,
        'height': 300 ,
        'backgroundColor': 'tan' ,
        'fontFamily': 'verdana' ,
        'textAlign': 'center' ,

        } ,
    id='text7' ,
    className="text7"
    )

# text7
text7.style = {'gridArea': "text7"}


# import dash_core_components as dcc


# import dash_core_components as dcc

def create_tab_top5():
    return dbc.Tab(
        top5_table ,
        label="Top 5 records" ,
        # value="top5",
        className="single-tab" ,
        id="top5-tab" ,
        # selected_className="single-tab--selected",
        style={'gridArea': "top5_table"}
        )


# first I added it to a tab

top5_tab = create_tab_top5()

###  END OF top5 ########
#### Matrix ######################################

df = my_data

# reference:https://plotly.com/python/splom/
# Define indices corresponding to flower categories, using pandas label encoding
index_vals = df['type_label'].astype( 'category' ).cat.codes

fig = go.Figure( data=go.Splom(
    dimensions=[dict( label='doc_mgmnt' ,
                      values=df['doc_mgmnt'] ) ,
                dict( label='rec_acct' ,
                      values=df['rec_acct'] ) ,
                dict( label='non_appt_ci' ,
                      values=df['non_appt_ci'] ) ,
                dict( label='appt_ci' ,
                      values=df['appt_ci'] ) ,
                dict( label='call_prep' ,
                      values=df['call_prep'] ) ,
                dict( label='tenure' ,
                      values=df['tenure'] ) ,
                dict( label='esc_ticket_cnt' ,
                      values=df['esc_ticket_cnt'] )] ,
    text=df['type_label'] ,
    marker=dict( color=index_vals ,
                 showscale=True ,  # colors encode categorical variables
                 line_color='white' , line_width=0.5 )
    ) )

fig.update_layout(
    title='Splom of the data' ,
    dragmode='select' ,
    width=740 ,
    height=720 ,
    hovermode='closest' ,
    )

splot_fig = fig

graph_03 = dcc.Graph( figure=splot_fig , id="splot_fig" ,
                      style={'gridArea': "graph_03"} )

# set style as a dictionary
title1C = html.H3( 'Relationships between variables' ,
                   style={
                       'backgroundColor': 'tan' ,
                       'fontFamily': 'verdana' ,
                       'textAlign': 'center' ,
                       'gridArea': "title1C"} ,
                   id='title1C' ,
                   className="title1C"
                   )

text_1 = html.Textarea( "Matrix:\nShow relationships between all variable" ,
                        style={
                            'backgroundColor': 'tan' ,
                            'fontFamily': 'verdana' ,
                            'textAlign': 'center' ,
                            'gridArea': "text_1" ,
                            } ,
                        id='text_1' ,
                        className="text_1" , maxLength=400 , minLength=100 )

# datediff_figure = dcc.Graph(figure=fig_daydiff, id="datediff-graph",style={'gridArea': "datediff_graph"})
# set style as a dictionary
DistriGraph_div = html.Div(
    html.Div( className="trend2" ,
              children=[

                  html.H5(
                      'Matrix Relationship Interpretation: The basis of the predictor is tenure.  Non-appt, appt, and call_prep are the most impactful as it relates to tenure. However the relationships among these feature variables are not linear.' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5_DistriGraph"

                          } ,
                      id='DistriGraphText' ,
                      className="distrText"
                      ) ,

                  ] ,
              )
    )

#########  End of Matrix Section  ##########################

###   START of :Normalize Data Using Bins ########### #########################3


### Create bin graphs ###################


bin_figures = []

import seaborn as sns
import matplotlib.pyplot as plt

# histofig , ax = plt.subplots()
# sns.histplot( data=my_data , x='tenure' , kde=True )
# ax.set_title( 'Histogram and KDE of tenure' )

histofig = px.histogram( my_data , x="tenure" )

bin_figures.append( histofig )

# from PIL import Image
histo_item_img = Image.open( "assets/tenure_distr_dist_plot.png" )
histo_item = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                        html.H5(
                            ' Tenure has several outliers but because my dataset is only 266 records, I did not remove any of the outliers.\n Created 6 bins usign ranges Created bins using ranges:# create bins bins1 = [387,494,541,583,881,1038]. In the future, I would like to obtain more data so I can remove outliers resulting in more equal distribution.' ,
                            style={
                                'backgroundColor': 'white' ,
                                'fontFamily': 'verdana' ,
                                # 'textAlign':'center',
                                'gridArea': "H5B_title_01"

                                }
                            ) ,
                        html.Img( src=histo_item_img , width=512 , height=400 ) ,  # using the pillow image variable

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="histo_item_fig"
    )
histo_item.style = {'gridArea': "histo_item"}

histo_text = html.Textarea( "import seaborn as sns\n\n import matplotlib.pyplot as plt \n "
                            "histofig, ax = plt.subplots() \n sns.histplot(data=my_data, x='tenure', "
                            "kde=True) \n ax.set_title('Histogram and KDE of tenure') \n histofig.show " ,
                            style={'width': '100%' ,
                                   'height': 100 ,
                                   'color': 'white' ,
                                   'backgroundColor': 'black' ,
                                   'fontFamily': 'verdana' ,
                                   'textAlign': 'center'
                                   } , id='histo_text' ,
                            className="histo" , maxLength=400 , minLength=100 )

histo_text.style = {'gridArea': "histo_text" , 'width': '45%' , 'height': 150}

histo_item.style = {'gridArea': "histo_item"}

cleaned_data_desc = html.Div(
    html.Div( className="trend_1" ,
              children=[

                  html.H5(
                      'EDA Steps performed: identified file length and record length,view file types, '
                      'identified null values, '
                      'identified relevant columns for further analysis, '
                      'identify columns that need data type conversions, '
                      'identify columns that need to be renamed, '
                      'potential issues that may affect models performance, '
                      'and identified possible features and target column data, merged files, and dropped duplicates.  '
                      , style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5_title"

                          }
                      ) ,

                  ]
              )
    )
cleaned_data_top5desc = html.Div(
    html.Div( className="trend_2" ,
              children=[

                  html.H5(
                      'Extracted the following best-performing features into a separate dataset based on heatmap results. Will use '
                      'tenure as the basis of my target variable.  The following shows the top 5 records from my dataset.   ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "top5_title"

                          }
                      ) ,

                  ]
              )
    )
#######   END of :Normalize Data Using Bins ###########
# checking for outliers
import plotly.express as px

boxfig = px.box( my_data , y="tenure" )
boxfig.update_layout(
    title='Box Plot:the distribution of tenure given as y argument is represented' ,
    dragmode='select' ,

    hovermode='closest' ,
    )
bin_figures.append( boxfig )

import plotly.express as px

tenure_bin_fig = px.histogram( my_data , x="tenure" )
tenure_bin_fig.update_layout(
    title='Tenure Distribution: Large Variance' ,
    dragmode='select' ,

    hovermode='closest' ,
    )
tenure_bin_fig.update_layout(

    dragmode='select' ,
    width=440 ,
    height=420 ,
    hovermode='closest' ,
    )

bin_figures.append( tenure_bin_fig )

#################
import numpy as np

# create bins
bins1 = [387 , 494 , 541 , 583 , 881 , 1038]
counts , bins2 = np.histogram( my_data.tenure , bins=bins1 )
bins2 = 0.5 * (bins1[:-1] + bins2[1:])

# specify sensible widths
widths = []
for i , b1 in enumerate( bins1[1:] ):
    widths.append( b1 - bins2[i] )
# plotly figure
new_bin_fig = go.Figure( go.Bar(
    x=bins2 ,
    y=counts ,
    width=widths  # customize width here
    ) )

new_bin_fig.update_layout(
    title='Tenure Distribution: normalized data using bins' ,
    dragmode='select' ,

    hovermode='closest' ,
    )
bin_figures.append( new_bin_fig )

### create bin graph components

graph_04 = dcc.Graph( figure=bin_figures[0] , id="graph_04" ,
                      style={'gridArea': "graph_04" , 'width': 240 , 'height': 420 , } )
graph_05 = dcc.Graph( figure=bin_figures[1] , id="graph_05" ,
                      style={'gridArea': "graph_05" , 'width': 440 , 'height': 420 , } )

# graph_06 = dcc.Graph(figure=bin_figures[2],
#                    style={'gridArea': "graph_06"})

graph_07 = dcc.Graph( figure=bin_figures[3] , id="graph_07" ,
                      style={'gridArea': "graph_07"} )

# set style as a dictionary
title2B = html.H3( 'Data Distribution' ,
                   style={
                       'backgroundColor': 'tan' ,
                       'fontFamily': 'verdana' ,
                       'textAlign': 'center' ,

                       } ,
                   id='title2B' ,
                   className="title2B"
                   )

# text1
text_1.style = {'gridArea': "text_1"}
text_2 = html.H4(
    "Distribution:  Tenure is my prediction variable however I would like this to be a classification problem.  "
    "  My goal is to group this data into 5 group and assign a label to each group. Given tenure data is not "
    "normalized.  Will need to equally distribute the data using bins.  I will create 5 bins based on percentile values  min, 50%,75%, and max values "
    "Bins values = [387,494,541,583,881,1038]" ,
    style={
        'backgroundColor': 'tan' ,
        'fontFamily': 'verdana' ,
        'textAlign': 'center' ,

        } ,
    id='text_2' )

# text1
text_2.style = {'gridArea': "text_2"}

# graph_03 = dcc.Graph(figure=splot_fig,
#                    style={'gridArea': "graph_03"})
##### END OF BIN SECTION #####################

####  AVERAGE Summary Section
average_type_data = pd.read_csv( "summary.csv" )
avg_columns = [{"name": "types" , "id": "types" , "type": "numeric" , "format": {'specifier': ','}} ,
               {"name": "type_label" , "id": "type_label" , "type": "text"} ,
               ]

# iterate the remaining columns and append the information about each column
for name in average_type_data.columns[3:]:
    col_info = {
        "name": name ,
        "id": name ,
        "type": "numeric" ,
        "format": {'specifier': ','}}

    avg_columns.append( col_info )
avg_columns

avg_data = average_type_data.sort_values( "types" , ascending=True ).to_dict( "records" )

from dash import dash_table

avg_table = dash_table.DataTable(
    id='avg-table' ,
    columns=avg_columns ,
    data=avg_data ,

    fixed_rows={"headers": True} ,
    active_cell={"row": 0 , "column": 0} ,
    sort_action="native" ,
    derived_virtual_data=avg_data ,
    style_table={
        "minHeight": "40vh" ,
        "height": "40vh" ,
        "overflowY": "scroll"
        } ,
    style_cell={
        "whitespace": "normal" ,
        "height": "auto" ,
        "fontFamily": 14

        } ,
    style_filter={'height': '50px'} ,
    style_header={
        "textAlign": "center" ,
        "fontSize": 14
        } ,
    style_data={
        "fontSize": 12
        } ,
    style_data_conditional=[
        {
            "if": {"column_id": "type_label"} ,
            "width": "60px" ,
            "textAlign": "left" ,
            "textDecoration": "underline" ,
            "cursor": "pointer"
            } ,
        {  # every other row change back ground color
            "if": {"row_index": "odd"} ,
            "backgroundColor": "#fafbfb"
            }
        ] ,
    )


def create_tab_avg():
    return dbc.Tab(
        avg_table ,
        label="Average" ,
        # value="top5",
        className="single-tab" ,
        id="avg-tab" ,
        # selected_className="single-tab--selected",
        style={'gridArea': "avg_table"}
        )


Average_tab = create_tab_avg()

Avg_tab = dcc.Tabs(
    [Average_tab] ,
    className="tabs-container" ,
    id="Avg-tabs" ,
    value="average" ,
    style={'gridArea': "avg_table"}

    )

import pandas as pd


def create_feature_plot_by_type(type):
    if type == 0:  # HighMaintenance  [Change loyist to high maint]
        feature = "rec_acct"
        g_title = 'HighMaintenance - Highest number of <br>reconciled account <br>Type vs rec_acct'

    elif type == 1:  # Dissatisfied
        feature = "esc_ticket_cnt"
        g_title = 'Dissatisfied - Highest number of escalation<br> tickets reported   <br>Type vs esc_ticket_cnt     '

    elif type == 2:  # Potential Loyalist
        feature = "appt_ci"
        g_title = 'Potential Loyalist - Highest number of document<br> management accounts (doc_mgmt)<br> Type vs doc_mgmt'
    elif type == 3:  # Loyalist
        feature = "non_appt_ci"
        g_title = 'Loyalist - 2nd Highest Non call <br> prep appts (non_appt_ci)<br> Type vs Non_appt_ci'

    elif type == 4:  # Satified
        feature = "doc_mgmnt"
        g_title = 'Satisfied - Does not rank High in <br>any feature evaluation<br> Type vs doc_mgmnt'

    temp_df = my_data.loc[: , [feature , 'types' , 'type_label']]
    temp_df = temp_df.reset_index( drop=True )
    pd.options.plotting.backend = "plotly"  # just once at the beginning

    temp_fig = my_data.plot.line( x=feature , y="types" , color="type_label" ,
                                  line_group="type_label" )
    temp_fig.update_layout( height=400 , width=600 , title=g_title , title_x=0.4 )

    return temp_fig


def create_feature_plot(feature):
    temp_df = my_data.loc[: , [f'{feature}' , 'types' , 'type_label']]

    pd.options.plotting.backend = "plotly"  # just once at the beginning

    temp_fig = non_appt_ci_df.plot.line( x=f'{feature}' , y="types" , color="type_label" ,
                                         line_group="type_label" )

    return temp_fig


def create_feature_plot(feature):
    temp_df = my_data.loc[: , [f'{feature}' , 'types' , 'type_label']]

    pd.options.plotting.backend = "plotly"  # just once at the beginning

    temp_fig = non_appt_ci_df.plot.line( x=f'{feature}' , y="types" , color="type_label" ,
                                         line_group="type_label" )

    return temp_fig


def new_create_subplots(df , type):
    value = type

    fig = create_feature_plot_by_type( type )

    return fig


### create tabs
def create_tab(content , label , value):
    return dcc.Tab(
        content ,
        label=label ,
        value=value ,
        id=f"{value}-tab" ,
        className="single-tab" ,
        selected_className="single-tab--selected" ,
        )


type_feature_analysis_figures = []
type_feature_analysis_figures.append( new_create_subplots( my_data , 0 ) )
type_feature_analysis_figures.append( new_create_subplots( my_data , 1 ) )
type_feature_analysis_figures.append( new_create_subplots( my_data , 2 ) )
type_feature_analysis_figures.append( new_create_subplots( my_data , 3 ) )
type_feature_analysis_figures.append( new_create_subplots( my_data , 4 ) )

# Create dash graphs
loyalist_graph = dcc.Graph( figure=type_feature_analysis_figures[3] , id="loyalist-graph" )
highmaint_graph = dcc.Graph( figure=type_feature_analysis_figures[0] , id="highmaint-graph" )
potloy_graph = dcc.Graph( figure=type_feature_analysis_figures[2] , id="potloy-graph" )
satisfied_graph = dcc.Graph( figure=type_feature_analysis_figures[4] , id="satisfied-graph" )
diss_graph = dcc.Graph( figure=type_feature_analysis_figures[1] , id="diss-graph" )

# Add graphs to tabs
analizeloyalist_tab = create_tab( loyalist_graph , "Loyalist" , "analyzeloyalist" )
analizehighmaint_tab = create_tab( highmaint_graph , "High Maint" , "analyzehighmaint" )
analizepotloy_tab = create_tab( potloy_graph , "Potential" , "analyzepotloy" )
analizesatisfied_tab = create_tab( satisfied_graph , "Satisfied" , "analyzesatis" )
analizediss_tab = create_tab( diss_graph , "Dissatisfied" , "analyzeddiss" )

analysis_tabs = dcc.Tabs(
    [analizeloyalist_tab , analizehighmaint_tab , analizepotloy_tab , analizesatisfied_tab , analizediss_tab] ,
    className="tabs-container" ,
    id="analyzefeatures" ,
    value="analyzeloyalist" ,
    style={'gridArea': "analyzefeatures"} )

analysis_graph = new_create_subplots( my_data , 2 )
test_graph_figure = dcc.Graph( figure=analysis_graph , id="test_graph_figure" ,
                               style={'gridArea': "test_graph_figure"} )

analysis_graph_figure = dcc.Graph( figure=analysis_graph , id="analysis_graph_figure" ,
                                   style={'gridArea': "analysis_graph_figure"} )
###################

# set style as a dictionary
title5A = html.Div(
    html.Div( className="trend_4" ,
              children=[

                  html.H3( 'Average Bin Groups, Add New Category Labels' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,

                               } ,
                           id='title5A' ,
                           className="title5A"
                           ) ,

                  html.H5(
                      'After grouping tenure data into 5 groups using bins, I used the average of each feature to further analyze feature performance.  Base on analysis, I feature engineered new labels. You can click the link on each record to view further analysis of feature performance for each group' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "title5_2ndtitle"

                          }
                      )
                  ] ,
              )
    )


### END OF AVERAGE SUMMARY SECTION

## Start Prediction Section

def create_my_prediction_tables(temp_df , group):
    used_columns = temp_df.columns.values

    df = temp_df.loc[: , used_columns]
    columns = [{"name": "index" ,
                # columns - List of dictionaries where each item represents information (name, id, type, format, etc...) on one column
                "id": "index" ,
                "type": "numeric"} ,
               {"name": "type_label" ,
                # columns - List of dictionaries where each item represents information (name, id, type, format, etc...) on one column
                "id": "type_label" ,
                "type": "text"} ,
               {"name": "types" ,
                # columns - List of dictionaries where each item represents information (name, id, type, format, etc...) on one column
                "id": "types" ,
                "type": "numeric"} ,
               {"name": "y_pred" ,
                # columns - List of dictionaries where each item represents information (name, id, type, format, etc...) on one column
                "id": "y_pred" ,
                "type": "numeric"}
               ]

    # print( columns )  # view columns.  Make sure all the column definitions have appended
    data = temp_df.sort_values( "types" , ascending=True ).to_dict( "records" )

    return dash_table.DataTable(
        id=f"{group}" ,
        columns=columns ,
        data=data ,
        fixed_rows={"headers": True} ,
        active_cell={"row": 0 , "column": 0} ,
        sort_action="native" ,
        derived_virtual_data=data ,
        style_table={
            "minHeight": "80vh" ,
            "height": "80vh" ,
            "overflowY": "scroll"
            } ,
        style_cell={'textAlign': 'left'} ,
        style_filter={'height': '50px'} ,
        # fill_width=False,   had an issue with viewing  all columns
        style_header={
            "textAlign": "center" ,
            "fontSize": 14
            } ,
        style_data={
            "fontSize": 12
            } ,
        style_data_conditional=[
            {
                "if": {"column_id": "types"} ,
                "width": "80px" ,
                "textAlign": "left" ,
                "textDecoration": "underline" ,
                "cursor": "pointer"
                } ,
            {  # every other row change back ground color
                "if": {"row_index": "odd"} ,
                "backgroundColor": "#fafbfb"
                }
            ] ,
        )


predictions = my_data.loc[: , ['type_label' , 'types' , 'y_pred']].reset_index()

predictions.loc[: , ['type_label' , 'types']].value_counts()

Pred_dissatisfied_df = predictions.query( 'types == 1' )
Pred_Loyalist_df = predictions.query( 'types == 3' )
Pred_High_Maintenance_df = predictions.query( 'types == 0' )
Pred_Potential_Loyalist_df = predictions.query( 'types == 2' )
Pred_Satisfied_df = predictions.query( 'types == 4' )

# id = dissatisfied-Table
Pred_dissatisfied_table = create_my_prediction_tables( Pred_dissatisfied_df , "preddissatisfied" )

# id =  Loyalist-Table
Pred_Loyalist_table = create_my_prediction_tables( Pred_Loyalist_df , "predLoyalist" )

# id = High_Maintenance-Table
Pred_High_Maintenance_table = create_my_prediction_tables( Pred_High_Maintenance_df , "predHigh_Maintenance" )

# id = Potential_Loyalist-Table
Pred_Potential_Loyalist_table = create_my_prediction_tables( Pred_Potential_Loyalist_df , "predPotential_Loyalist" )

# id = Satisfied-Table
Pred_Satisfied_table = create_my_prediction_tables( Pred_Satisfied_df , "predSatisfied" , )

Pred_Satisfied_tab = create_tab( Pred_Satisfied_table , "Satisfied" , "predsatisfied" )
Pred_High_Maintenance_tab = create_tab( Pred_High_Maintenance_table , "High_Maint" , "predhigh_maint" )
Pred_dissatisfied_tab = create_tab( Pred_dissatisfied_table , "Dissatisfied" , "preddissatisfied" )
Pred_Loyalist_tab = create_tab( Pred_Loyalist_table , "Loyalist" , "predloyalist" )
Pred_Potential_Loyalist_tab = create_tab( Pred_Potential_Loyalist_table , "Potential_Loyalist" , "predpot_loyalist" )

Pred_table_tabs = dcc.Tabs(
    [Pred_Satisfied_tab , Pred_High_Maintenance_tab , Pred_dissatisfied_tab , Pred_Loyalist_tab ,
     Pred_Potential_Loyalist_tab] ,
    className="tabs-container" ,
    id="pred-table-tabs" ,
    value="predpot_loyalist" ,
    style={'gridArea': "pred_table_tabs"}

    )
## End of Prediction Section
### start of distribution section
my_data_normalize = pd.DataFrame( my_data.type_label.value_counts( normalize=True ) )
my_data_normalize = my_data_normalize.reset_index()

circle_fig = px.pie( my_data_normalize , values='type_label' , names='index' )
circle_fig.update_traces( textposition='inside' )
circle_fig.update_layout( uniformtext_minsize=12 , uniformtext_mode='hide' )

# set style as a dictionary
title5B = html.Div(
    html.Div( className="trend_6" ,
              children=[

                  html.H3( 'Category Type Distribution' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,

                               } ,
                           id='title5B' ,
                           className="title5B"
                           ) ,

                  html.H5(
                      'In viewing the distribution of my data, I see the number of "Satisified" customers are under represented.  This is going to affect my predictive power for this particular group. In the future, I would like to gather more records for this class to bring balance to all the classes' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "title5_2ndtitle"

                          }
                      )
                  ] ,
              )
    )

graph_01 = dcc.Graph( figure=circle_fig ,
                      style={'gridArea': "graph_01"} )


## end of distribution section


### pRediction section  ####
def return_type_prediction_subplots(df , type):
    value = type
    df = my_data.query( 'types==@value' )

    new_df = df.loc[: , ['types' , 'y_pred' , 'type_label']]
    new_df = new_df.reset_index( drop=True )

    type_label_value = ""
    type_label_value = new_df.iloc[0]['type_label']

    x_actual = new_df.index
    y_actual = new_df.types

    x_pred = new_df.index
    y_pred = new_df.y_pred

    fig = go.Figure()
    fig.add_bar( x=x_actual , y=y_actual , name='actual' )
    fig.add_bar( x=x_pred , y=y_pred , name='prediction' )
    fig.update_layout( height=400 , width=800 , title=f'{type_label_value} actual vs pred' )

    return fig


pred_figures = []
pred_figures.append( return_type_prediction_subplots( Pred_Satisfied_df , 4 ) )
pred_figures.append( return_type_prediction_subplots( Pred_High_Maintenance_df , 0 ) )
pred_figures.append( return_type_prediction_subplots( Pred_dissatisfied_df , 1 ) )
pred_figures.append( return_type_prediction_subplots( Pred_Loyalist_df , 3 ) )
pred_figures.append( return_type_prediction_subplots( Pred_Potential_Loyalist_df , 2 ) )

# Create dash graphs
loyalist_graph2 = dcc.Graph( figure=pred_figures[3] , id="loyalist-graph2" )
highmaint_graph2 = dcc.Graph( figure=pred_figures[1] , id="highmaint-graph2" )
potloy_graph2 = dcc.Graph( figure=pred_figures[4] , id="potloy-graph2" )
satisfied_graph2 = dcc.Graph( figure=pred_figures[0] , id="satisfied-graph2" )
diss_graph2 = dcc.Graph( figure=pred_figures[2] , id="diss-graph2" )
##############
# pred_graph = dcc.Graph( figure=pred_figures[4] , id="pred_graph", style={'gridArea': "pred_graph"})
pred_graph = dcc.Graph( figure=pred_figures[4] , id="pred-graph" ,
                        style={'gridArea': "pred_graph"} )

###################################
# pred_graph_item = html.Div( dcc.Graph( figure=pred_figures[4], id="pred_graph" ))
# pred_graph_item.style={'gridArea': "pred_graph"}
######################
# Add graphs to tabs
analizeloyalist_tab2 = create_tab( loyalist_graph2 , "Loyalist" , "analyzeloyalist2" )
analizehighmaint_tab2 = create_tab( highmaint_graph2 , "High Maint" , "analyzehighmaint2" )
analizepotloy_tab2 = create_tab( potloy_graph2 , "Potential" , "analyzepotloy2" )
analizesatisfied_tab2 = create_tab( satisfied_graph2 , "Satisfied" , "analyzesatis2" )
analizediss_tab2 = create_tab( diss_graph2 , "Dissatisfied" , "analyzeddiss2" )

analysis_tabs2 = dcc.Tabs(
    [analizeloyalist_tab2 , analizehighmaint_tab2 , analizepotloy_tab2 , analizesatisfied_tab2 , analizediss_tab2] ,
    className="tabs-container" ,
    id="analyzefeatures2" ,
    value="analyzepotloy2" ,
    style={'gridArea': "analyzefeatures2"} )

##################################
LogisticRegression_img = Image.open( "assets/LogisticRegression.PNG" )
LogisticRegressionConfusionMatrix_img = Image.open( "assets/LogisticRegressionConfusionMatrix.PNG" )
ImprovedScoreUsingRandomForestClassifer_img = Image.open( "assets/ImprovedScoreUsingRandomForestClassifer.PNG" )
RandomForestPCA_img = Image.open( "assets/RandomForestPCA2.png" )
FindPCA_img = Image.open( "assets/RandomForestPCA1.png" )
Overfit_img = Image.open( "assets/Overfitting.png" )

########################################################
LogisticRegression_img.style = {'gridArea': "LogisticRegression_fig"}
LogisticRegressionConfusionMatrix_img.style = {'gridArea': "LogisticRegressionConfusionMatrix_fig"}
ImprovedScoreUsingRandomForestClassifer_img.style = {'gridArea': "ImprovedScoreUsingRandomForestClassifer_fig"}
RandomForestPCA_img.style = {'gridArea': "RandomForestPCA_fig"}
Overfit_img.style = {'gridArea': "Overfit_fig"}
##########################################################


title9 = html.Div(
    html.Div( className="trend_9" ,
              children=[

                  html.H3( ' Model Performance' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,

                               } ,
                           id='title9' ,
                           className="title9"
                           ) ,
                  html.H5(
                      'Prediction accuracy using Logistic Regression Model ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5B_title_01"

                          }
                      ) ,
                  html.Img( src=LogisticRegression_img , width=812 , height=900 ) ,
                  html.H5(
                      'Tested for Overfitting.  Found model is not overfit so there is no need to tune the model. ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "Overfit_title_01"

                          }
                      ) ,
                  html.Img( src=Overfit_img , width=720 , height=850 )

                  ,
                  html.H5(
                      'Evaluate the performance using .score() method. ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5B_title"

                          }
                      ) ,
                  html.Img( src=LogisticRegressionConfusionMatrix_img , width=512 , height=400 )
                  ,

                  html.H5(
                      'Improved Logistic Regression score using RandomForestClassifer ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5B_title"

                          }
                      ) ,
                  html.Img( src=ImprovedScoreUsingRandomForestClassifer_img , width=512 , height=400 ) ,
                  html.H3( ' Introducing PCA to improve score and identify feature importance' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,

                               } ,
                           id='PCA9' ,
                           className="PCA9"
                           ) ,
                  html.H5(
                      'Test for Best PCA value ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "PCAvalue_title"

                          }
                      ) ,
                  html.Img( src=FindPCA_img , width=742 , height=900 ) ,
                  html.H5(
                      'Improved RandomForestClassifer score using PCA(n_components=2) ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "FindPCA_title"

                          }
                      ) ,
                  html.Img(src=RandomForestPCA_img , width=512 , height=500 ) ,

                  html.H5(
                      'Conclusion I was able to run my Random Forest model using PCA and reduce features down to 2 principle '
                      ' components resulting in a accuracy score of 96%. Before, the accuracy '
                      ' results were 0.9285714285714286 so the results are the same. As a result, PCA did improve my performance. '
                       ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "H5B_title"

                          }
                      )
                  ] ,
              )
    )
######################################
title_pred = html.Div(
    html.Div( className="trend_11" ,
              children=[

                  html.H3( 'Predictions & Multiclass classification ' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,

                               } ,
                           id='title_pred' ,
                           className="title_pred"
                           ) ,

                  html.H5(
                      'Made predictions using RandomForestClassifier model. Appended scores to dataframe.  Click each tab to view prediction results ' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "title_pred2"

                          }
                      )
                  ] ,
              )
    )

######################################
# Graph my prediction and graph my actual value
from plotly.colors import qualitative

COLORS = qualitative.T10
COLORS

All_pred_fig_01 = go.Figure()
All_pred_fig_01.add_scatter( x=my_data.index ,
                             y=my_data['types'] ,
                             mode="lines+markers" ,
                             line={'color': COLORS[0]} ,
                             name='actual' )
All_pred_fig_01.add_scatter( x=my_data.index ,
                             y=my_data['y_pred'] ,
                             mode="lines+markers" ,
                             line={'color': COLORS[1]} ,
                             name='prediction' )
All_pred_fig_01.update_layout( height=400 , width=800 , title={
    "text": "All Types: Trace Actual vs Predition" ,
    }
                               )

All_pred_fig_dv = dcc.Graph( figure=All_pred_fig_01 ,
                             style={'gridArea': "All_pred_fig_dv"} )

## end of prediction sections
## COnfustion matrix section

# from PIL import Image

ConfusionMatrix_item = html.Div( html.Img( src=r'assets/ConfusionMatrix.png' , alt='image' ) ,
                                 id="ConfusionMatrix_item" )

ConfusionMatrix_item.style = {'grid Area': "ConfusionMatrix_item"}

ConfusionMatrix_text = html.Textarea( "\
#split data to Train and test\n\n \
from  sklearn.model_selection \nimport train_test_split \n \
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=0)\n\n \
\
#Use Support Vector Classifier as a classifier\n \
from sklearn.svm import SVC\n \
from sklearn.metrics import confusion_matrix\n\n \
#training the classifier using X_Train and y_train\n \
clf = SVC(kernel = 'linear').fit(X_train, y_train)\n \
clf.predict(X_train)\n\n \
#Creating a confusion matrix which compares the y_test and y_pred \n \
cm = confusion_matrix(y_test, y_pred)\n\n \
plt.figure(figsize=(6,5))\n \
sns.heatmap(cm_df,annot=True)\n \
plt.title('Confusion Matrix')\n \
plt.ylabel('Actual values')\n \
plt.xlabel('Predicted values')\n \
plt.savefig('assets\ConfusionMatrix.png')\n \
plt.show()" ,
                                      style={'width': '100%' ,
                                             'height': 300 ,
                                             'color': 'white' ,
                                             'backgroundColor': 'black' ,
                                             'fontFamily': 'verdana' ,
                                             'textAlign': 'center'
                                             } , id='ConfusionMatrix_text' ,
                                      className="ConfusionMatrix_text" , maxLength=400 , minLength=100 )

ConfusionMatrix_text.style = {'gridArea': "ConfusionMatrix_text" , 'width': '45%' , 'height': 300}

# set style as a dictionary
Cm_title = html.H2( 'Confusion Matrix for 5 class classification' ,
                    style={
                        'backgroundColor': 'tan' ,
                        'fontFamily': 'verdana' ,
                        'textAlign': 'center' ,

                        } ,
                    id='Cm_title' ,
                    className="Cm_title"
                    )

Cm_title.style = {'gridArea': "Cm_title"}

# set style as a dictionary
Cm_subtitle = html.H3( "The dataset has 5 customer types as outputs or classes: 'Loyalist', \
'Dissatisfied', 'High_Maintenance', 'Satisfied', 'Potential_Loyalist'" ,
                       style={
                           'backgroundColor': 'tan' ,
                           'fontFamily': 'verdana' ,
                           'textAlign': 'center' ,

                           } ,
                       id='Cm_subtitle' ,
                       className="Cm_subtitle"
                       )

Cm_subtitle.style = {'gridArea': "Cm_subtitle"}

#########################################################


text15 = html.H3( "ROC Evaluation:  The main interest is not the plot but the ROC-AUC score itself"
                  , style={
        'backgroundColor': 'tan' ,
        'fontFamily': 'verdana' ,
        'textAlign': 'center' ,

        } ,
                  id='text15' )
# className="text15" , maxLength=400 , minLength=100 )

text15.style = {'gridArea': "text15"}
#############################
title_ROC = html.Div(
    html.Div( className="trend_10" ,
              children=[

                  html.H3( 'Evaluation with ROC Curves and ROC AUC' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,

                               } ,
                           id='title_ROC' ,
                           className="title_ROC"
                           ) ,

                  html.H5(
                      'The ROC AUC evaluates binary classification models measures how well my model is classifying each class. Based on the results below, my accuracy is between 60-62% accuracy.  In a multi-class classification setup with highly imbalanced classes, micro-averaging is preferable over macro-averaging.' ,
                      style={
                          'backgroundColor': 'white' ,
                          'fontFamily': 'verdana' ,
                          # 'textAlign':'center',
                          'gridArea': "title_ROC2"

                          }
                      ) ,
                  html.Br() ,
                  html.A( 'Resource Link: Multiclass Receiver Operating Characteristic (ROC)' ,
                          href="https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html" ,
                          style={'gridArea': "link_ROC"} ) , html.Br() ,

                  ] ,
              )
    )
#


from PIL import Image

pil_img = Image.open( "assets/Roc_curve_Loyalist_fig.png" )
pil_hmimg = Image.open( 'assets/High_Maintenance_fig.png' )
pil_limg = Image.open( 'assets/Potential_Loyalist_fig.png' )
pil_dimg = Image.open( 'assets/Dissatisfied_fig.png' )
pil_simg = Image.open( 'assets/Satisfied_fig.png' )
pil_allimg = Image.open( 'assets/ROC_All_fig.png' )

pil_allimg = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                        html.H3( 'The Overall micro-average accuracy score is  .70 for all classes' ) ,
                        html.Img( src=pil_allimg , width=512 , height=400 ) ,  # using the pillow image variable

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="All_img_fig"
    )

pil_simg = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                        html.H3( 'The Satissifed class has a micro-average accuracy score of .42.  '
                                 'This is an imbalanced class and the accuracy score is .28 less than '
                                 'the over all average' ) ,

                        html.Img( src=pil_simg , width=512 , height=400 ) ,  # using the pillow image variable

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="Satisfied_fig"
    )

pil_dimg = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                        html.H3( 'The Dissatissifed class has a micro-average accuracy score of .62.  '
                                 'This is an imbalanced class and the accuracy score is .08 less than the '
                                 'over all average' ) ,
                        html.Img( src=pil_dimg , width=512 , height=400 ) ,  # using the pillow image variable

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="Dissatisfied_fig"
    )

pil_limg = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                        html.H3( 'The Potential Loyalist class has a micro-average accuracy score of .66.  '
                                 'That is .04 less than the Overall average' ) ,

                        html.Img( src=pil_limg , width=512 , height=400 ) ,  # using the pillow image variable

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="Roc_curve_all_img"
    )

pil_hmimg = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                        html.H3( 'The High Maintenance class has a micro-average accuracy score of .66. '
                                 ' That is .04 less than the Overall average' ) ,
                        html.Img( src=pil_hmimg , width=512 , height=400 ) ,  # using the pillow image variable

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="High_Maintenance_fig"
    )

pil_img = html.Div(
    [
        html.Div(
            html.Div(
                [
                    html.Div( [
                        html.H3( 'The Loyalist class has a micro-average accuracy score of .66.  '
                                 'That is .04 less than the Overall average' ) ,
                        html.Img( src=pil_img , width=512 , height=400 ) ,  # using the pillow image variable

                        ] ) ,
                    html.Div( className="sidebar-wrapper" ) ,
                    ]
                ) ,
            className="sidebar" ,
            ) ,
        html.Div(
            html.Div(
                html.Div( className="container-fluid" ) ,
                className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " ,
                ) ,
            className="main-panel" ,
            ) ,
        ] , id="Roc_curve_Loyalist_fig"
    )

text15 = html.Textarea( "ROC Evaluation"
                        , style={
        'backgroundColor': 'tan' ,
        'fontFamily': 'verdana' ,
        'textAlign': 'center' ,

        } ,
                        id='text15' ,
                        className="text15" , maxLength=400 , minLength=100 )

text15.style = {'gridArea': "text15"}

# add images to a containerF
pil_img.style = {'gridArea': "Roc_curve_Loyalist_fig"}
pil_hmimg.style = {'gridArea': "High_Maintenance_fig"}
pil_limg.style = {'gridArea': "Potential_Loyalist_fig"}
pil_dimg.style = {'gridArea': "Dissatisfied_fig"}
pil_simg.style = {'gridArea': "Satisfied_fig"}
pil_allimg.style = {'gridArea': "ROC2_All_fig"}

######################################


# Add images  to tabs

# roc_tab_loyal_ROC
roc_tab_loyal = create_tab( pil_img , "Loyalist" , "loy_roc" )
roc_tab_highmaint = create_tab( pil_hmimg , "High Maint" , "hm_roc" )
roc_tab_potloy = create_tab( pil_limg , "Potential Loyalist" , "pl_roc" )
roc_tab_satis = create_tab( pil_simg , "Satisfied" , "sat_roc" )
roc_tab_diss = create_tab( pil_dimg , "Dissatisfied" , "dis_roc" )
roc_tab_all = create_tab( pil_allimg , "All" , "all_roc" )

roc_tabs = dcc.Tabs(
    [roc_tab_loyal , roc_tab_highmaint , roc_tab_potloy , roc_tab_satis , roc_tab_diss , roc_tab_all] ,
    className="tabs-container" ,
    id="roctabs" ,
    value="loy_roc" ,
    style={'gridArea': "roctabs"} )
## end of ROC section


##################################

# set style as a dictionary
conclusion_title = html.Div(
    html.Div( className="trend_18" ,
              children=[

                  html.H3( 'Conclusion' ,
                           style={
                               'backgroundColor': 'tan' ,
                               'fontFamily': 'verdana' ,
                               'textAlign': 'center' ,

                               } ,
                           id='conclusiontitle' ,
                           className="conclusiontitle"
                           ) ,

                  html.H5(
                      'In conclusion, I was able to determine there are several factors that affect customer cancellation.  The most prominent features are non-appt calls and prep time.  I was able to create customer types based on different feature however the imbalance of my classes affected my micro-average accuracy score of my multi-classification model.  In the future, I would like to gather more data under the "satisfied" classification to balance my classes and improve model accuracy'
                      ,
                      style={
                          'backgroundColor': 'tan' ,
                          'fontFamily': 'verdana' ,
                          'textAlign': 'center' ,

                          } ,
                      id='conclusiontitle2' ,
                      className="conclusiontitle2"
                      )
                  ] ,
              )
    )

# 'In conclustion, I was able to determine there are several factors that affect customer cancellation.  The most prominent features are non-appt calls and prep time.  I was able to create customer types based on different feature however the imbalance of my classes affected my micro-average accuracy score of my multi-classification model.  In the future, I would like to gather more data under the "satisfied" classifcation'
################################## create dataframe tables ################

# *********************************************************************************************************
app.layout = html.Div( [

    dbc.Row( [dbc.Col( title , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( links , width=5 )] , justify="around" ) ,
    dbc.Row( [dbc.Col(shortvideo_item, width=5)], justify="around"),
    dbc.Row( [dbc.Col(presentation_item, width=5)], justify="around"),
    dbc.Row( [dbc.Col( purch_cancel_code_item , width=5 )] , justify="around" ) ,
    ###
    #Relationships between variables
    dbc.Row( [dbc.Col( title1C , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( text_1 , width=3 ) , dbc.Col( DistriGraph_div , width=8 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( graph_03 , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( correlation_item , width=11 )] , justify="around" ) ,

    ##
    dbc.Row( [dbc.Col( Purchase_activity_desc , width=11 )] , justify="around" ) ,
    # dbc.Row( [dbc.Col(purchase_fig,width=5),dbc.Col(cancel_fig,width=6)], justify="around"),
    dbc.Row( [dbc.Col( title7 , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( text7 , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( cleaned_data_desc , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( top5_tab , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( cleaned_data_top5desc , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( extract_feature_table , width=11 )] , justify="around" ) ,



    dbc.Row( [dbc.Col( title2B , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( text_2 , width=3 ) , dbc.Col( histo_text , width=8 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( histo_item , width=11 )] , justify="around" ) ,
    dbc.Row( [ dbc.Col( graph_07 , width=6 ) ] , justify="around" ) ,#dbc.Col( graph_05 , width=5 ),
    dbc.Row( [dbc.Col( title5A , width=11 )] , justify="around" ) ,
    # dbc.Row( [dbc.Col(ConfusionMatrix_item,width=11)],justify="around"),
    dbc.Row( [dbc.Col( avg_table , width=5 ) , dbc.Col( analysis_graph_figure , width=5 )] , justify="around" ) ,
    # dbc.Row( [dbc.Col(avg_table,width=5), dbc.Col(analysis_tabs,width=5)], justify="around" ),

    dbc.Row( [dbc.Col( title5B , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( graph_01 , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( title9 , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( title_pred , width=11 )] , justify="around" ) ,

    dbc.Row( [dbc.Col( pred_graph , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( Pred_table_tabs , width=11 )] , justify="around" ) ,
    #dbc.Row( [dbc.Col( analysis_tabs2 , width=11 )] , justify="around" ) ,  #

    dbc.Row( [dbc.Col( All_pred_fig_dv , width=11 )] , justify="around" ) ,

    dbc.Row( [dbc.Col( title_ROC , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( text15 , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( roc_tabs , width=11 )] , justify="around" ) ,
    dbc.Row( [dbc.Col( conclusion_title , width=11 )] , justify="around" ) ,

    ] )






@app.callback(
    Output( "pred-graph" , "figure" ) ,
    Input( "pred-table-tabs" , "value" )
    )
def change_pred_graph(group):
    if group == "predsatisfied":
        return return_type_prediction_subplots( Pred_Satisfied_df , 4 )
    elif group == "predhigh_maint":
        return return_type_prediction_subplots( Pred_High_Maintenance_df , 0 )
    elif group == "preddissatisfied":
        return return_type_prediction_subplots( Pred_dissatisfied_df , 1 )
    elif group == "predloyalist":
        return return_type_prediction_subplots( Pred_Loyalist_df , 3 )
    else:
        return return_type_prediction_subplots( Pred_Potential_Loyalist_df , 2 )




@app.callback(
    Output( "analysis_graph_figure" , "figure" ) ,
    Input( 'avg-table' , 'active_cell' ) ,
    State( 'avg-table' , 'derived_virtual_data' )

    )
def change_area_graphs(avg_cell , avg_data):
    """
    Change the all three graphs in the upper right hand corner of the app

    Parameters
    ----------
    avg_cell : dict with keys `row` and `cell` mapped to integers of cell location

    avg_data : list of dicts of one country per row.
                     Has keys Country, Deaths, Cases, Deaths per Million, Cases per Million

    Returns
    -------
    List of three plotly figures, one for each of the `Output`
    """
    row_number = avg_cell["row"]
    row_data = avg_data[row_number]
    types = row_data['types']
    # print("active_cell", avg_cell,
    #       "\nrow_number", row_number,
    #       "\nrow_data", row_data,
    #       "\ntypes", types)

    # convert type to a number

    fig = new_create_subplots( my_data , types )
    return fig


if __name__ == "__main__":
    app.run_server( debug=True )

# https://youtu.be/X3OuhqS8ueM
