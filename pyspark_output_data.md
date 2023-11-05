LOAD operation
See data output below: 
|    | FILM                        |   STARS |   RATING |   VOTES |
|---:|:----------------------------|--------:|---------:|--------:|
|  0 | Fifty Shades of Grey (2015) |       4 |      3.9 |   34846 |
|  1 | Jurassic World (2015)       |     nan |      4.5 |   34390 |
|  2 | American Sniper (2015)      |       5 |      4.8 |   34085 |
|  3 | Furious 7 (2015)            |       5 |      4.8 |   33538 |
|  4 | Inside Out (2015)           |     nan |      4.5 |   15749 |


QUERY operation
SELECT AVG(RATING) FROM Fandango WHERE VOTES > 100
See data output below: 
|    |   avg(RATING) |
|---:|--------------:|
|  0 |       3.96197 |


TRANSFORM operation
See data output below: 
|    | FILM                        |   STARS |   RATING |   VOTES |   Low_Vote_High_Rating |
|---:|:----------------------------|--------:|---------:|--------:|-----------------------:|
|  0 | Fifty Shades of Grey (2015) |       4 |      3.9 |   34846 |                      0 |
|  1 | Jurassic World (2015)       |     nan |      4.5 |   34390 |                      0 |
|  2 | American Sniper (2015)      |       5 |      4.8 |   34085 |                      0 |
|  3 | Furious 7 (2015)            |       5 |      4.8 |   33538 |                      0 |
|  4 | Inside Out (2015)           |     nan |      4.5 |   15749 |                      0 |


LOAD operation
See data output below: 
|    | FILM                        |   STARS |   RATING |   VOTES |
|---:|:----------------------------|--------:|---------:|--------:|
|  0 | Fifty Shades of Grey (2015) |       4 |      3.9 |   34846 |
|  1 | Jurassic World (2015)       |     nan |      4.5 |   34390 |
|  2 | American Sniper (2015)      |       5 |      4.8 |   34085 |
|  3 | Furious 7 (2015)            |       5 |      4.8 |   33538 |
|  4 | Inside Out (2015)           |     nan |      4.5 |   15749 |


QUERY operation
SELECT AVG(RATING) FROM Fandango WHERE VOTES > 100
See data output below: 
|    |   avg(RATING) |
|---:|--------------:|
|  0 |       3.96197 |


TRANSFORM operation
See data output below: 
|    | FILM                        |   STARS |   RATING |   VOTES |   Low_Vote_High_Rating |
|---:|:----------------------------|--------:|---------:|--------:|-----------------------:|
|  0 | Fifty Shades of Grey (2015) |       4 |      3.9 |   34846 |                      0 |
|  1 | Jurassic World (2015)       |     nan |      4.5 |   34390 |                      0 |
|  2 | American Sniper (2015)      |       5 |      4.8 |   34085 |                      0 |
|  3 | Furious 7 (2015)            |       5 |      4.8 |   33538 |                      0 |
|  4 | Inside Out (2015)           |     nan |      4.5 |   15749 |                      0 |


