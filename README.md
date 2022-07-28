For this project, I will use NFL Total Regular Season Passing Yards data from the ESPN website (https://www.espn.com/nfl/stats/team/_/stat/passing/table/passing/sort/netPassingYards/dir/desc) and enter it in VSCode by creating Dictionaries. Each Dictionary will contain the Total Yards Passing of each NFL team, and there will be a Dictionary for each season between 2004 and 2021. Once the raw data has been added, I will use the LEN function to confirm no team was left out of each season and the SUM function to add up the Team Totals to equal a League Total for each season. I wll clean it up further by formatting the values so that they contain commas. The data will be analyzed to see how the passing yards per season have been trending. I will then add visualization with matplotlib so that it is easily digestible. Markdowns will be included in each cell to explain why each step is taken. 

In order to run the program on your computer:   
1. Begin in VS Code using Python 3.10.4
2. Clone the Repo on GitHub (https://github.com/Monkeyorphan/NFLPassingYards.git)
3. Open nfl_passing_visualization.ipynb
4. Install the extensions listed in requirements.txt (notebook, pandas, numpy, matplotlib)
5. Once you hit Run All, the program should be visible.

The data and visualization makes it obvious that NFL Total Regular Season Passing Yards have been trending upward, with a couple of years that could be considered anomalies.

- Troy Nally