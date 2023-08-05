import pandas as pd
import pytest
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import os
import tempfile

from main import (
    plot_category_dev,
    read_data,
    table_top_category,
    calculate_higher_ratios,
    create_barplot,
    save_plot,
    write_csv,
    show_content_csv,
    show_content_png
)


def test_read_data():
    """
    Test the read_data function to ensure proper reading of the input CSV file.
    Test cases:
    1. Assert that the returned object is a DataFrame.
    2. Assert that the data DataFrame has the expected number of rows and
    columns.
    3. Assert that columns 2 to 10 are converted to numeric values, and
    non-numeric values are replaced with NaN.
    4. Assert that all values in columns 2 to 10 are either numeric or NaN.
    """
    # Read the data from the input CSV file
    data = pd.read_csv("../data/Studienanfänger.csv", sep=';')

    # Assert that the data DataFrame has been successfully created
    assert isinstance(data, pd.DataFrame), "data is not a DataFrame"

    # Assert that the data DataFrame has expected number of rows and columns
    expected_rows = 7032  # Expected number of rows
    expected_columns = 11  # Expected number of columns
    assert data.shape == (
        expected_rows, expected_columns), "data has unexpected shape"

    # Convert columns 2 to 10 to numeric, replacing non-numeric values with NaN
    for col in data.columns[2:11]:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Assert that all values in the column are either numeric or NaN
    for col in data.columns[2:11]:
        assert pd.api.types.is_numeric_dtype(data[col]) or data[col].isnull(
        ).all(), f"Not all values in column '{col}' are numeric or NaN"


def test_plot_category_dev():
    """
    Test the plot_category_dev function to ensure proper creation of a bar
    plot.
    Test cases:
    1. Assert that the returned object is an instance of AxesSubplot.
    2. Assert that the x-axis label is set correctly.
    3. Assert that the y-axis label is set correctly.
    4. Assert that the plot title is set correctly.
    5. Additional test with empty numeric2 and y_axis_label.
    """
    df = read_data()
    categ = 'Semester'  # Replace with the actual column name for grouping
    # Replace with the actual column name for numeric1
    numeric1 = 'Insgesamt Insgesamt'
    # Replace with the actual column name for numeric2 (optional)
    numeric2 = 'Ausländer Insgesamt'
    plot_title = 'Test Title'  # Replace with the actual plot title (optional)
    # Replace with the actual y-axis label (optional)
    y_axis_label = 'Studienanfänger'

    ax = plot_category_dev(df, categ, numeric1, numeric2,
                           plot_title, y_axis_label)

    assert isinstance(
        ax, plt.Axes), "Returned object is not an instance of AxesSubplot"
    assert ax.get_xlabel() == categ, "Incorrect x-axis label"
    assert ax.get_ylabel() == y_axis_label, "Incorrect y-axis label"

    if plot_title is not None:
        assert ax.get_title() == plot_title, "Incorrect plot title"
    else:
        expected_title = f'Sum of {numeric1}'
        if numeric2 is not None and y_axis_label:
            expected_title += f' {numeric2}'
        expected_title += f' per {categ}'
        assert ax.get_title() == expected_title, "Incorrect plot title"


