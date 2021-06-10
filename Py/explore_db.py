# Explor JUR db
import psycopg2
import psycopg2.extras

# Explore data
def get_tables():

    """
    Create and return a list of dictionaries with the
    schemas and names of tables in the database
    connected to by the connection argument.
    """
    params = config()
    # connect to the PostgreSQL server
    connection = psycopg2.connect(**params)
    # create a cursor
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("""SELECT table_schema, table_name
                      FROM information_schema.tables
                      WHERE table_schema != 'pg_catalog'
                      AND table_schema != 'information_schema'
                      AND table_type='BASE TABLE'
                      ORDER BY table_schema, table_name""")

    tables = cursor.fetchall()

    cursor.close()

    return tables


def print_tables(tables):

    """
    Prints the list created by get_tables
    """

    for row in tables:

        print("{}.{}".format(row[0], row[1]))
        

def get_columns(table_schema, table_name):

    """
    Creates and returns a list of dictionaries for the specified
    schema.table in the database connected to.
    """
    params = config()
    # connect to the PostgreSQL server
    connection = psycopg2.connect(**params)

    where_dict = {"table_schema": table_schema, "table_name": table_name}

    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("""SELECT column_name, ordinal_position, is_nullable, data_type, character_maximum_length
                      FROM information_schema.columns
                      WHERE table_schema = %(table_schema)s
                      AND table_name   = %(table_name)s
                      ORDER BY ordinal_position""",
                      where_dict)

    columns = cursor.fetchall()

    cursor.close()

    return columns


def print_columns(columns):

    """
    Prints the list created by get_columns.
    """

    for row in columns:

        print("Column Name:              {}".format(row["column_name"]))
        print("Ordinal Position:         {}".format(row["ordinal_position"]))
        print("Is Nullable:              {}".format(row["is_nullable"]))
        print("Data Type:                {}".format(row["data_type"]))
        print("Character Maximum Length: {}\n".format(row["character_maximum_length"]))     


def get_tree():

    """
    Uses get_tables and get_columns to create a tree-like data
    structure of tables and columns.

    It is not a true tree but a list of dictionaries containing
    tables, each dictionary having a second dictionary
    containing column information.
    """
    params = config()
    # connect to the PostgreSQL server
    connection = psycopg2.connect(**params)

    tree = get_tables()

    for table in tree:

        table["columns"] = get_columns(table["table_schema"], table["table_name"])

    return tree


def print_tree(tree):

    """
    Prints the tree created by get_tree
    """

    for table in tree:

        print("{}.{}".format(table["table_schema"], table["table_name"]))

        for column in table["columns"]:

            print(" |-{} ({})".format(column["column_name"], column["data_type"]))


#-----------------------
cursor = connection.cursor()
postgreSQL_select_Query = "select * from public.jur_sumarios"
cursor.execute(postgreSQL_select_Query)
records = cursor.fetchmany(10)
records[1]

postgreSQL_select_Query = "select table_name, pg_relation_size(quote_ident(table_name)) from information_schema.tables where table_schema = 'public' order by 2"
cursor.execute(postgreSQL_select_Query)
tamaño_tabla = cursor.fetchall()
tamaño_tabla
print(pd.DataFrame(tamaño_tabla))

postgreSQL_select_Query = "select * from public.jur_fallos"
cursor.execute(postgreSQL_select_Query)
fallos = cursor.fetchmany(10)
fallos[1]
