from helper.aws_helper import S3Connection
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import math

with open('./config.yaml', 'r') as file:
    config_file = yaml.safe_load(file)


# unpack value counts results and return
def col_count(df, col):
    keys = []
    values = []
    dt = df[col].value_counts().to_dict()
    for k in dt:
        keys.append(k)
        values.append(dt[k])
    return keys, values


# provide simple dataframes used for the simple graphs
def provide_df(df, col, key_name, value_name):
    keys, values = col_count(df, col)
    df = pd.DataFrame(data={key_name: keys, value_name: values})
    return df


# function provides basic graphs that will paint basic picture of the dataset
def multi_h_bar(df_list, title_list):
    axs_count = len(df_list)
    rows = math.ceil(axs_count / config_file["MH_PLOT_PARAMS"]['cols'])
    # OO method plot
    fig, axes = plt.subplots(nrows=rows,
                             ncols=config_file["MH_PLOT_PARAMS"]['cols'],
                             figsize=(
                                 config_file["MH_PLOT_PARAMS"]['fig_width'],
                                 config_file["MH_PLOT_PARAMS"]['fig_height']))

    axes = axes.flatten()

    for ax, df, title in zip(axes, df_list, title_list):
        # Plot data
        ax.barh(df.iloc[:, 0], df.iloc[:, 1])
        # # Customize the plot
        ax.set_title(title, fontweight=config_file['MH_PLOT_PARAMS']['font_weight'])
        ax.set(xlabel=df.keys()[1], ylabel=df.keys()[0])
        # # Add value labels to the bars
        for i, count in enumerate(df.iloc[:, 1]):
            ax.text(count, i, str(count), va=config_file['MH_PLOT_PARAMS']['vert_align'])
        # Hide any unused subplots
        for ax in axes[axs_count:]:
            ax.set_visible(False)
    plt.tight_layout()
    plt.show()


def single_v_bar(df, title):
    # OO method plot
    fig, ax = plt.subplots(
        figsize=(config_file["SV_PLOT_PARAMS"]['fig_width'], config_file["SV_PLOT_PARAMS"]['fig_height']))
    # Plot data
    ax.bar(df.iloc[:, 0], df.iloc[:, 1])
    # Customize the plot
    ax.set_title(title, fontweight=config_file['SV_PLOT_PARAMS']['font_weight'])
    ax.set(xlabel=df.keys()[1], ylabel=df.keys()[0])
    # # Add value labels to the bars
    for i, count in enumerate(df.iloc[:, 1]):
        ax.text(i, count, str(count), ha=config_file['SV_PLOT_PARAMS']['center_align'],
                va=config_file['SV_PLOT_PARAMS']['vert_align'])
    plt.tight_layout()
    plt.show()


def multi_v_bar(df_list, title_list, x_axis, y_axis):
    num_plots = len(df_list)
    rows = math.ceil(num_plots / config_file["MV_PLOT_PARAMS"]['cols'])

    fig, axes = plt.subplots(nrows=rows, ncols=config_file["MV_PLOT_PARAMS"]['cols'],
                             figsize=(config_file["MV_PLOT_PARAMS"]['fig_width'],
                                      config_file["MV_PLOT_PARAMS"]['fig_height'] * rows))
    axes = axes.flatten()  # Flatten the 2D array of axes to 1D for easy iteration

    for ax, df, title in zip(axes, df_list, title_list):
        df.plot.bar(ax=ax)
        ax.set_title(title, fontweight=config_file['MV_PLOT_PARAMS']['font_weight'])
        ax.set(xlabel=x_axis, ylabel=y_axis)

    # Hide any unused subplots
    for ax in axes[num_plots:]:
        ax.set_visible(False)

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()  # Display the plots


# get more details on a segment
def distributions(df, col1, col2, check1):
    return (df.loc[df[col1] == check1, col2]).value_counts()


# Custom function to place the values outside the pie chart
def autopct_outside(pct):
    return ('%.1f%%' % pct) if pct > 0 else ''


def multi_pie_chart(df_list, title_list):
    axs_count = len(df_list)
    rows = math.ceil(axs_count / config_file["PIE_PLOT_PARAMS"]['cols'])

    plt.close()
    # OO method plot
    fig, axes = plt.subplots(nrows=rows,
                             ncols=config_file["PIE_PLOT_PARAMS"]['cols'],
                             figsize=(
                                 config_file["PIE_PLOT_PARAMS"]['fig_width'],
                                 config_file["PIE_PLOT_PARAMS"]['fig_height']))
    axes = axes.flatten()
    print(axes)
    for ax, df, title in zip(axes, df_list, title_list):
        # Plot data
        df.plot.pie(y=config_file["PIE_PLOT_PARAMS"]['y'], ax=ax, colors=config_file["PIE_PLOT_PARAMS"]['colors'],
                    autopct=autopct_outside, startangle=config_file["PIE_PLOT_PARAMS"]['start_angle'],
                    labels=None,
                    # labels=config_file["PIE_PLOT_PARAMS"]['labels'],
                    pctdistance=config_file["PIE_PLOT_PARAMS"]['pct_distance'])
        # # Customize the plot
        ax.set_title(title, fontweight=config_file['PIE_PLOT_PARAMS']['font_weight'])
        ax.set_ylabel('')
        # Add value labels to the pie chart
        ax.legend(labels=df.index, loc=config_file['PIE_PLOT_PARAMS']['loc'], bbox_to_anchor=(
            config_file['PIE_PLOT_PARAMS']['bbox_to_anchor_width'],
            config_file['PIE_PLOT_PARAMS']['bbox_to_anchor_height']))
    # Hide any unused subplots
    for ax in axes[axs_count:]:
        ax.set_visible(False)

    plt.tight_layout()
    # Show the plot
    plt.show()


