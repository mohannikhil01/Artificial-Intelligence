Given are the 4 files respectively :
1. IDS.py
2. Heuristic1.py
3. Heuristic2.py
4. Report.txt

1. IDS.py

	This python file contains the code for the Iterative Deepening Search. This file also includes 4 sample initial game states for which the respective results can be witnessed ( mentioned in the Report.txt).

The control flow for this file is as follows:
main()
iterativeDeepeningSearch()
depthLimitedSearch()[Recuresive] { generateChildren(), goalReached() }
getPath() { logicPrint() }

The use of each of the methods is defined in the file.

2. Heuristic1.py

	This python file contains the code for the A* Algorithm using the manhattan distance as the heuristic function. This file also includes 4 sample initial game states for which the respective results can be witnessed ( mentioned in the Report.txt).

The control flow for this file is as follows:
main()
heuristicSearch() { getAdjacentCells(), goalReached(), getF(), getG(), getHeuristics() }
getPath() { logicPrint() }

The use of each of the methods is defined in the file.

3. Heuristic2.py

	This python file contains the code for the A* Algorithm using the distance of the pegs from the middle line of the board as the heuristic function. This file also includes 4 sample initial game states for which the respective results can be witnessed ( mentioned in the Report.txt).

The control flow for this file is as follows:
main()
heuristicSearch() { getAdjacentCells(), goalReached(), getF(), getG(), getHeuristics() }
getPath() { logicPrint() }

The use of each of the methods is defined in the file.

4. Report.txt

	This file contains the output of various test cases solved using the above 3 search techniques.
