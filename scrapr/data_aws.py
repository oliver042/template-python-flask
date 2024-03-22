import boto3
import uuid

# Initialisiere einen DynamoDB-Client
dynamodb = boto3.resource('dynamodb')

# Definiere die Attribute der Tabelle
table_name = 'NeueTabelle'
attribute_definitions = [
    {
        'AttributeName': 'PrimaryKey',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'Name',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'Alter',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'Beruf',
        'AttributeType': 'S'
    }
    # Fügen Sie hier weitere Attribute hinzu, falls nötig
]

# Definiere den Primärschlüssel der Tabelle
key_schema = [
    {
        'AttributeName': 'PrimaryKey',
        'KeyType': 'HASH'  # 'HASH' für den Partitionsschlüssel, 'RANGE' für den Sortierschlüssel
    },
    # Fügen Sie hier den Sortierschlüssel hinzu, falls nötig
]

# Definiere die Durchsatzspezifikationen
provisioned_throughput = {
    'ReadCapacityUnits': 10,
    'WriteCapacityUnits': 10
}

# Erstelle die DynamoDB-Tabelle
table = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=attribute_definitions,
    KeySchema=key_schema,
    ProvisionedThroughput=provisioned_throughput
)

# Warte bis die Tabelle erstellt wurde
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

print(f'Tabelle {table_name} wurde erfolgreich erstellt.')

# Daten, die in die Tabelle eingefügt werden sollen
# Hier als Beispiel ein Dictionary mit mehreren Einträgen
data_items = [
    {
        'Name': 'Max Mustermann',
        'Alter': 30,
        'Beruf': 'Ingenieur'
    },
    {
        'Name': 'Erika Mustermann',
        'Alter': 28,
        'Beruf': 'Architektin'
    }
    # Fügen Sie hier weitere Dictionaries hinzu
]

# Wähle deine DynamoDB-Tabelle
table = dynamodb.Table(table_name)

# Füge jedes Dictionary aus der Liste in die DynamoDB-Tabelle ein
for data in data_items:
    # Generiere eine eindeutige UUID für den Primärschlüssel
    data['PrimaryKey'] = str(uuid.uuid4())
    # Füge die Daten in die DynamoDB-Tabelle ein
    table.put_item(Item=data)

print(f'Daten wurden erfolgreich in die DynamoDB-Tabelle {table_name} hochgeladen.')

# In diesem Codebeispiel:
# - `AttributeType` 'S' steht für String und 'N' für Number.
# - Die `attribute_definitions` wurden um die Attribute 'Name', 'Alter' und 'Beruf' erweitert, die den Schlüsseln im `data_items` Dictionary entsprechen.
# - Stellen Sie sicher, dass die Attribute in den Dictionaries den Spaltennamen in Ihrer DynamoDB-Tabelle entsprechen und dass die AWS-Zugangsdaten konfiguriert sind. Ändern Sie `table_name`, `attribute_definitions`, `key_schema`, `provisioned_throughput` und `data_items` entsprechend Ihren Anforderungen.
