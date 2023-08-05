import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from PIL import Image
import numpy as np
import logging


# Logger
def setup_logger():
    """
    Set up a logger for logging application events to a file.

    Returns:
        logging.Logger: A Logger object configured to log events
        to 'execution.log' file.
    """
    logging.basicConfig(filename="execution.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger


# Data Layer
def read_data():
    """
    Reads the data from the input CSV file and performs data cleaning.

    Returns:
        pandas.DataFrame: The cleaned DataFrame.
    """
    try:
        logging.info("Attempting to read data.")
        data = pd.read_csv("../data/Studienanfänger.csv", sep=';')

        for col in data.columns[2:11]:
            logging.debug(f'Reading in {col}')
            data[col] = pd.to_numeric(data[col], errors='coerce')

        logging.info("Data read successfully.")
        return data
    except Exception as e:
        logging.error("Failed to read data. Error: %s", e)


# Presentation Layer
def plot_category_dev(df, categ, numeric1, numeric2=None, plot_title=None,
                      y_axis_label=None, figure_width=13, figure_height=6):
    """
    Displays the development of numerical categories in a multiple line plot
    while grouping them according to a given category.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        categ (str): The column name to group the data.
        numeric1 (str): The column name for the first numeric data.
        numeric2 (str): The column name for the second numeric data (optional).
        plot_title (str): The title of the plot (optional).
        y_axis_label (str): The label for the y-axis (optional).
        figure_width (int): The width of the plot figure (default: 13).
        figure_height (int): The height of the plot figure (default: 6).

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The plot object.
    """
    try:
        logging.info("Executing plot_category_dev function")

        logging.info(
            "Grouping DataFrame by category and calculating "
            "sum of the first numeric column")

        sum_numeric1 = df.groupby(categ)[numeric1].sum()

        logging.info("Setting plot style and creating the initial line plot")
        sns.set_theme(style='whitegrid')

        plt.figure(figsize=(figure_width, figure_height), dpi=200)
        ax = sns.lineplot(data=sum_numeric1, color='blue', label=numeric1)
        plt.xlabel(categ, fontsize=12)
        plt.ylabel(y_axis_label, fontsize=12)

        if numeric2 is not None:
            logging.info("Second numeric column detected, adding to the plot")
            sum_numeric2 = df.groupby(categ)[numeric2].sum()
            ax = sns.lineplot(data=sum_numeric2,
                              color='orange', label=numeric2)

        logging.info("Setting plot title")
        if plot_title is not None:
            plt.title(plot_title, fontsize=14)
        else:
            title = (f'Sum of {numeric1} per {categ}'
                     if numeric2 is None
                     else f'Sum of {numeric1} {numeric2} per {categ}')
            plt.title(title, fontsize=14)

        plt.xticks(rotation=45, ha='right')

        logging.info("Removing top and right spines from the plot")
        sns.despine()

        logging.info("Displaying plot legend")
        plt.legend()

        logging.info("Finalizing plot layout and displaying it")
        plt.tight_layout()

        logging.info("Finished plot_category_dev function successfully")

        return ax
    except Exception as e:
        logging.error(
            f"{e} occurred in plot_category_dev function", exc_info=True)


def table_top_category(df, categ1, categ2, numeric1):
    """
    Finds the study program with the most students per semester.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        categ1 (str): The column name to group the data.
        categ2 (str): The column name representing the study program.
        numeric1 (str): The column name representing the number of students.

    Returns:
        pandas.DataFrame: The resulting DataFrame with the top study program
        per semester.
    """
    try:
        logging.info("Executing table_top_category function")

        logging.info(
            "Grouping DataFrame by first category"
            " and calculating max of numeric column")
        max_program = df.groupby(categ1)[numeric1].idxmax()

        logging.info(
            "Creating DataFrame with the top study program per semester")
        max_program_df = df.loc[max_program,
                                [categ1, categ2,
                                 numeric1]].reset_index(drop=True)

        logging.info("Finished table_top_category function successfully")

        return max_program_df

    except Exception as e:
        logging.error(
            f"{e} occurred in table_top_category function", exc_info=True)


def calculate_higher_ratios(df, category_column, numerator_column,
                            denominator_column):
    """
    Calculates the ratio between two numeric columns in a DataFrame and
    returns the values that are greater than or equal to 1.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        category_column (str): The column name to group the data.
        numerator_column (str): The column name representing the numerator in
                                the ratio calculation.
        denominator_column (str): The column name representing the denominator
                                  in the ratio calculation.

    Returns:
        pandas.DataFrame: The resulting DataFrame with index reset, containing
                the values of the ratio that are greater than or equal to 1.
    """
    try:
        logging.info("Executing calculate_higher_ratios function")

        logging.info("Replacing NaN values with 0 in the DataFrame")
        df = df.fillna(0)

        logging.info(
            "Calculating ratios and filtering"
            " those greater than or equal to 1")
        ratio = (df.groupby(category_column)[numerator_column].sum() /
                 df.groupby(category_column)[denominator_column].sum())
        higher_values = ratio[ratio >= 1].reset_index()

        logging.info("Renaming second column to 'Ratio'")
        higher_values.rename(columns={higher_values.columns[1]: 'Ratio'},
                             inplace=True)

        logging.info("Finished calculate_higher_ratios function successfully")

        return higher_values

    except Exception as e:
        logging.error(
            f"{e} occurred in calculate_higher_ratios function", exc_info=True)


def create_barplot(dataframe, column, xlabel, ylabel,
                   title, figure_width=13, figure_height=6):
    """
    Creates a bar plot using Seaborn.

    Args:
        dataframe (pandas.DataFrame): The DataFrame containing the data.
        column (str): The column name for the x-axis values.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        title (str): The title of the plot.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The plot object.
    """
    try:
        logging.info("Executing create_barplot function")

        logging.info(
            "Extracting study programs and their values from the DataFrame")
        study_program = dataframe[column]
        values = dataframe['Ratio']

        logging.info("Filtering out NaN and infinite values")
        mask = np.isfinite(values)
        study_program = study_program[mask]
        values = values[mask]

        logging.info("Creating the bar plot using Seaborn")
        plt.figure(figsize=(figure_width, figure_height))
        ax = sns.barplot(x=study_program, y=values)

        logging.info("Configuring the appearance of the plot")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.gca().xaxis.set_tick_params(pad=8)

        logging.info("Adding annotations for the exact values above each bar")
        for i, v in enumerate(values):
            ax.text(i, v, str(round(v, 2)), ha='center', va='bottom')

        logging.info("Finalizing the plot and displaying it")
        plt.tight_layout()

        logging.info("Finished create_barplot function successfully")

        return ax

    except Exception as e:
        logging.error(
            f"{e} occurred in create_barplot function", exc_info=True)


def save_plot(plot_obj, plot_name):
    """
    Save the plot in a .png file in the result directory.

    Args:
        plot_obj (matplotlib.figure.Figure): The plot object to be saved.
        plot_name (str): The name of the plot.

    Returns:
        None
    """
    try:
        logging.info("Executing save_plot function")
        plot_obj.savefig('../results/' + plot_name + '.png')

        logging.info("Finished save_plot function successfully")

    except Exception as e:
        logging.error(
            f"{e} occurred while saving plot in save_plot",
            " function", exc_info=True)


def write_csv(data_frame, table_name):
    """
    Saves the DataFrame into a CSV file with semicolon (;) separator.

    Args:
        data_frame (pandas.DataFrame): The DataFrame to be saved.
        table_name (str): The name of the table or file.

    Returns:
        None
    """
    try:
        logging.info("Executing write_csv function")

        filepath = '../results/' + table_name + '.csv'

        logging.info("Writing DataFrame to CSV file at path: %s", filepath)
        data_frame.to_csv(filepath, sep=';', index=False)

        logging.info("Finished write_csv function successfully")
    except Exception as e:
        logging.error(f"{e} occurred in write_csv function", exc_info=True)


def show_content_csv(file_csv):
    """
    Reads a CSV file and displays its content as a formatted table.

    Args:
        file_csv (str): The path to the CSV file.

    Returns:
        None
    """
    try:
        logging.info("Executing show_content_csv function")

        logging.info(f"Reading CSV file from path: {file_csv}")
        df = pd.read_csv(file_csv)

        logging.info("Converting DataFrame to a formatted table")
        table = tabulate(df.head(15), headers='keys', tablefmt='psql')

        logging.info("Displaying the table")
        print(table)

        logging.info("Finished show_content_csv function successfully")

    except Exception as e:
        logging.error(
            f"{e} occurred in show_content_csv function", exc_info=True)


def show_content_png(file_png):
    """
    Opens and displays a PNG image.

    Args:
        file_png (str): The path to the PNG image file.

    Returns:
        None
    """
    try:
        logging.info("Executing show_content_png function")

        logging.info(f"Opening PNG file at {file_png}")
        image = Image.open(file_png)

        logging.info("Creating new figure and displaying the image")
        fig = plt.figure(figsize=(50, 50))
        plt.imshow(image)
        plt.axis('off')

        logging.info("Displaying the figure")
        plt.show()

        logging.info("Finished show_content_png function successfully")

    except Exception as e:
        logging.error(
            f"{e} occurred in show_content_png function", exc_info=True)


# Controller Layer
def call_student_semester(data, figure_width, figure_height):
    """
    Displays the development of the number of German and international
    students per semester.

    Args:
        data (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    try:
        logging.info("Executing call_student_semester function")

        logging.info(
            "Generating plot for the development of"
            " the number of German and international students per semester")

        multi_line = plot_category_dev(
            data,
            categ="Semester",
            numeric1="Deutsche Insgesamt",
            numeric2="Ausländer Insgesamt",
            plot_title=("Deutsche und ausländische Studienanfänger "
                        "pro Semester"),
            y_axis_label="Anzahl Studienanfänger",
            figure_width=figure_width,
            figure_height=figure_height
        )

        logging.info("Saving plot as a PNG file")
        save_plot(multi_line.figure, "Variation of nationality")

        logging.info("Closing the plot after saving")
        plt.close()

        logging.info("Displaying the saved PNG plot")
        show_content_png('../results/Variation of nationality.png')

        logging.info("Closing the plot after display")
        plt.close()

        logging.info("Finished call_student_semester function successfully")

    except Exception as e:
        logging.error(
            f"{e} occurred in call_student_semester function", exc_info=True)


def call_top_program(data):
    """
    Displays the table of the study program with the most students
    per semester.

    Args:
        data (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    try:
        logging.info("Executing call_top_program function")

        logging.info(
            "Running table_top_category function to find the"
            " most popular study program per semester")
        top_program = table_top_category(data, "Semester", "Studiengang",
                                         "Insgesamt Insgesamt")

        logging.info("Writing the results to a CSV file")
        write_csv(top_program, "Popular study program")

        logging.info("Displaying the content of the CSV file")
        show_content_csv('../results/Popular study program.csv')

        logging.info("Finished call_top_program function successfully")

    except Exception as e:
        logging.error(
            f"{e} occurred in call_top_program function", exc_info=True)


def call_freshmen_plot(data, figure_width, figure_height):
    """
    Displays the line graph of the number of first-year students per semester.

    Args:
        data (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    try:
        logging.info("Executing call_freshmen_plot function")

        logging.info("Creating a plot of first-year students per semester")
        plot_category_dev(data, "Semester", "Insgesamt Insgesamt",
                          plot_title="Studienanfänger Insgesamt pro Semester",
                          y_axis_label="Anzahl Studienanfänger",
                          figure_width=figure_width,
                          figure_height=figure_height)

        logging.info("Saving the plot")
        save_plot(plt, "First year students per semester")

        logging.info("Closing the plot object")
        plt.close()

        logging.info("Displaying the saved plot content")
        show_content_png('../results/First year students per semester.png')

        logging.info("Closing the plot after display")
        plt.close()

        logging.info("Finished call_freshmen_plot function successfully")

    except Exception as e:
        logging.error(
            f"{e} occurred in call_freshmen_plot function", exc_info=True)


def call_higher_ratio(data, figure_width, figure_height):
    """
    Displays the bar graph of the ratio of international students to German
    students in study programs where the number of international students
    is greater than or equal to the number of German students.

    Args:
        data (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    try:
        logging.info("Executing call_higher_ratio function")

        logging.info("Calculating higher ratios")
        higher_ratios = calculate_higher_ratios(data, "Studiengang",
                                                "Ausländer Insgesamt",
                                                "Deutsche Insgesamt")

        logging.info("Creating bar plot")
        create_barplot(
            higher_ratios,
            column='Studiengang',
            xlabel='Studiengang',
            ylabel='Verhältnis (Ausländer zu Deutsche)',
            title='Verhältnis Ausländer zu Deutsche in Studiengängen',
            figure_width=figure_width,
            figure_height=figure_height
        )

        logging.info("Saving the plot")
        save_plot(plt, "Higher ratio")

        logging.info("Closing the generated plot")
        plt.close()

        logging.info("Displaying the saved plot")
        show_content_png('../results/Higher ratio.png')

        logging.info("Closing the plot after display")
        plt.close()

        logging.info("Finished call_higher_ratio function successfully")

    except Exception as e:
        logging.error(
            f"{e} occurred in call_higher_ratio function", exc_info=True)


def main():
    """This function is the entry point of the program and starts it"""
    try:
        logging = setup_logger()

        parser = argparse.ArgumentParser(
            description="Plot figure size options")
        parser.add_argument("--width", type=int,
                            default=13, help="Figure width")
        parser.add_argument("--height", type=int,
                            default=6, help="Figure height")

        logging.info("Executing main function")

        logging.info("Reading the data")
        data_set = read_data()

        # Parse the command-line arguments
        args = parser.parse_args()

        # Process user requests
        while True:
            prompt = ("Which function do you want to run? "
                      "(e.g. Semester, Program, Freshmen, Ratio, Exit): ")
            user_input = input(prompt)

            if user_input == 'Semester':
                logging.info("Executing call_student_semester function")
                call_student_semester(data_set, figure_width=args.width,
                                      figure_height=args.height)
                plt.close()
            elif user_input == 'Program':
                logging.info("Executing call_top_program function")
                call_top_program(data_set)
            elif user_input == 'Freshmen':
                logging.info("Executing call_freshmen_plot function")
                call_freshmen_plot(data_set, figure_width=args.width,
                                   figure_height=args.height)
                plt.close()
            elif user_input == 'Ratio':
                logging.info("Executing call_higher_ratio function")
                call_higher_ratio(data_set, figure_width=args.width,
                                  figure_height=args.height)
                plt.close()
            elif user_input == 'Exit':
                logging.info("Exiting the program")
                raise SystemExit
            else:
                # Program continues after any invalid input
                logging.warning('Invalid input provided by user')
                print('Invalid input')
                continue

    except Exception as e:
        logging.error(f"{e} occurred in main function", exc_info=True)


if __name__ == '__main__':
    main()
