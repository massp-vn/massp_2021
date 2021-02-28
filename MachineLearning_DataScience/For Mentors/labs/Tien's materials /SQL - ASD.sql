/* write your SQL and answers */
/* Execution of various SQL commands based on Autism dataset: */

/*     How many middle eastern children show ASD traits ? */

SELECT COUNT(*) 
FROM "Toddler Autism dataset"
WHERE [Ethnicity]="middle eastern" AND [Class/ASDTraits]="Yes";

/*     How many children who have Jaundice show ASD traits ? */

SELECT COUNT(*) 
FROM "Toddler Autism dataset"
WHERE [Jaundice]="yes" AND [Class/ASDTraits]="Yes";

/*     Are ASD traits dependent on hereditary ? Justify . */

SELECT [Family_mem_with_ASD], [Class/ASDTraits], COUNT(*) 
FROM "Toddler Autism dataset"
GROUP BY  [Family_mem_with_ASD], [Class/ASDTraits]

/*  Answer: No, Incase the data set is good enought, the proportion of show ASD traits in Family had mem with ASD( 115/55=2.09) ie 
nearly equal (even less than)  with the proportion of show ASD traits in Family didn't has mem with ASD ( 613/271=2.26) */

/*     People of which ethnicity are most likely to exhibit ASD traits ? */
/* ===> The ethnicity have highest number case of ASD traits */ 
SELECT Ethnicity, COUNT(Ethnicity) AS C
FROM "Toddler Autism dataset"
GROUP BY Ethnicity
HAVING [Class/ASDTraits] = "Yes"
ORDER BY C DESC
LIMIT 1;

/*  ===> The ethnicity have highest proportion of ASD traits/total */
WITH TotalTable AS (
	SELECT Ethnicity, COUNT(Ethnicity) AS T
	FROM "Toddler Autism dataset"
	GROUP BY Ethnicity
),  ASDTable AS (
	SELECT Ethnicity, COUNT(Ethnicity) AS C, [Class/ASDTraits]
	FROM "Toddler Autism dataset"
	WHERE [Class/ASDTraits]="Yes"
	GROUP BY Ethnicity
)
SELECT TotalTable.Ethnicity, [C]*1.0/[T] AS  PROPORTION
FROM TotalTable, ASDTable
Where TotalTable.Ethnicity = ASDTable.Ethnicity
ORDER BY PROPORTION DESC
LIMIT 1;

/*     What is the proportion of a white European girls (female) exhibit ASD traits among all white European girls? */

WITH TempTable
AS
( 
    SELECT [sex], [Ethnicity], [Class/ASDTraits] 
	FROM "Toddler Autism dataset"
	WHERE [sex]="f" AND [Ethnicity]="White European"
  )
SELECT  [Ethnicity], [sex], [Class/ASDTraits], (COUNT(*) * 1.0 / (SELECT COUNT(*) FROM TempTable)) AS [PROPORTION]
FROM TempTable
WHERE [Class/ASDTraits]="Yes" AND [Ethnicity]="White European" AND [sex]="f" 
GROUP BY [sex], [Ethnicity], [Class/ASDTraits];