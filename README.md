For this project, I will input/import NFL Offense statistical data. The data will be manipulated, cleaned, analyzed, and visualized to show how the game has changed over the years.

Requirement 1: Read Data In - There are many ways to read data to be analyzed. I first, created dictionaries of data from (https://www.espn.com/nfl/stats/team/_/stat/passing/table/passing/sort/netPassingYards/dir/desc), and then modified & exported data from https://www.pro-football-reference.com/, saving it to two separate CSV files.

Requirement 2: Manipulate and Clean Your Data - I used pandas functions to rename and delete data columns in the CSV, fill in all nan values with zeros in the data, and convert the data to integers. I also formatted the dictionary data to add commas in the thousands place.

Requirement 3: Analyze Your Data - I used the Len function to be sure all 32 teams were accounted for in the dictionary data. I used the Sum function to add up the total passing yards for each dictionary. 

Requirement 4: Visualize Your Data - I plotted the data from the two CSV files and also plotted the dictionary data just to show that there are multiple ways to enter and look at data. It can be seen that Total NFL Passing Yards has steadily increased throughout the years, while Total NFL Rushing Yards has remained fairly constant and has stayed within a much smaller range. This is likely due to rule changes made over the years that have made the game more pass friendly. It could also stem from the focus on getting Quarterbacks trained and ready at a much younger age and/or a shift in the most athletic players becoming Wide Receivers rather than Running Backs.

In order to run the program on your computer:   
  1. Begin in VS Code using Python 3.10.4
  2. Clone the Repo on GitHub (https://github.com/Monkeyorphan/NFLPassingYards.git)
  3. Open nfl_passing_visualization.ipynb
  4. Install the extensions listed in requirements.txt (notebook, pandas, numpy, matplotlib, csv)
  5. Once you hit Run All, the program should be visible.