if __name__ == '__main__':
    conn = S3Connection()
    medsafe_dataset = conn.read_file("medsafe-docs/physicians_migration_additional_cleaned_data.csv",
                                     "medsafe-docs")
    # provide the df for the professional cadre column
    professional_cadre_df = provide_df(medsafe_dataset,
                                       "9. What is your current professional cadre?", "Gender",
                                       "Count")
    # provide the df for the gender column
    gender_cadre_df = provide_df(medsafe_dataset, "2. Your sex", "Gender", "Count")
    # provide the df for the religion column
    Religion_cadre_df = provide_df(medsafe_dataset,
                                   "5. Your religion. (Please, specify the religion if your response is 'Other')",
                                   "Religion", "Count")
    # provide the df for the Marital status column
    Marital_cadre_df = provide_df(medsafe_dataset, "3. Marital status", "Marital status", "Count")
    dataframes_list = [professional_cadre_df, gender_cadre_df, Religion_cadre_df, Marital_cadre_df]
    titles_list = ["Professional cadre", "Gender distribution", "Religious Distribution", "Marital status"]
    multi_h_bar(dataframes_list, titles_list)
    Satisfaction_distribution_df = provide_df(medsafe_dataset,
                                              "15. How satisfied are you with your current professional practice in "
                                              "Nigeria?", "Level of Satisfaction", "Total Count")
    dataframe = Satisfaction_distribution_df
    title = "Satisfaction level of medical professionals practicing in Nigeria"
    single_v_bar(dataframe, title)
    Unsatisfied_table = distributions(medsafe_dataset, "15. How satisfied are you with your current professional "
                                                       "practice in Nigeria?", "9. What is your current professional "
                                                                               "cadre?", "Unsatisfied")
    Very_Unsatisfied_table = distributions(medsafe_dataset, "15. How satisfied are you with your current professional "
                                                            "practice in Nigeria?", "9. What is your current "
                                                                                    "professional cadre?",
                                           "Very unsatisfied")
    Satisfied_table = distributions(medsafe_dataset, "15. How satisfied are you with your current professional "
                                                     "practice in Nigeria?", "9. What is your current professional "
                                                                             "cadre?", "Satisfied")
    Very_Satisfied_table = distributions(medsafe_dataset, "15. How satisfied are you with your current professional "
                                                          "practice in Nigeria?", "9. What is your current "
                                                                                  "professional cadre?",
                                         "Very satisfied")
    dataframes_list = [Very_Unsatisfied_table, Unsatisfied_table, Very_Satisfied_table, Satisfied_table]
    titles_list = ['% of Professions that are Very unsatisfied', '% of Professions that are Unsatisfied',
                   '% of Professions that are Very satisfied', '% of Professions that are Satisfied']
    multi_pie_chart(dataframes_list, titles_list)
    Unsatisfied_Religion_table = pd.DataFrame((distributions(medsafe_dataset,
                                                             "15. How satisfied are you with "
                                                             "your current professional practice "
                                                             "in Nigeria?",
                                                             "5. Your religion. (Please, specify "
                                                             "the religion if your response is "
                                                             "'Other')",
                                                             "Unsatisfied").to_dict()), index=[""])
    Very_Unsatisfied_Religion_table = pd.DataFrame((distributions(medsafe_dataset,
                                                                  "15. How satisfied are you with your current "
                                                                  "professional practice in Nigeria?",
                                                                  "5. Your religion. (Please, specify the religion if "
                                                                  "your response is 'Other')",
                                                                  "Very unsatisfied").to_dict()),
                                                   index=[""])
    Satisfied_Religion_table = pd.DataFrame((distributions(medsafe_dataset,
                                                           "15. How satisfied are you with your current professional "
                                                           "practice in Nigeria?",
                                                           "5. Your religion. (Please, specify the religion if your "
                                                           "response is 'Other')",
                                                           "Satisfied").to_dict()), index=[""])
    Very_Satisfied_Religion_table = pd.DataFrame((distributions(medsafe_dataset,
                                                                "15. How satisfied are you with your current "
                                                                "professional practice in Nigeria?",
                                                                "5. Your religion. (Please, specify the religion if "
                                                                "your response is 'Other')",
                                                                "Very satisfied").to_dict()),
                                                 index=[""])
    dataframe_list = [Unsatisfied_Religion_table, Very_Unsatisfied_Religion_table, Satisfied_Religion_table,
                      Very_Satisfied_Religion_table]
    title_list = ["Religions that are Unsatisfied", "Religions that are Very Unsatisfied",
                  "Religions that are Satisfied", "Religions that are Very Satisfied"]
    multi_v_bar(dataframe_list, title_list, "Religions", "Count")
