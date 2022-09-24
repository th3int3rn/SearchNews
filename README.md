# News Search

### Search routines to perform queries on a set of documents

#### The documents are line separated and are referenced in the order they appear, e.g.
| News article | Reference  | 
| :-----: | :---: |
| June 5 , 2013 : The majority ... | 0   |
| July 9 , 2013 : The HSCIC has ...| 0   |
#### Acceptance criteria:
| Query | Type of search   | Expected outcome: document references   |
| :-----: | :---: | :---: |
| Care Quality Commission | OR   | 0,1,2,3,4,5,6  |
| September 2004 | OR   | 9 |
| general population generally | OR   | 6,8  |
| Care Quality Commission admission | AND   | 1 |
| general population Alzheimer | AND   | 6  |

#### Command to run:
####### Test all acceptance criteria us:
     E.g.: python3 Search.py -q "Care Quality Commission admission" -t "and"  