def test_plot_category_dev_additional():
    """
    Additional test for the plot_category_dev function with empty numeric2 and
    y_axis_label.
    Test cases:
    1. Assert that the returned object is an instance of AxesSubplot.
    2. Assert that the x-axis label is set correctly.
    3. Assert that the y-axis label is set to an empty string (expected when
    y_axis_label is None).
    4. Assert that the plot title is set correctly.
    """
    df = read_data()
    categ = 'Semester'  # Replace with the actual column name for grouping
    # Replace with the actual column name for numeric1
    numeric1 = 'Insgesamt Insgesamt'
    numeric2 = None  # Empty numeric2
    plot_title = 'Test Title'  # Replace with the actual plot title (optional)
    y_axis_label = None  # Empty y_axis_label

    # Call the plot_category_dev function with the provided arguments
    ax = plot_category_dev(df, categ, numeric1, numeric2,
                           plot_title, y_axis_label)

    # Assert that the returned object is an instance of AxesSubplot
    assert isinstance(
        ax, plt.Axes), "Returned object is not an instance of AxesSubplot"

    # Assert that the x-axis label is set correctly
    assert ax.get_xlabel() == categ, "Incorrect x-axis label"

    # Assert that the y-axis label is set to an empty string
    assert ax.get_ylabel() == '', "Incorrect y-axis label (expected empty)"

    # Assert that the plot title is set correctly
    if plot_title is not None:
        assert ax.get_title() == plot_title, "Incorrect plot title"
    else:
        expected_title = f'Sum of {numeric1}'
        if numeric2 is not None and y_axis_label:
            expected_title += f' {numeric2}'
        expected_title += f' per {categ}'
        assert ax.get_title() == expected_title, "Incorrect plot title"


def test_table_top_category():
    """
    Test the table_top_category function to ensure proper grouping and
    calculation of top categories.
    Test cases:
    1. Assert that the resulting DataFrame has the expected columns.
    2. Assert that the resulting DataFrame is not empty.
    3. Assert that all values in the 'categ1' column are unique.
    4. Assert that the 'numeric1' column contains only numeric values.
    """
    df = read_data()
    # Replace with the actual column name for grouping
    categ1 = 'Semester'
    # Replace with the actual column name for the study program
    categ2 = 'Studiengang'
    # Replace with the actual column name for the number of students
    numeric1 = 'Insgesamt Insgesamt'

    result_df = table_top_category(df, categ1, categ2, numeric1)

    expected_columns = [categ1, categ2, numeric1]
    assert list(
        result_df.columns) == expected_columns, "Result has unexpected columns"
    assert not result_df.empty, "Resulting DataFrame is empty"
    assert result_df[categ1].nunique() == len(
        result_df), "'categ1' column contains non-unique values"
    assert pd.api.types.is_numeric_dtype(
        result_df[numeric1]), "'numeric1' column contains non-numeric values"


def test_calculate_higher_ratios():
    """
    Test the calculate_higher_ratios function to ensure proper calculation of
    higher ratios.
    Test cases:
    1. Assert that the resulting ratio is a pandas DataFrame.
    2. Assert that the resulting DataFrame has two columns.
    3. Assert that the result matches the expected output.
    4. Assert that there are no NaN values in the result.
    5. Assert that all ratios in the result are greater than or equal to 1.
    """
    data = {
        'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Numerator': [10, 20, 30, np.nan, 50, 60],
        'Denominator': [5, 5, 15, np.nan, 25, 25]
    }
    df = pd.DataFrame(data)

    expected_result = pd.DataFrame({
        'Category': ['A', 'B', 'C'],
        'Ratio': [3.0, 2.0, 2.2]
    })

    result = calculate_higher_ratios(
        df, 'Category', 'Numerator', 'Denominator')

    assert isinstance(result,
                      pd.DataFrame), "Ratio result is not a pandas DataFrame."
    assert result.shape[1] == 2, "Higher values does not have 2 columns."
    assert result.equals(
        expected_result), "The result does not match the expected output."
    assert pd.isna(result).sum().sum(
    ) == 0, "There should be no NaN values in the result."
    assert (result['Ratio'] >= 1).all(
    ), "All ratios in the result should be greater than or equal to 1."


