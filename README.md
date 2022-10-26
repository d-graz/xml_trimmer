# XML Trimmer
Tool used to trimm-down xml file for 2022-2023 *SMBUS* project
## Usage 
Convert xml database to a more ordinate format and correct `&` error
```
python main.py clean <path/to/your_database.xml> <path/to/cleaned_database.xml>
```
Alterantively you can clean database for csv import. To do so:
```
python main.py clean_csv <path/to/your_database.xml> <path/to/cleaned_database.xml>
```

---

Trimm down size to make file size more feasible for import in neo4j
```
python main.py trimm <path/to/cleaned_database.xml> <path/to/neo4j_database.xml> [#_of_articles,books,...]
```
Defaul size of number of articles is `500`

---
You can now import your xml database in neo4j with
```
CALL apoc.import.xml("neo4j_database.xml")
```
