# RSE_StudentAnalysis

## Project Overview

This Python project aims to analyze a dataset containing information about first-year students in Germany. The dataset includes details such as semester, nationality, gender, and field of study. The project utilizes the pandas library for data manipulation and matplotlib and seaborn for data visualization.

## Research Questions

The project provides functionality to answer the following research questions:

1. How has the number of German and international students varied per semester in the last 25 years?
2. Which study programs have the highest number of new students in Germany per semester?
3. How many first-year students are there in total in Germany per semester?
4. Are there certain fields of study in which the proportion of foreign first-year students is significantly higher than the proportion of German first-year students?

## Tools and Libraries

The project leverages the following tools and libraries:

- Python: The programming language used for the project.
- pandas: A powerful data manipulation library used to handle and analyze the dataset.
- matplotlib: A popular library for creating visualizations, used to generate charts and graphs.
- seaborn: A data visualization library built on top of matplotlib, used for creating more advanced and aesthetically pleasing visualizations.
- argparse: A library for parsing command-line arguments, used to customize the width and height of the generated plots.
- tabulate: A library for creating formatted tables, used to display the results in a tabular format.
- PIL (Python Imaging Library): A library for image processing, used to open and display PNG images.
- numpy: A library for numerical computations, used in various calculations within the script.
- logging: A library used for logging application events to a file, providing insights into the script's execution.

## Usage Guide

1. Ensure you have Python and the required libraries (pandas, matplotlib, seaborn, argparse, tabulate, PIL, numpy, logging) installed on your system.

2. Place the dataset file "Studienanfänger.csv" in the appropriate location. The script expects the file to be located at "../data/Studienanfänger.csv".

3. Open a terminal or command prompt and navigate to the directory containing the script.

4. Run the script by executing the following command:
   ```
   python main.py [--width <figure_width>] [--height <figure_height>]
   ```

5. The script accepts optional parameters to customize the width and height of the generated plots. If you do not provide these parameters, the script will use the default values of 13 for width and 6 for height.

   Example usage:
   ```
   python main.py --width 15 --height 8
   ```

6. After running the script, it will prompt you to enter the function you want to run. You can choose from the following options:
   - `Semester`: Display the development of the number of German and international students per semester.
   - `Program`: Display the table of the study program with the most students per semester.
   - `Freshmen`: Display the line graph of the number of first-year students per semester.
   - `Ratio`: Display the bar graph of the ratio of international students to German students in study programs where the number of international students is greater than or equal to the number of German students.
   - `Exit`: Exit the program.

7. Depending on the function you choose, the script will generate plots and display the results on the screen.

8. The generated plots and tables will be saved in the "results" directory.

## Code of Conduct and Contribution Guidelines

For information about the project's Code of Conduct and guidelines for contributing to the project, please refer to the following files:

- [CONDUCT.md](CONDUCT.md): This file outlines the expected behavior and standards of conduct for all project participants.
- [CONTRIBUTING.md](CONTRIBUTING.md): This file provides guidelines for contributing to the project, including information about reporting issues, making suggestions, and submitting pull requests.

We encourage all contributors to familiarize themselves with the Code of Conduct and adhere to the guidelines when interacting with the project's community.

## License

This project is licensed under the terms of the [MIT License](LICENSE.txt).

## Citation

If you use this code or find it helpful in your research, please consider citing it using the [CITATION.cff](CITATION.cff) file provided in this repository.

## Contact Information

For any questions or inquiries regarding this project, please feel free to contact:

Email: (Laurenz Gilbert) gilbert@uni-potsdam.de, (Rado Nomena Radimilahy) rado.nomena.radimilahy@uni-potsdam.de, (Nora Hunger) nora.hunger@uni-potsdam.de