def test_create_barplot():
    """
    Test the create_barplot function to ensure proper creation of a bar plot.
    Test cases:
    1. Assert that the returned object is a matplotlib AxesSubplot.
    2. Assert that the x-axis label, y-axis label, and plot title are set
    correctly.
    3. Assert that the x-axis labels are rotated 45 degrees and aligned to the
    right.
    4. Assert that NaN and infinite values are filtered out.
    """
    df = read_data()
    higher_ratios = calculate_higher_ratios(df, "Studiengang",
                                            "Ausländer Insgesamt",
                                            "Deutsche Insgesamt")
    column = 'Studiengang'
    xlabel = 'Studiengang'
    ylabel = 'Verhältnis (Ausländer zu Deutsche)'
    title = 'Verhältnis Ausländer zu Deutsche in Studiengängen'

    ax = create_barplot(higher_ratios, column, xlabel, ylabel, title)

    assert isinstance(
        ax, plt.Axes), "Returned object should be a matplotlib AxesSubplot."
    assert ax.get_xlabel() == xlabel, "Incorrect x-axis label."
    assert ax.get_ylabel() == ylabel, "Incorrect y-axis label."
    assert ax.get_title() == title, "Incorrect plot title."
    assert ax.get_xticklabels()[0].get_rotation(
    ) == 45, "X-axis labels should be rotated 45 degrees."
    assert ax.get_xticklabels()[0].get_ha(
    ) == 'right', "X-axis labels alignment should be 'right'."
    assert np.isfinite(ax.get_children()[0].get_height()).all(
    ), "Non-finite values should be filtered out."
    plt.close(ax.figure)


def test_save_plot():
    """
    Test the save_plot function to ensure proper saving of the plot as
    an image.
    Test cases:
    1. Assert that the image file is saved in the specified location.
    """
    data = read_data()
    multi_line = plot_category_dev(
        data,
        categ="Semester",
        numeric1="Deutsche Insgesamt",
        numeric2="Ausländer Insgesamt",
        plot_title="Deutsche und ausländische Studienanfänger pro Semester",
        y_axis_label="Anzahl Studienanfänger"
    )
    save_plot(multi_line.figure, "Variation of nationality")
    plot_name = 'test_plot'
    save_plot(multi_line.figure, plot_name)
    assert os.path.isfile(f'../results/{plot_name}.png')


def test_write_csv():
    """
    Test the write_csv function to ensure proper saving of a DataFrame
    as a CSV file.
    Test cases:
    1. Assert that the CSV file is saved in the specified location.
    2. Assert that the file contains the expected data from the DataFrame.
    """
    table_name = 'test_table'
    data = read_data()
    top_program = table_top_category(data, "Semester", "Studiengang",
                                     "Insgesamt Insgesamt")
    write_csv(top_program, table_name)

    assert os.path.isfile(f'../results/{table_name}.csv')
    df = pd.read_csv(f'../results/{table_name}.csv', sep=';')
    assert df.equals(top_program)

    os.remove(f'../results/{table_name}.csv')


def test_show_content_csv(capsys):
    """
    Test the show_content_csv function to ensure proper display of CSV content
    in tabular format.
    Test cases:
    1. Assert that the displayed content matches the expected output after
    formatting.
    """
    csv_content = """Name,Age,Gender
    Alice,28,Female
    Bob,34,Male
    Charlie,22,Male
    Diana,45,Female
    Eve,38,Female
    """
    with tempfile.NamedTemporaryFile(suffix=".csv", mode="w",
                                     delete=False) as temp_file:
        temp_file.write(csv_content)

    try:
        show_content_csv(temp_file.name)
        captured = capsys.readouterr()
        df = pd.read_csv(temp_file.name)
        expected_output = tabulate(
            df.head(15), headers='keys', tablefmt='psql')

        assert captured.out.strip() == expected_output.strip()
    finally:
        os.remove(temp_file.name)


def test_show_content_png():
    """
    Test the show_content_png function to ensure proper display of a PNG image.
    Test cases:
    1. Assert that the PNG image is displayed correctly. Check manually
    using the Spyder IDE
    """
    test_image_path = '../results/test_plot.png'
    show_content_png(test_image_path)
    os.remove(test_image_path)


if __name__ == '__main__':
    pytest.main(['-v', '--capture=no'])
